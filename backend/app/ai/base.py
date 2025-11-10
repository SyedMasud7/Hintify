"""Base AI provider interface"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pydantic import BaseModel


class QuestionData(BaseModel):
    """Data structure for generated questions"""
    question_text: str
    options: List[str]  # 4 options (A-D)
    correct_answer: int  # Index 0-3
    hint: str
    explanation: str
    difficulty: str  # EASY, MEDIUM, HARD


class AIProvider(ABC):
    """
    Abstract base class for AI providers.
    
    All AI providers (OpenAI, DeepSeek, local, fallback) must implement this interface.
    """
    
    @abstractmethod
    async def generate_hint(
        self,
        question: str,
        options: List[str],
        difficulty: str,
        pre_submit: bool = True
    ) -> str:
        """
        Generate a hint for a question.
        
        Args:
            question: The question text
            options: List of 4 answer options
            difficulty: EASY, MEDIUM, or HARD
            pre_submit: If True, don't reveal answer; if False, can be more explicit
            
        Returns:
            Hint text that guides without revealing (if pre_submit=True)
        """
        pass
    
    @abstractmethod
    async def generate_explanation(
        self,
        question: str,
        correct_answer: str,
        user_answer: str = None
    ) -> str:
        """
        Generate a detailed explanation for a question.
        
        Args:
            question: The question text
            correct_answer: The correct answer text
            user_answer: The user's selected answer (optional)
            
        Returns:
            Detailed explanation of why the answer is correct
        """
        pass
    
    @abstractmethod
    async def generate_questions(
        self,
        text: str,
        count: int = 45
    ) -> List[QuestionData]:
        """
        Generate multiple-choice questions from text content.
        
        Args:
            text: Source text to generate questions from
            count: Number of questions to generate (default 45)
            
        Returns:
            List of QuestionData objects
        """
        pass
    
    @abstractmethod
    async def calibrate_difficulty(
        self,
        question: str,
        options: List[str]
    ) -> str:
        """
        Determine the difficulty level of a question.
        
        Args:
            question: The question text
            options: List of answer options
            
        Returns:
            Difficulty level: EASY, MEDIUM, or HARD
        """
        pass
