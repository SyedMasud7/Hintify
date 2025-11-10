# Hintify - Design Document

## Overview

Hintify is a full-stack web application built with FastAPI (backend) and vanilla JavaScript (frontend). The system uses SQLite for data storage and implements a clean separation between curated questions and user-uploaded questions. The architecture prioritizes simplicity, maintainability, and bug-free operation.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (Browser)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Home       │  │  Take Test   │  │   Upload     │      │
│  │   Section    │  │   Section    │  │   Section    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │ My Questions │  │  Analytics   │                        │
│  └──────────────┘  └──────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                            │ HTTP/REST API
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend (FastAPI)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Subjects    │  │  Questions   │  │   Upload     │      │
│  │   Router     │  │   Router     │  │   Router     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Database (SQLite)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   subjects   │  │  questions   │  │   choices    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│  ┌──────────────┐                                           │
│  │    hints     │                                           │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Backend:**
- FastAPI 0.104.1 - Modern Python web framework
- SQLAlchemy 2.0.23 - ORM for database operations
- Uvicorn 0.24.0 - ASGI server
- Python 3.9+ - Programming language

**Frontend:**
- Vanilla JavaScript (ES6+) - No framework dependencies
- HTML5 - Semantic markup
- CSS3 - Glassmorphism styling with animations
- Chart.js 4.4.0 - Analytics visualization

**Database:**
- SQLite 3 - Embedded database

**File Processing:**
- PyPDF2 3.0.1 - PDF text extraction
- python-docx 1.1.0 - DOCX text extraction
- python-pptx 0.6.23 - PPTX text extraction

## Components and Interfaces

### Backend Components

#### 1. Main Application (main.py)

**Purpose:** Application entry point and configuration

**Key Responsibilities:**
- Initialize FastAPI application
- Configure CORS middleware
- Mount static file directories
- Register API routers
- Serve frontend HTML

**Configuration:**
```python
app = FastAPI(
    title="Hintify API",
    description="AI-Powered Learning Platform",
    version="2.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 2. Database Module (database.py)

**Purpose:** Database connection and session management

**Key Components:**
- `engine`: SQLAlchemy engine instance
- `SessionLocal`: Session factory
- `Base`: Declarative base for models
- `get_db()`: Dependency for database sessions

**Connection String:**
```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./hintify.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

#### 3. Models (models/)

**Subject Model (subject.py):**
```python
class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    icon = Column(String)
    color = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    questions = relationship("Question", back_populates="subject")
```

**Question Model (question.py):**
```python
class DifficultyLevel(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    question_text = Column(Text, nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    correct_answer = Column(Integer, nullable=False)
    source_document = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    subject = relationship("Subject", back_populates="questions")
    choices = relationship("Choice", back_populates="question", cascade="all, delete-orphan")
    hint = relationship("Hint", back_populates="question", uselist=False, cascade="all, delete-orphan")
```

**Choice Model (choice.py):**
```python
class Choice(Base):
    __tablename__ = "choices"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    choice_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    letter = Column(String(1), nullable=False)  # A, B, C, D
    
    # Relationships
    question = relationship("Question", back_populates="choices")
```

**Hint Model (hint.py):**
```python
class Hint(Base):
    __tablename__ = "hints"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    hint_text = Column(Text, nullable=False)
    
    # Relationships
    question = relationship("Question", back_populates="hint")
```

#### 4. API Routers

**Subjects Router (routers/subjects.py):**

Endpoints:
- `GET /api/subjects/` - List all active subjects with question counts

Response Format:
```json
[
  {
    "id": 1,
    "name": "Technology",
    "description": "Computer science, programming, and digital technology concepts",
    "icon": "💻",
    "color": "#3B82F6",
    "question_count": 45,
    "is_active": true
  }
]
```

**Questions Router (routers/questions.py):**

Endpoints:
- `GET /api/questions/` - Get questions by subject and difficulty
  - Query params: `subject_id`, `difficulty`, `limit` (default 15)
- `GET /api/questions/{question_id}/hint` - Get hint for specific question
- `GET /api/questions/uploaded` - Get all uploaded questions

Response Format:
```json
[
  {
    "id": 1,
    "question_text": "What does CPU stand for?",
    "difficulty": "EASY",
    "options": [
      "Central Processing Unit",
      "Computer Personal Unit",
      "Central Program Unit",
      "Computer Processing Unit"
    ],
    "correct_answer": 0,
    "explanation": "CPU stands for Central Processing Unit...",
    "source_document": null
  }
]
```

**Upload Router (routers/upload.py):**

Endpoints:
- `POST /api/upload/` - Upload document and generate questions
  - Form data: `file` (PDF/DOCX/PPTX), `subject_id`

Response Format:
```json
{
  "message": "File uploaded and processed successfully",
  "filename": "document.pdf",
  "questions_generated": 45,
  "subject_id": 1
}
```

#### 5. Services

**Document Parser Service (services/document_parser.py):**

Purpose: Extract text from uploaded documents

Methods:
- `parse_pdf(file_path: str) -> str` - Extract text from PDF
- `parse_docx(file_path: str) -> str` - Extract text from DOCX
- `parse_pptx(file_path: str) -> str` - Extract text from PPTX

**Question Generator Service (services/question_generator.py):**

Purpose: Generate questions from document content

Methods:
- `generate_questions(text: str, subject_id: int, filename: str) -> List[QuestionData]`
  - Returns 45 questions (15 easy, 15 medium, 15 hard)
  - Each question includes text, options, correct answer, hint, explanation

### Frontend Components

#### 1. Application Structure

**File Organization:**
```
frontend/
├── index.html          # Main HTML file
├── css/
│   └── styles.css      # All styles (embedded in HTML for simplicity)
└── js/
    └── app.js          # All JavaScript (embedded in HTML for simplicity)
```

#### 2. State Management

**Global State Object:**
```javascript
const AppState = {
  // Current test state
  currentSubjectId: null,
  currentSubjectName: null,
  currentDifficulty: 'easy',
  currentQuestions: [],
  currentQuestionIndex: 0,
  userAnswers: [],
  
  // UI state
  currentSection: 'home',
  theme: 'dark',
  
  // Methods
  reset() {
    this.currentQuestions = [];
    this.currentQuestionIndex = 0;
    this.userAnswers = [];
  },
  
  setSubject(id, name) {
    this.currentSubjectId = id;
    this.currentSubjectName = name;
  },
  
  setDifficulty(difficulty) {
    this.currentDifficulty = difficulty;
  }
};
```

#### 3. Core Functions

**Navigation Functions:**
- `showSection(sectionId)` - Show/hide sections
- `loadSubjects()` - Fetch and display subjects
- `selectSubject(id, name)` - Handle subject selection
- `backToSubjects()` - Return to subject selection
- `exitTest()` - Exit current test

**Test Functions:**
- `loadQuestions(subjectId, difficulty)` - Fetch questions from API
- `displayQuestion(index)` - Render current question
- `selectOption(optionIndex)` - Handle answer selection
- `submitAnswer()` - Submit current answer and show feedback
- `nextQuestion()` - Navigate to next question
- `previousQuestion()` - Navigate to previous question
- `jumpToQuestion(index)` - Jump to specific question
- `switchDifficulty(difficulty)` - Change difficulty level

**Results Functions:**
- `submitTest()` - Calculate and display final results
- `calculateStats()` - Calculate test statistics
- `displayResults(stats)` - Render results screen

**Upload Functions:**
- `uploadFile()` - Handle file upload
- `loadUploadedQuestions()` - Fetch uploaded questions
- `displayUploadedQuestions(questions)` - Render uploaded questions

**Utility Functions:**
- `toggleTheme()` - Switch between dark/light themes
- `getHint(questionId)` - Fetch and display hint
- `showNotification(message, type)` - Display toast notification
- `updateStats()` - Update real-time statistics display

#### 4. UI Components

**Subject Card:**
```html
<div class="subject-card" onclick="selectSubject(${id}, '${name}')">
  <div class="subject-icon">${icon}</div>
  <h3>${name}</h3>
  <p>${description}</p>
  <div class="question-count">${questionCount} questions</div>
</div>
```

**Question Display:**
```html
<div class="question-container">
  <div class="question-header">
    <h3>Question ${index + 1} of ${total}</h3>
    <span class="difficulty-badge ${difficulty}">${difficulty}</span>
  </div>
  <p class="question-text">${questionText}</p>
  <div class="options">
    ${options.map((opt, i) => `
      <div class="option ${selected === i ? 'selected' : ''}" 
           onclick="selectOption(${i})">
        ${String.fromCharCode(65 + i)}. ${opt}
      </div>
    `).join('')}
  </div>
  <div class="question-actions">
    <button onclick="getHint(${questionId})">
      <i class="fas fa-lightbulb"></i> Get Hint
    </button>
  </div>
</div>
```

**Question Navigation Grid:**
```html
<div class="question-nav-grid">
  ${questions.map((q, i) => `
    <div class="q-nav-item ${getQuestionStatus(i)}" 
         onclick="jumpToQuestion(${i})">
      ${i + 1}
    </div>
  `).join('')}
</div>
```

**Statistics Display:**
```html
<div class="stats-container">
  <div class="stat-card">
    <div class="stat-value">${attempted}</div>
    <div class="stat-label">Attempted</div>
  </div>
  <div class="stat-card">
    <div class="stat-value correct">${correct}</div>
    <div class="stat-label">Correct</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">${remaining}</div>
    <div class="stat-label">Remaining</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">${accuracy}%</div>
    <div class="stat-label">Accuracy</div>
  </div>
</div>
```

## Data Models

### Database Schema

```sql
-- Subjects table
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    icon VARCHAR(10),
    color VARCHAR(7),
    is_active BOOLEAN DEFAULT 1
);

-- Questions table
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    difficulty VARCHAR(10) NOT NULL CHECK(difficulty IN ('EASY', 'MEDIUM', 'HARD')),
    correct_answer INTEGER NOT NULL CHECK(correct_answer BETWEEN 0 AND 3),
    source_document VARCHAR(255),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Choices table
CREATE TABLE choices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    choice_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT 0,
    letter VARCHAR(1) NOT NULL CHECK(letter IN ('A', 'B', 'C', 'D')),
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Hints table
CREATE TABLE hints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    hint_text TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Indexes for performance
CREATE INDEX idx_questions_subject_difficulty ON questions(subject_id, difficulty);
CREATE INDEX idx_questions_source ON questions(source_document);
CREATE INDEX idx_choices_question ON choices(question_id);
CREATE INDEX idx_hints_question ON hints(question_id);
```

### Question Data Structure

**Curated Question Example:**
```json
{
  "subject_id": 1,
  "question_text": "What does CPU stand for?",
  "difficulty": "EASY",
  "correct_answer": 0,
  "choices": [
    {"letter": "A", "text": "Central Processing Unit", "is_correct": true},
    {"letter": "B", "text": "Computer Personal Unit", "is_correct": false},
    {"letter": "C", "text": "Central Program Unit", "is_correct": false},
    {"letter": "D", "text": "Computer Processing Unit", "is_correct": false}
  ],
  "hint": "Think about the main component that processes instructions in a computer - it's the 'brain' of the system.",
  "explanation": "CPU stands for Central Processing Unit. It's the primary component that executes instructions and performs calculations in a computer."
}
```

## Error Handling

### Backend Error Handling

**Strategy:** Use FastAPI's exception handlers and HTTP status codes

**Common Error Scenarios:**
1. **Invalid file upload** - Return 400 Bad Request
2. **File too large** - Return 413 Payload Too Large
3. **Question not found** - Return 404 Not Found
4. **Database error** - Return 500 Internal Server Error
5. **Invalid parameters** - Return 422 Unprocessable Entity

**Implementation:**
```python
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
```

### Frontend Error Handling

**Strategy:** Try-catch blocks with user-friendly notifications

**Common Error Scenarios:**
1. **Network error** - Show "Connection error" notification
2. **API error** - Show error message from API response
3. **No questions available** - Show "No questions found" message
4. **Upload failed** - Show specific error message

**Implementation:**
```javascript
async function loadQuestions(subjectId, difficulty) {
  try {
    const response = await fetch(`/api/questions/?subject_id=${subjectId}&difficulty=${difficulty}&limit=15`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const questions = await response.json();
    
    if (questions.length === 0) {
      showNotification('No questions available for this selection', 'warning');
      return;
    }
    
    // Process questions...
  } catch (error) {
    console.error('Error loading questions:', error);
    showNotification('Failed to load questions. Please try again.', 'error');
  }
}
```

## Testing Strategy

### Backend Testing

**Unit Tests:**
- Test each model's CRUD operations
- Test question generation logic
- Test document parsing functions
- Test API endpoint responses

**Integration Tests:**
- Test complete question retrieval flow
- Test file upload and question generation flow
- Test database relationships and cascading deletes

**Test Framework:** pytest

**Example Test:**
```python
def test_get_questions_by_subject_and_difficulty(client, db_session):
    # Arrange
    subject = create_test_subject(db_session)
    create_test_questions(db_session, subject.id, difficulty="EASY", count=15)
    
    # Act
    response = client.get(f"/api/questions/?subject_id={subject.id}&difficulty=EASY&limit=15")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 15
    assert all(q["difficulty"] == "EASY" for q in data)
```

### Frontend Testing

**Manual Testing Checklist:**
- [ ] Subject selection loads correct questions
- [ ] Difficulty switching maintains subject context
- [ ] Question navigation works correctly
- [ ] Answer selection provides immediate feedback
- [ ] Hint display works for all questions
- [ ] Submit test calculates correct statistics
- [ ] File upload generates 45 questions
- [ ] Uploaded questions appear only in "My Questions"
- [ ] Theme switching works smoothly
- [ ] All animations render correctly
- [ ] Mobile responsive design works

**Browser Testing:**
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment Considerations

### Development Environment

**Setup Steps:**
1. Create virtual environment: `python -m venv venv`
2. Activate environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize database: `python seed_database.py`
5. Start server: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

### Production Considerations

**Performance:**
- Use connection pooling for database
- Implement caching for frequently accessed data
- Optimize database queries with proper indexes
- Compress static assets

**Security:**
- Validate all file uploads
- Sanitize user inputs
- Implement rate limiting
- Use HTTPS in production
- Set secure CORS policies

**Monitoring:**
- Log all errors and exceptions
- Monitor API response times
- Track database query performance
- Monitor file upload success rates

## Design Decisions and Rationales

### 1. SQLite vs PostgreSQL

**Decision:** Use SQLite for initial implementation

**Rationale:**
- Simpler setup and deployment
- No separate database server required
- Sufficient for expected load (single user or small team)
- Easy to backup (single file)
- Can migrate to PostgreSQL later if needed

### 2. Embedded CSS/JS vs Separate Files

**Decision:** Embed CSS and JavaScript in HTML

**Rationale:**
- Reduces HTTP requests
- Simplifies deployment (single file)
- Easier cache management
- No build process required
- Suitable for application size

### 3. Vanilla JavaScript vs Framework

**Decision:** Use vanilla JavaScript (no React/Vue/Angular)

**Rationale:**
- No build process or dependencies
- Faster initial load time
- Easier to understand and maintain
- Sufficient for application complexity
- Reduces bundle size

### 4. State Management Approach

**Decision:** Use global state object with explicit reset methods

**Rationale:**
- Prevents question mixing bugs
- Clear state lifecycle
- Easy to debug
- No framework overhead
- Explicit is better than implicit

### 5. Question Separation Strategy

**Decision:** Use source_document field to separate curated and uploaded questions

**Rationale:**
- Single table simplifies queries
- Easy to filter by source
- Maintains referential integrity
- Allows future expansion (multiple sources)

### 6. File Upload Processing

**Decision:** Generate questions immediately on upload

**Rationale:**
- Immediate feedback to user
- No background job complexity
- Acceptable processing time for small files
- Simpler error handling

## Future Enhancements

**Potential Features:**
1. User authentication and profiles
2. Progress tracking across sessions
3. Spaced repetition algorithm
4. Social features (leaderboards, sharing)
5. AI-powered question generation from document content
6. Export results to PDF
7. Custom question creation interface
8. Multi-language support
9. Accessibility improvements (screen reader support)
10. Offline mode with service workers
