"""Subjects router"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.subject import Subject
from app.models.question import Question

router = APIRouter(prefix="/api/subjects", tags=["subjects"])


@router.get("/")
def get_subjects(db: Session = Depends(get_db)):
    """
    Get all active subjects with question counts
    
    Returns:
        List of subjects with metadata
    """
    subjects = db.query(Subject).filter(Subject.is_active == True).all()
    
    result = []
    for subject in subjects:
        question_count = db.query(Question).filter(
            Question.subject_id == subject.id,
            Question.is_active == True
        ).count()
        
        result.append({
            "id": subject.id,
            "name": subject.name,
            "description": subject.description,
            "icon": subject.icon,
            "color": subject.color,
            "question_count": question_count,
            "is_active": subject.is_active
        })
    
    return result
