"""Main FastAPI application"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.routers import subjects, questions, upload
from app.database import Base, engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Hintify Professional API",
    description="AI-Powered Learning Platform with Intelligent Hints",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)
logger.info("Database tables created/verified")

# Register routers
app.include_router(subjects.router)
app.include_router(questions.router)
app.include_router(upload.router)

logger.info("API routers registered")

# Mount static files (frontend)
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")
    logger.info(f"Static files mounted from {frontend_path}")


@app.get("/")
async def root():
    """Root endpoint - serve frontend or API info"""
    frontend_index = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_index):
        return FileResponse(frontend_index)
    
    return {
        "message": "Hintify Professional API",
        "version": "2.0.0",
        "docs": "/docs",
        "endpoints": {
            "subjects": "/api/subjects",
            "questions": "/api/questions",
            "upload": "/api/upload"
        }
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "2.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
