"""Seed database with 180 curated questions"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.database import SessionLocal, engine, Base
from app.models.subject import Subject
from app.models.question import Question, DifficultyLevel
from app.models.choice import Choice
from app.models.hint import Hint
from app.models.test_session import TestSession
from app.models.attempt import Attempt

def seed_subjects(db):
    """Create 4 subjects"""
    subjects_data = [
        {"name": "Technology", "description": "Computer science and programming", "icon": "💻", "color": "#3B82F6"},
        {"name": "Science", "description": "Physics, chemistry, and biology", "icon": "🔬", "color": "#10B981"},
        {"name": "Geography", "description": "World geography and landmarks", "icon": "🌍", "color": "#F59E0B"},
        {"name": "General Knowledge", "description": "History and culture", "icon": "📚", "color": "#EF4444"}
    ]
    
    subjects = []
    for data in subjects_data:
        subject = Subject(**data)
        db.add(subject)
        subjects.append(subject)
    
    db.commit()
    for subject in subjects:
        db.refresh(subject)
    
    return subjects

def add_question(db, subject_id, difficulty, question_text, choices_data, hint_text, explanation):
    """Helper to add a question"""
    question = Question(
        subject_id=subject_id,
        question_text=question_text,
        difficulty=difficulty,
        explanation=explanation
    )
    db.add(question)
    db.flush()
    
    for letter, (text, is_correct) in choices_data.items():
        choice = Choice(
            question_id=question.id,
            choice_text=text,
            is_correct=is_correct,
            letter=letter
        )
        db.add(choice)
    
    hint = Hint(question_id=question.id, hint_text=hint_text)
    db.add(hint)


from app.scripts.questions_data import (
    TECHNOLOGY_EASY, TECHNOLOGY_MEDIUM, TECHNOLOGY_HARD,
    SCIENCE_EASY, SCIENCE_MEDIUM, SCIENCE_HARD,
    GEOGRAPHY_EASY, GEOGRAPHY_MEDIUM, GEOGRAPHY_HARD,
    GENERAL_EASY, GENERAL_MEDIUM, GENERAL_HARD
)

def seed_all_questions(db, subjects):
    """Seed all 180 questions"""
    tech_id = subjects[0].id
    science_id = subjects[1].id
    geo_id = subjects[2].id
    gk_id = subjects[3].id
    
    print("Seeding Technology questions...")
    for q_text, choices, hint, explanation in TECHNOLOGY_EASY:
        add_question(db, tech_id, DifficultyLevel.EASY, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in TECHNOLOGY_MEDIUM:
        add_question(db, tech_id, DifficultyLevel.MEDIUM, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in TECHNOLOGY_HARD:
        add_question(db, tech_id, DifficultyLevel.HARD, q_text, choices, hint, explanation)
    
    print("Seeding Science questions...")
    for q_text, choices, hint, explanation in SCIENCE_EASY:
        add_question(db, science_id, DifficultyLevel.EASY, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in SCIENCE_MEDIUM:
        add_question(db, science_id, DifficultyLevel.MEDIUM, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in SCIENCE_HARD:
        add_question(db, science_id, DifficultyLevel.HARD, q_text, choices, hint, explanation)
    
    print("Seeding Geography questions...")
    for q_text, choices, hint, explanation in GEOGRAPHY_EASY:
        add_question(db, geo_id, DifficultyLevel.EASY, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in GEOGRAPHY_MEDIUM:
        add_question(db, geo_id, DifficultyLevel.MEDIUM, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in GEOGRAPHY_HARD:
        add_question(db, geo_id, DifficultyLevel.HARD, q_text, choices, hint, explanation)
    
    print("Seeding General Knowledge questions...")
    for q_text, choices, hint, explanation in GENERAL_EASY:
        add_question(db, gk_id, DifficultyLevel.EASY, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in GENERAL_MEDIUM:
        add_question(db, gk_id, DifficultyLevel.MEDIUM, q_text, choices, hint, explanation)
    for q_text, choices, hint, explanation in GENERAL_HARD:
        add_question(db, gk_id, DifficultyLevel.HARD, q_text, choices, hint, explanation)

def main():
    """Main seeding function"""
    print("=" * 60)
    print("Hintify Professional - Database Seeding")
    print("=" * 60)
    
    # Create tables
    print("\nCreating database tables...")
    print(f"Database URL: {engine.url}")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created")
    print(f"Tables: {list(Base.metadata.tables.keys())}")
    
    # Create session
    db = SessionLocal()
    
    try:
        # Check if already seeded
        print("\nChecking for existing data...")
        existing_subjects = db.query(Subject).count()
        if existing_subjects > 0:
            print("\n⚠ Database already contains data!")
            response = input("Do you want to reset and reseed? (yes/no): ")
            if response.lower() != 'yes':
                print("Seeding cancelled.")
                return
            
            # Clear existing data
            print("\nClearing existing data...")
            db.query(Hint).delete()
            db.query(Choice).delete()
            db.query(Question).delete()
            db.query(Subject).delete()
            db.commit()
            print("✓ Data cleared")
        
        # Seed subjects
        print("\nSeeding subjects...")
        subjects = seed_subjects(db)
        print(f"✓ Created {len(subjects)} subjects")
        
        # Seed questions
        print("\nSeeding questions...")
        seed_all_questions(db, subjects)
        db.commit()
        
        # Verify
        total_questions = db.query(Question).count()
        total_choices = db.query(Choice).count()
        total_hints = db.query(Hint).count()
        
        print("\n" + "=" * 60)
        print("Seeding Complete!")
        print("=" * 60)
        print(f"✓ Subjects: {len(subjects)}")
        print(f"✓ Questions: {total_questions}")
        print(f"✓ Choices: {total_choices}")
        print(f"✓ Hints: {total_hints}")
        print("\nBreakdown by subject:")
        for subject in subjects:
            count = db.query(Question).filter(Question.subject_id == subject.id).count()
            print(f"  {subject.icon} {subject.name}: {count} questions")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()
