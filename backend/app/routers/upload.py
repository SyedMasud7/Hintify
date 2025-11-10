"""Upload router for document processing and question generation"""

import os
import logging
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.subject import Subject
from app.models.question import Question, DifficultyLevel
from app.models.choice import Choice
from app.models.hint import Hint
from app.services.document_parser import DocumentParser
from app.services.question_generator import QuestionGenerator
from app.ai.factory import get_provider_instance

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/upload", tags=["upload"])

# File upload constraints
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.pptx'}
UPLOAD_DIR = "uploads"

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    subject_id: int = Form(...),
    db: Session = Depends(get_db)
):
    """
    Upload a document and generate 45 questions (15 easy, 15 medium, 15 hard)
    
    Args:
        file: Uploaded file (PDF, DOCX, or PPTX)
        subject_id: Subject ID for the generated questions
        db: Database session
        
    Returns:
        JSON with generated questions and metadata
    """
    logger.info(f"Received upload: {file.filename}, subject_id: {subject_id}")
    
    # Validate subject exists
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    # Validate file extension
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Read file content
    content = await file.read()
    file_size = len(content)
    
    # Validate file size
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size: {MAX_FILE_SIZE / 1024 / 1024}MB"
        )
    
    logger.info(f"File size: {file_size / 1024:.2f}KB")
    
    # Save file temporarily
    temp_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(temp_path, 'wb') as f:
            f.write(content)
        
        # Parse document
        logger.info("Parsing document...")
        parser = DocumentParser()
        text = parser.parse_document(temp_path)
        
        if not text or len(text) < 100:
            raise HTTPException(
                status_code=400,
                detail="Document contains insufficient text content"
            )
        
        logger.info(f"Extracted {len(text)} characters")
        
        # Generate questions using AI
        logger.info("Generating questions with AI...")
        ai_provider = get_provider_instance()
        generator = QuestionGenerator(ai_provider)
        
        questions_data = await generator.generate_from_text(
            text=text,
            subject_id=subject_id,
            filename=file.filename,
            count=45
        )
        
        if len(questions_data) < 45:
            logger.warning(f"Only generated {len(questions_data)} questions, expected 45")
        
        # Save questions to database
        logger.info("Saving questions to database...")
        saved_questions = []
        
        for q_data in questions_data:
            # Create question
            question = Question(
                subject_id=subject_id,
                question_text=q_data.question_text,
                difficulty=DifficultyLevel[q_data.difficulty],
                explanation=q_data.explanation,
                source_document=file.filename
            )
            db.add(question)
            db.flush()  # Get question ID
            
            # Create choices
            for i, option_text in enumerate(q_data.options):
                choice = Choice(
                    question_id=question.id,
                    choice_text=option_text,
                    is_correct=(i == q_data.correct_answer),
                    letter=chr(65 + i)  # A, B, C, D
                )
                db.add(choice)
            
            # Create hint (check if one already exists)
            existing_hint = db.query(Hint).filter(Hint.question_id == question.id).first()
            if not existing_hint:
                hint = Hint(
                    question_id=question.id,
                    hint_text=q_data.hint,
                    is_ai_generated=True
                )
                db.add(hint)
            else:
                # Update existing hint
                existing_hint.hint_text = q_data.hint
                existing_hint.is_ai_generated = True
            
            saved_questions.append({
                "id": question.id,
                "question_text": question.question_text,
                "difficulty": question.difficulty.value,
                "options": q_data.options,
                "hint": q_data.hint
            })
        
        db.commit()
        logger.info(f"Successfully saved {len(saved_questions)} questions")
        
        # Count by difficulty
        difficulty_counts = {
            "EASY": sum(1 for q in questions_data if q.difficulty == "EASY"),
            "MEDIUM": sum(1 for q in questions_data if q.difficulty == "MEDIUM"),
            "HARD": sum(1 for q in questions_data if q.difficulty == "HARD")
        }
        
        return {
            "success": True,
            "message": "Document processed successfully",
            "filename": file.filename,
            "subject": subject.name,
            "questions_generated": len(saved_questions),
            "difficulty_distribution": difficulty_counts,
            "questions": saved_questions
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing upload: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(e)}"
        )
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
                logger.info("Cleaned up temporary file")
            except Exception as e:
                logger.warning(f"Failed to remove temp file: {e}")


@router.get("/uploaded-questions")
def get_uploaded_questions(db: Session = Depends(get_db)):
    """
    Get all questions generated from uploaded documents
    
    Returns:
        List of uploaded questions with metadata
    """
    questions = db.query(Question).filter(
        Question.source_document.isnot(None)
    ).all()
    
    result = []
    import random
    
    for question in questions:
        # Get choices
        choices = db.query(Choice).filter(Choice.question_id == question.id).all()
        sorted_choices = sorted(choices, key=lambda x: x.letter)
        
        # Find the correct answer
        correct_choice = next((c for c in sorted_choices if c.is_correct), sorted_choices[0])
        
        # Shuffle the options
        shuffled_choices = list(sorted_choices)
        random.shuffle(shuffled_choices)
        
        # Find new position of correct answer
        correct_answer_index = shuffled_choices.index(correct_choice)
        options = [c.choice_text for c in shuffled_choices]
        
        result.append({
            "id": question.id,
            "question_text": question.question_text,
            "difficulty": question.difficulty.value,
            "options": options,
            "correct_answer": correct_answer_index,
            "explanation": question.explanation or "No explanation available.",
            "subject_id": question.subject_id,
            "source_document": question.source_document
        })
    
    return result
