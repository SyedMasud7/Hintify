"""Attempt model"""

from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database import Base


class Attempt(Base):
    """
    Attempt model representing a user's answer to a specific question in a test.
    
    Tracks which answer was selected, whether it was correct, time taken,
    and whether a hint was used.
    """
    __tablename__ = "attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    test_session_id = Column(Integer, ForeignKey("test_sessions.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    selected_answer = Column(Integer, nullable=True)  # 0-3 for A-D, NULL if skipped
    is_correct = Column(Boolean, nullable=True)
    time_taken = Column(Integer, nullable=True)  # Time in seconds
    hint_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    test_session = relationship("TestSession", back_populates="attempts")
    question = relationship("Question")
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_attempts_session', 'test_session_id'),
        Index('idx_attempts_question', 'question_id'),
    )
    
    def __repr__(self):
        return f"<Attempt(id={self.id}, question_id={self.question_id}, correct={self.is_correct})>"
