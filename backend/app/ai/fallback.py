"""Fallback rule-based AI provider"""

import random
import re
from typing import List
from app.ai.base import AIProvider, QuestionData


class FallbackProvider(AIProvider):
    """
    Rule-based fallback provider that works without external AI APIs.
    
    Uses keyword extraction, template-based hints, and simple heuristics.
    """
    
    async def generate_hint(
        self,
        question: str,
        options: List[str],
        difficulty: str,
        pre_submit: bool = True
    ) -> str:
        """Generate a rule-based hint"""
        keywords = self._extract_keywords(question)
        
        if pre_submit:
            # Pre-submit: eliminate one wrong answer
            hints = [
                f"Think about {keywords[0] if keywords else 'the key concept'} in this question.",
                f"Consider what you know about {keywords[0] if keywords else 'this topic'}.",
                f"Focus on the relationship between {keywords[0] if keywords else 'the concepts'} and {keywords[1] if len(keywords) > 1 else 'the answer'}.",
                f"Remember the definition of {keywords[0] if keywords else 'the main term'}.",
            ]
            return random.choice(hints)
        else:
            # Post-submit: more detailed
            return f"The correct answer relates to {keywords[0] if keywords else 'the main concept'}. Review the fundamentals of this topic for better understanding."
    
    async def generate_explanation(
        self,
        question: str,
        correct_answer: str,
        user_answer: str = None
    ) -> str:
        """Generate a template-based explanation"""
        keywords = self._extract_keywords(question)
        
        if user_answer and user_answer != correct_answer:
            return f"The correct answer is '{correct_answer}'. This is because it directly addresses {keywords[0] if keywords else 'the question'}. Review the key concepts to strengthen your understanding."
        else:
            return f"Correct! '{correct_answer}' is the right answer. This demonstrates your understanding of {keywords[0] if keywords else 'the topic'}."
    
    async def generate_questions(
        self,
        text: str,
        count: int = 45
    ) -> List[QuestionData]:
        """
        Generate simple questions from text.
        
        Note: This is a basic implementation. For production use with uploads,
        an AI provider should be configured.
        """
        # Extract sentences
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 20]
        
        if not sentences:
            # If no sentences, create generic questions
            return self._generate_generic_questions(count)
        
        questions = []
        per_difficulty = count // 3  # 15 each for easy, medium, hard
        
        # Generate questions cycling through sentences
        for i in range(count):
            sentence = sentences[i % len(sentences)]
            keywords = self._extract_keywords(sentence)
            
            if not keywords:
                # If no keywords, use the whole sentence
                keywords = sentence.split()[:3]
            
            # Pick a keyword based on position for variety
            keyword_idx = i % len(keywords) if keywords else 0
            keyword = keywords[keyword_idx] if keywords else "concept"
            
            # Create a simple fill-in-the-blank style question
            question_text = sentence.replace(keyword, "______", 1)
            
            # Generate distractors
            options = [keyword]
            options.extend(self._generate_distractors(keyword, 3))
            random.shuffle(options)
            
            correct_idx = options.index(keyword)
            
            # Determine difficulty based on position
            if i < per_difficulty:
                difficulty = "EASY"
            elif i < 2 * per_difficulty:
                difficulty = "MEDIUM"
            else:
                difficulty = "HARD"
            
            questions.append(QuestionData(
                question_text=f"Fill in the blank: {question_text}",
                options=options,
                correct_answer=correct_idx,
                hint=f"Think about the context of {keywords[1] if len(keywords) > 1 else 'the sentence'}.",
                explanation=f"The correct answer is '{keyword}' based on the context provided.",
                difficulty=difficulty
            ))
        
        return questions[:count]
    
    async def calibrate_difficulty(
        self,
        question: str,
        options: List[str]
    ) -> str:
        """Estimate difficulty based on question length and complexity"""
        # Simple heuristic: longer questions and options = harder
        avg_option_length = sum(len(opt) for opt in options) / len(options)
        question_length = len(question)
        
        if question_length < 50 and avg_option_length < 20:
            return "EASY"
        elif question_length < 100 and avg_option_length < 40:
            return "MEDIUM"
        else:
            return "HARD"
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords from text"""
        # Remove common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
                     'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                     'would', 'should', 'could', 'may', 'might', 'must', 'can', 'this',
                     'that', 'these', 'those', 'what', 'which', 'who', 'when', 'where',
                     'why', 'how'}
        
        # Extract words
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        
        # Filter and return
        keywords = [w for w in words if w not in stop_words]
        return keywords[:5]  # Return top 5
    
    def _generate_distractors(self, correct: str, count: int) -> List[str]:
        """Generate plausible but incorrect options"""
        # Simple distractor generation
        distractors = []
        
        # Add variations
        if correct.endswith('s'):
            distractors.append(correct[:-1])
        else:
            distractors.append(correct + 's')
        
        # Add prefix/suffix variations
        prefixes = ['un', 'non', 'pre', 'post', 'anti', 'pro']
        suffixes = ['ing', 'ed', 'er', 'est', 'ly', 'tion']
        
        for prefix in prefixes:
            if len(distractors) < count:
                distractors.append(prefix + correct)
        
        for suffix in suffixes:
            if len(distractors) < count:
                distractors.append(correct + suffix)
        
        # Pad with generic options if needed
        generic = ['None of the above', 'All of the above', 'Cannot be determined', 'Insufficient information']
        distractors.extend(generic)
        
        return distractors[:count]
    
    def _generate_generic_questions(self, count: int) -> List[QuestionData]:
        """Generate generic questions when text extraction fails"""
        questions = []
        per_difficulty = count // 3
        
        templates = [
            ("What is the main topic of this document?", ["Technology", "Science", "History", "Mathematics"]),
            ("Which concept is most important?", ["Primary concept", "Secondary concept", "Tertiary concept", "None"]),
            ("What is the key takeaway?", ["Main idea", "Supporting detail", "Example", "Conclusion"]),
        ]
        
        for i in range(count):
            template_idx = i % len(templates)
            question_text, options = templates[template_idx]
            
            if i < per_difficulty:
                difficulty = "EASY"
            elif i < 2 * per_difficulty:
                difficulty = "MEDIUM"
            else:
                difficulty = "HARD"
            
            # Randomize correct answer position
            import random
            correct_answer = random.randint(0, 3)
            
            questions.append(QuestionData(
                question_text=question_text,
                options=options,
                correct_answer=correct_answer,
                hint="Review the document content carefully.",
                explanation=f"The correct answer is '{options[correct_answer]}'.",
                difficulty=difficulty
            ))
        
        return questions
