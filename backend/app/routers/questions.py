"""Questions router"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.question import Question, DifficultyLevel
from app.models.choice import Choice
from app.models.hint import Hint

router = APIRouter(prefix="/api/questions", tags=["questions"])


@router.get("/")
def get_questions(
    subject_id: Optional[int] = Query(None),
    difficulty: Optional[str] = Query(None),
    limit: int = Query(15, ge=1, le=50),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """
    Get questions with optional filters
    
    Args:
        subject_id: Filter by subject
        difficulty: Filter by difficulty (EASY, MEDIUM, HARD)
        limit: Maximum number of questions to return
        offset: Number of questions to skip
        
    Returns:
        List of questions with choices
    """
    query = db.query(Question).filter(
        Question.is_active == True,
        Question.source_document.is_(None)  # Only curated questions
    )
    
    if subject_id:
        query = query.filter(Question.subject_id == subject_id)
    
    if difficulty:
        try:
            diff_level = DifficultyLevel[difficulty.upper()]
            query = query.filter(Question.difficulty == diff_level)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid difficulty level")
    
    questions = query.offset(offset).limit(limit).all()
    
    result = []
    import random
    
    for question in questions:
        choices = db.query(Choice).filter(Choice.question_id == question.id).order_by(Choice.letter).all()
        
        # Find the correct answer
        correct_choice = next((c for c in choices if c.is_correct), choices[0])
        
        # Shuffle the options
        shuffled_choices = list(choices)
        random.shuffle(shuffled_choices)
        
        # Find new position of correct answer
        correct_answer_index = shuffled_choices.index(correct_choice)
        
        result.append({
            "id": question.id,
            "question_text": question.question_text,
            "difficulty": question.difficulty.value,
            "options": [c.choice_text for c in shuffled_choices],
            "correct_answer": correct_answer_index,
            "explanation": question.explanation
        })
    
    return result


@router.get("/{question_id}/hint")
def get_hint(question_id: int, db: Session = Depends(get_db)):
    """
    Get hint for a specific question
    
    Args:
        question_id: Question ID
        
    Returns:
        Hint text
    """
    hint = db.query(Hint).filter(Hint.question_id == question_id).first()
    
    if not hint:
        raise HTTPException(status_code=404, detail="Hint not found")
    
    return {
        "hint": hint.hint_text,
        "is_ai_generated": hint.is_ai_generated
    }
