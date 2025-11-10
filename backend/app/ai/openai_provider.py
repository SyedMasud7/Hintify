"""OpenAI AI provider"""

import os
from typing import List
from tenacity import retry, stop_after_attempt, wait_exponential
from app.ai.base import AIProvider, QuestionData


class OpenAIProvider(AIProvider):
    """
    OpenAI-based AI provider using GPT models.
    
    Requires: AI_API_KEY environment variable
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        try:
            from openai import AsyncOpenAI
            self.client = AsyncOpenAI(api_key=api_key)
        except ImportError:
            raise ImportError("openai package not installed. Run: pip install openai")
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def generate_hint(
        self,
        question: str,
        options: List[str],
        difficulty: str,
        pre_submit: bool = True
    ) -> str:
        """Generate AI hint using OpenAI"""
        if pre_submit:
            prompt = f"""Generate a helpful hint for this multiple-choice question WITHOUT revealing the answer.
The hint should guide the student's thinking without being too obvious.

Question: {question}
Options: {', '.join(options)}
Difficulty: {difficulty}

Provide only the hint text, no additional commentary."""
        else:
            prompt = f"""Generate a detailed explanation for this question.

Question: {question}
Options: {', '.join(options)}

Provide a clear, educational explanation."""
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7,
                timeout=30.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            # Fallback to simple hint
            return f"Consider the key concepts in this {difficulty.lower()} question."
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def generate_explanation(
        self,
        question: str,
        correct_answer: str,
        user_answer: str = None
    ) -> str:
        """Generate AI explanation"""
        prompt = f"""Explain why this is the correct answer to the question.

Question: {question}
Correct Answer: {correct_answer}
{f"User's Answer: {user_answer}" if user_answer else ""}

Provide a clear, concise explanation suitable for learning."""
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7,
                timeout=30.0
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return f"The correct answer is '{correct_answer}'. Review the relevant concepts for better understanding."
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def generate_questions(
        self,
        text: str,
        count: int = 45
    ) -> List[QuestionData]:
        """Generate questions from text using AI"""
        prompt = f"""Generate {count} multiple-choice questions from the following text.
Each question should have:
- Clear question text
- 4 options (A-D)
- One correct answer
- A helpful hint
- A brief explanation

Distribute difficulty: {count//3} EASY, {count//3} MEDIUM, {count//3} HARD

Text:
{text[:3000]}

Return as JSON array with format:
[{{"question_text": "...", "options": ["A", "B", "C", "D"], "correct_answer": 0, "hint": "...", "explanation": "...", "difficulty": "EASY"}}]"""
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4000,
                temperature=0.8,
                timeout=60.0
            )
            
            import json
            content = response.choices[0].message.content.strip()
            # Extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            questions_data = json.loads(content)
            return [QuestionData(**q) for q in questions_data[:count]]
        except Exception as e:
            # Return empty list on failure
            return []
    
    async def calibrate_difficulty(
        self,
        question: str,
        options: List[str]
    ) -> str:
        """Determine difficulty using AI"""
        prompt = f"""Rate the difficulty of this question as EASY, MEDIUM, or HARD.

Question: {question}
Options: {', '.join(options)}

Respond with only one word: EASY, MEDIUM, or HARD"""
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10,
                temperature=0.3,
                timeout=15.0
            )
            difficulty = response.choices[0].message.content.strip().upper()
            if difficulty in ["EASY", "MEDIUM", "HARD"]:
                return difficulty
        except Exception:
            pass
        
        return "MEDIUM"  # Default
