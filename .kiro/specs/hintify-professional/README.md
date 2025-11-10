# Hintify Professional - Spec Summary

## Overview

This spec defines a complete AI-powered learning platform with intelligent hints for multiple-choice questions. The system supports multiple AI providers (OpenAI, DeepSeek, local models) with graceful fallback to rule-based hints.

## Key Features

- **AI Provider Integration**: Provider-agnostic layer supporting OpenAI, DeepSeek, local models, with fallback
- **180 Curated Questions**: 4 subjects × 45 questions each (15 easy, 15 medium, 15 hard)
- **Document Upload**: Auto-generate 45 MCQs from PDF/DOCX/PPTX files using AI
- **Interactive Testing**: Per-question submit, immediate feedback, hints, timer, keyboard shortcuts
- **Advanced Analytics**: Chart.js visualizations (donut, bar, line, heatmap) with PNG/PDF export
- **Professional UI**: Glassmorphism design, Particles.js background, dark/light themes
- **PWA Support**: Offline capability, installable, responsive design
- **No Authentication**: Everything accessible without login

## Technology Stack

**Backend:**
- FastAPI + SQLAlchemy + Alembic
- SQLite (default) with PostgreSQL/MySQL support
- OpenAI/LiteLLM for AI providers
- pdfminer.six, python-docx, python-pptx for document parsing

**Frontend:**
- Vanilla JavaScript (no framework)
- Chart.js for analytics
- Particles.js for animated background
- Pure CSS with glassmorphism

## Project Structure

```
hintify-professional/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/          # SQLAlchemy models
│   │   ├── routers/         # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── ai/              # AI provider layer
│   │   └── scripts/         # Seed data
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html           # Single-page app
│   ├── manifest.json        # PWA manifest
│   ├── service-worker.js    # Offline support
│   └── assets/              # Icons, images
├── Makefile
└── README.md
```

## Getting Started

### 1. Review the Spec Files

- **requirements.md** - 15 requirements with EARS-compliant acceptance criteria
- **design.md** - Complete technical architecture and component design
- **tasks.md** - 19 major tasks with 100+ actionable subtasks

### 2. Start Implementation

Open `tasks.md` and click "Start task" next to any task to begin implementation. Recommended order:

1. **Task 1**: Set up project structure and dependencies
2. **Task 2**: Implement database foundation
3. **Task 3**: Implement AI provider layer
4. **Task 4**: Create seed data with 180 questions
5. **Task 5**: Implement document processing
6. **Task 6**: Implement backend API routers
7. **Task 7**: Create main FastAPI application
8. **Task 8-9**: Build frontend HTML/CSS
9. **Task 10-16**: Implement frontend JavaScript
10. **Task 17**: Add PWA functionality
11. **Task 18**: Testing and quality assurance
12. **Task 19**: Documentation and deployment

### 3. Environment Setup

Create `.env` file based on `.env.example`:

```bash
# Database
DATABASE_URL=sqlite:///./hintify.db

# AI Provider (optional - uses fallback if not provided)
AI_PROVIDER=openai
AI_API_KEY=your_api_key_here
AI_MODEL=gpt-3.5-turbo

# Server
HOST=0.0.0.0
PORT=8000
```

### 4. Run the Application

```bash
# Install dependencies
make install

# Seed database with 180 questions
make seed

# Start development server
make dev

# Access at http://localhost:8000
# API docs at http://localhost:8000/docs
```

## API Endpoints

- `GET /api/subjects` - List all subjects
- `GET /api/questions` - Get questions with filters
- `POST /api/tests/start` - Start test session
- `POST /api/attempts/submit` - Submit answer
- `GET /api/tests/{id}/summary` - Get test results
- `POST /api/uploads` - Upload document and generate questions
- `GET /api/reports/overview` - Get analytics data
- `GET /api/admin/export` - Export questions
- `POST /api/admin/import` - Import questions

## Acceptance Criteria Checklist

- [ ] App starts with `make dev` and serves frontend + API
- [ ] 4 subjects with 3 difficulties each, unique questions
- [ ] Per-question submit with immediate verdict and optional hint
- [ ] File upload generates ≥45 MCQs (15 easy/15 medium/15 hard)
- [ ] Analytics renders multiple charts and exports images
- [ ] Dark/Light toggle persists; live background runs smoothly
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Keyboard shortcuts work (N, P, S, H, D)
- [ ] Seed provides ≥180 MCQs (45 × 4 subjects) with hints
- [ ] If no AI key, fallback hinting works without errors
- [ ] Rate limits applied (30/min hints, 5/hour uploads)
- [ ] Input validated, file uploads sanitized
- [ ] PWA installable with offline support

## Notes

- All tasks are required (comprehensive approach chosen)
- Testing tasks (Task 18) are included for production quality
- No authentication system - everything is publicly accessible
- AI provider is optional - system works with fallback if no API key provided
- Database is SQLite by default but can be swapped to PostgreSQL/MySQL

## Support

For questions or issues during implementation:
1. Review the design.md for technical details
2. Check requirements.md for acceptance criteria
3. Refer to tasks.md for step-by-step implementation guidance
