"""Subject model"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Subject(Base):
    """
    Subject model representing a category of questions.
    
    Examples: Technology, Science, Geography, General Knowledge
    """
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    icon = Column(String(10))  # Emoji or icon class (e.g., "💻", "fa-laptop")
    color = Column(String(7))  # Hex color code (e.g., "#3B82F6")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    questions = relationship(
        "Question",
        back_populates="subject",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}')>"
