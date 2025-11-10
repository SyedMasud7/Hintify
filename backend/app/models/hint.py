"""Hint model"""

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Hint(Base):
    """
    Hint model representing a helpful clue for a question.
    
    Each question has exactly one hint. Hints can be pre-written or AI-generated.
    Pre-submit hints should guide without revealing the answer.
    """
    __tablename__ = "hints"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False, unique=True)
    hint_text = Column(Text, nullable=False)
    is_ai_generated = Column(Boolean, default=False)
    
    # Relationships
    question = relationship("Question", back_populates="hint")
    
    def __repr__(self):
        return f"<Hint(id={self.id}, question_id={self.question_id}, ai_generated={self.is_ai_generated})>"
