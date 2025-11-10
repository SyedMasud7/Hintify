"""Question model"""

from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.database import Base


class DifficultyLevel(str, Enum):
    """Question difficulty levels"""
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Question(Base):
    """
    Question model representing a multiple-choice question.
    
    Each question has 4 choices (A-D), one correct answer, a hint, and an explanation.
    Questions can be curated (source_document=NULL) or generated from uploads.
    """
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    difficulty = Column(SQLEnum(DifficultyLevel), nullable=False)
    explanation = Column(Text)  # Explanation shown after answering
    source_document = Column(String(255), nullable=True)  # NULL for curated, filename for uploaded
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    subject = relationship("Subject", back_populates="questions")
    choices = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete-orphan",
        order_by="Choice.letter"
    )
    hint = relationship(
        "Hint",
        back_populates="question",
        uselist=False,  # One-to-one relationship
        cascade="all, delete-orphan"
    )
    # Lazy relationship - Attempt model defined elsewhere
    # attempts = relationship("Attempt", back_populates="question")
    
    def __repr__(self):
        return f"<Question(id={self.id}, difficulty='{self.difficulty}', subject_id={self.subject_id})>"
