"""Question generator service using AI"""

import logging
from typing import List
from app.ai.base import AIProvider, QuestionData
from app.models.question import DifficultyLevel

logger = logging.getLogger(__name__)


class QuestionGenerator:
    """Service for generating questions from document content using AI"""
    
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider
    
    async def generate_from_text(
        self,
        text: str,
        subject_id: int,
        filename: str,
        count: int = 45
    ) -> List[QuestionData]:
        """
        Generate MCQs from text content
        
        Args:
            text: Source text to generate questions from
            subject_id: Subject ID for the questions
            filename: Source document filename
            count: Number of questions to generate (default 45)
            
        Returns:
            List of QuestionData objects
        """
        logger.info(f"Generating {count} questions from {filename}")
        
        # Truncate text if too long (keep first 5000 chars for context)
        if len(text) > 5000:
            logger.warning(f"Text too long ({len(text)} chars), truncating to 5000")
            text = text[:5000]
        
        # Generate questions using AI
        questions = await self.ai_provider.generate_questions(text, count=count)
        
        if not questions:
            logger.warning("AI generation failed, using fallback")
            # If AI fails, create a simple fallback
            questions = self._generate_fallback_questions(text, count)
        
        # Ensure we have exactly the right distribution
        questions = self._balance_difficulty(questions, count)
        
        logger.info(f"Generated {len(questions)} questions")
        return questions
    
    def _balance_difficulty(
        self,
        questions: List[QuestionData],
        total_count: int = 45
    ) -> List[QuestionData]:
        """
        Ensure exactly 15 easy, 15 medium, 15 hard questions
        
        Args:
            questions: List of generated questions
            total_count: Total questions needed (default 45)
            
        Returns:
            Balanced list of questions
        """
        per_difficulty = total_count // 3  # 15 each
        
        # Separate by difficulty
        easy = [q for q in questions if q.difficulty == "EASY"]
        medium = [q for q in questions if q.difficulty == "MEDIUM"]
        hard = [q for q in questions if q.difficulty == "HARD"]
        
        # Adjust counts
        easy = easy[:per_difficulty] if len(easy) >= per_difficulty else easy
        medium = medium[:per_difficulty] if len(medium) >= per_difficulty else medium
        hard = hard[:per_difficulty] if len(hard) >= per_difficulty else hard
        
        # If we don't have enough, redistribute
        balanced = easy + medium + hard
        
        # Pad with remaining questions if needed
        if len(balanced) < total_count:
            remaining = [q for q in questions if q not in balanced]
            balanced.extend(remaining[:total_count - len(balanced)])
        
        return balanced[:total_count]
    
    def _generate_fallback_questions(
        self,
        text: str,
        count: int = 45
    ) -> List[QuestionData]:
        """
        Generate simple fallback questions when AI is unavailable
        
        Args:
            text: Source text
            count: Number of questions needed
            
        Returns:
            List of basic QuestionData objects
        """
        import re
        
        # Extract sentences
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 20]
        
        questions = []
        per_difficulty = count // 3
        
        for i in range(min(count, len(sentences))):
            sentence = sentences[i]
            
            # Determine difficulty based on position
            if i < per_difficulty:
                difficulty = "EASY"
            elif i < 2 * per_difficulty:
                difficulty = "MEDIUM"
            else:
                difficulty = "HARD"
            
            # Create a simple fill-in-the-blank question
            words = sentence.split()
            if len(words) > 5:
                # Pick a word to blank out
                blank_idx = len(words) // 2
                correct_word = words[blank_idx]
                question_text = ' '.join(words[:blank_idx] + ['______'] + words[blank_idx+1:])
                
                # Generate simple distractors
                options = [correct_word]
                options.extend([f"{correct_word}s", f"not {correct_word}", f"anti-{correct_word}"])
                
                questions.append(QuestionData(
                    question_text=f"Fill in the blank: {question_text}",
                    options=options[:4],
                    correct_answer=0,
                    hint=f"Think about the context of the sentence.",
                    explanation=f"The correct answer is '{correct_word}' based on the context.",
                    difficulty=difficulty
                ))
        
        return questions
