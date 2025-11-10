.PHONY: install dev format lint test seed reset-db run build-frontend help

help:
	@echo "Hintify Professional - Makefile Commands"
	@echo "========================================"
	@echo "install        - Create venv and install dependencies"
	@echo "dev            - Run development server with auto-reload"
	@echo "format         - Format code with black and isort"
	@echo "lint           - Lint code with ruff"
	@echo "test           - Run tests with coverage"
	@echo "seed           - Seed database with 180 questions"
	@echo "reset-db       - Reset database and reseed"
	@echo "run            - Run production server"
	@echo "build-frontend - No build needed (vanilla JS)"

install:
	@echo "Creating virtual environment..."
	python3 -m venv .venv
	@echo "Installing dependencies..."
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r backend/requirements.txt
	@echo "✓ Installation complete!"

dev:
	@echo "Starting development server..."
	. .venv/bin/activate && cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

format:
	@echo "Formatting code..."
	. .venv/bin/activate && black backend/app backend/tests
	. .venv/bin/activate && isort backend/app backend/tests
	@echo "✓ Code formatted!"

lint:
	@echo "Linting code..."
	. .venv/bin/activate && ruff check backend/app backend/tests
	@echo "✓ Linting complete!"

test:
	@echo "Running tests..."
	. .venv/bin/activate && cd backend && pytest tests/ -v --cov=app --cov-report=html --cov-report=term
	@echo "✓ Tests complete! Coverage report in backend/htmlcov/index.html"

seed:
	@echo "Seeding database..."
	. .venv/bin/activate && cd backend && python -m app.scripts.seed_database
	@echo "✓ Database seeded with 180 questions!"

reset-db:
	@echo "Resetting database..."
	rm -f backend/hintify.db
	. .venv/bin/activate && cd backend && alembic upgrade head
	$(MAKE) seed
	@echo "✓ Database reset complete!"

run:
	@echo "Starting production server..."
	. .venv/bin/activate && cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000

build-frontend:
	@echo "Frontend is vanilla JS - no build needed!"
	@echo "✓ Frontend ready to serve!"
