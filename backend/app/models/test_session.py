"""TestSession model"""

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.question import DifficultyLevel


class TestSession(Base):
    """
    TestSession model representing a single test instance.
    
    Tracks when a user starts a test, which subject and difficulty,
    and when they complete it. Related attempts track individual answers.
    """
    __tablename__ = "test_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    difficulty = Column(SQLEnum(DifficultyLevel), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    total_questions = Column(Integer, default=15)
    
    # Relationships
    subject = relationship("Subject")
    attempts = relationship(
        "Attempt",
        back_populates="test_session",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<TestSession(id={self.id}, subject_id={self.subject_id}, difficulty='{self.difficulty}')>"
