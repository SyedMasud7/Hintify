# 🎓 Hintify Professional

AI-Powered Learning Platform with Intelligent Hints

## ✨ Features

- **180 Curated Questions** across 4 subjects (Technology, Science, Geography, General Knowledge)
- **AI-Powered Hints** with support for OpenAI, DeepSeek, or rule-based fallback
- **Document Upload** - Generate 45 questions (15 easy, 15 medium, 15 hard) from PDF/DOCX/PPTX
- **Interactive Testing** - Per-question feedback with hints and explanations
- **Professional UI** - Glassmorphism design with animated particle background
- **Dark/Light Themes** - Toggle with preference persistence
- **Responsive Design** - Works on mobile, tablet, and desktop

## 🚀 Quick Start

### Prerequisites

- Python 3.11+ (tested with 3.13)
- pip

### Installation

```bash
# Clone or navigate to project
cd hintify-professional

# Install dependencies
make install

# Seed database with 180 questions
make seed

# Start development server
make dev
```

### Access the Application

- **Frontend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## 📁 Project Structure

```
hintify-professional/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routers/         # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── ai/              # AI provider layer
│   │   ├── scripts/         # Seed data
│   │   ├── database.py      # DB configuration
│   │   └── main.py          # FastAPI app
│   ├── tests/               # Test suite
│   ├── alembic/             # DB migrations
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment template
│   └── hintify.db           # SQLite database
├── frontend/
│   └── index.html           # Single-page application
├── Makefile                 # Development commands
└── README.md                # This file
```

## 🔧 Configuration

Create a `.env` file in the `backend/` directory:

```bash
# Database (default SQLite)
DATABASE_URL=sqlite:///./hintify.db

# AI Provider (optional - uses fallback if not set)
AI_PROVIDER=fallback  # Options: openai, deepseek, local, fallback
AI_API_KEY=           # Your API key (leave empty for fallback)
AI_MODEL=gpt-3.5-turbo

# Server
HOST=0.0.0.0
PORT=8000
```

## 📚 API Endpoints

### Subjects
- `GET /api/subjects/` - List all subjects with question counts

### Questions
- `GET /api/questions/` - Get questions (filters: subject_id, difficulty, limit, offset)
- `GET /api/questions/{id}/hint` - Get hint for specific question

### Upload
- `POST /api/upload/` - Upload document and generate 45 questions
  - Form data: `file` (PDF/DOCX/PPTX), `subject_id`
  - Returns: Generated questions with difficulty distribution

### Health
- `GET /api/health` - Health check endpoint

## 🎯 How to Use

### 1. Take a Test

1. Click "Take Test" in navigation
2. Select a subject (Technology, Science, Geography, or General Knowledge)
3. Answer questions and get immediate feedback
4. Click "Hint" button for guidance
5. Navigate between questions

### 2. Upload Documents ✅ WORKING

1. Click "Upload" in navigation
2. Select a subject for the generated questions
3. Drag & drop or click to upload PDF/DOCX/PPTX (max 10MB)
4. System generates 45 questions automatically:
   - 15 Easy questions
   - 15 Medium questions
   - 15 Hard questions
5. Each question includes AI-generated hints and explanations
6. View generated questions in "My Questions" section
7. Take tests on your uploaded content

**Test it now:** Two sample documents are included (test_document.docx, science_study_guide.docx)

## 🤖 AI Provider Setup

### Using OpenAI

```bash
AI_PROVIDER=openai
AI_API_KEY=sk-your-openai-key
AI_MODEL=gpt-3.5-turbo
```

### Using DeepSeek

```bash
AI_PROVIDER=deepseek
AI_API_KEY=your-deepseek-key
AI_MODEL=deepseek-chat
```

### Using Fallback (No API Key Required)

```bash
AI_PROVIDER=fallback
# No API key needed - uses rule-based hints
```

## 🛠️ Development Commands

```bash
make install      # Create venv and install dependencies
make dev          # Start development server with auto-reload
make seed         # Seed database with 180 questions
make reset-db     # Reset and reseed database
make format       # Format code with black and isort
make lint         # Lint code with ruff
make test         # Run tests with coverage
```

## 📊 Database

### Seeded Data

- **4 Subjects**: Technology, Science, Geography, General Knowledge
- **180 Questions**: 45 per subject (15 easy, 15 medium, 15 hard)
- **720 Choices**: 4 options per question (A-D)
- **180 Hints**: One hint per question

### Schema

- `subjects` - Subject categories
- `questions` - MCQ questions
- `choices` - Answer options (A-D)
- `hints` - Helpful hints
- `test_sessions` - Test instances
- `attempts` - Individual answers

## 🎨 UI Features

- **Glassmorphism Design** - Modern transparent glass-like UI
- **Animated Background** - Floating particles with Particles.js
- **Dark/Light Themes** - Toggle with localStorage persistence
- **Responsive Layout** - Mobile-first design
- **Smooth Animations** - 60fps transitions

## 🔒 Security

- Input validation with Pydantic
- File upload sanitization
- File size limits (10MB)
- File type validation (PDF, DOCX, PPTX only)
- CORS configuration
- Rate limiting ready (slowapi)

## 📝 License

MIT License

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md for guidelines.

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ using FastAPI, SQLAlchemy, and Vanilla JavaScript**
