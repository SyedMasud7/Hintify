"""Database configuration and session management"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read database URL from environment or use SQLite default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hintify.db")

# Create engine with appropriate configuration
connect_args = {}
if "sqlite" in DATABASE_URL:
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,  # Verify connections before using
    echo=False  # Set to True for SQL query logging
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base for models
Base = declarative_base()


def get_db():
    """
    Dependency function for FastAPI routes to get database session.
    
    Usage:
        @router.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database by creating all tables"""
    # Import all models to register them
    from app.models.subject import Subject
    from app.models.question import Question
    from app.models.choice import Choice
    from app.models.hint import Hint
    from app.models.test_session import TestSession
    from app.models.attempt import Attempt
    Base.metadata.create_all(bind=engine)
