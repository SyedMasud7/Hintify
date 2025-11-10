"""Choice model"""

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database import Base


class Choice(Base):
    """
    Choice model representing one of four possible answers (A-D) for a question.
    
    Exactly one choice per question should have is_correct=True.
    """
    __tablename__ = "choices"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    choice_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    letter = Column(String(1), nullable=False)  # A, B, C, or D
    
    # Relationships
    question = relationship("Question", back_populates="choices")
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_question_letter', 'question_id', 'letter'),
    )
    
    def __repr__(self):
        return f"<Choice(id={self.id}, letter='{self.letter}', question_id={self.question_id})>"
