#!/bin/bash

echo "🎓 Hintify Professional - Quick Start"
echo "======================================"

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "Installing dependencies..."
    .venv/bin/pip install -q --upgrade pip
    .venv/bin/pip install -q -r backend/requirements.txt
    echo "✓ Dependencies installed"
fi

# Check if database exists
if [ ! -f "backend/hintify.db" ]; then
    echo "Seeding database with 180 questions..."
    .venv/bin/python backend/app/scripts/seed_database.py
    echo "✓ Database seeded"
fi

echo ""
echo "Starting server..."
echo "Frontend: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop"
echo ""

cd backend && ../.venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
