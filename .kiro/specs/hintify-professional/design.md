# Hintify Professional - Design Document

## Overview

Hintify Professional is a full-stack AI-powered learning platform built with FastAPI (backend) and vanilla JavaScript (frontend). The system features a provider-agnostic AI layer supporting OpenAI, DeepSeek, and local models with graceful fallback to rule-based hints. It uses SQLite for data storage with SQLAlchemy ORM for database abstraction, enabling easy migration to PostgreSQL or MySQL.

The architecture prioritizes simplicity, maintainability, security, and professional aesthetics with glassmorphism UI and live animated backgrounds.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Frontend (Browser - Vanilla JS)               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │   Home   │  │   Test   │  │  Upload  │  │ Reports  │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│  • Glassmorphism UI  • Particles.js  • Chart.js  • PWA         │
└─────────────────────────────────────────────────────────────────┘
                            │ REST API (JSON)
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Backend (FastAPI + Python)                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ Subjects │  │Questions │  │  Tests   │  │  Upload  │       │
│  │  Router  │  │  Router  │  │  Router  │  │  Router  │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                     │
│  │ Reports  │  │  Admin   │  │   AI     │                     │
│  │  Router  │  │  Router  │  │ Provider │                     │
│  └──────────┘  └──────────┘  └──────────┘                     │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AI Layer (Provider Agnostic)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │  OpenAI  │  │ DeepSeek │  │  Local   │  │ Fallback │       │
│  │ Provider │  │ Provider │  │  Model   │  │   Rules  │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Database (SQLite/PostgreSQL)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ subjects │  │questions │  │  choices │  │   hints  │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│  ┌──────────┐  ┌──────────┐                                    │
│  │  tests   │  │ attempts │                                    │
│  └──────────┘  └──────────┘                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Backend:**
- FastAPI 0.104+ - Modern async Python web framework
- SQLAlchemy 2.0+ - ORM with support for SQLite/PostgreSQL/MySQL
- Alembic - Database migrations
- Uvicorn - ASGI server
- Pydantic - Data validation
- Python 3.11+ - Programming language

**AI/ML:**
- OpenAI Python SDK - For OpenAI GPT models
- LiteLLM (optional) - Unified interface for multiple providers
- Tenacity - Retry logic with exponential backoff
- CacheTools - Response caching

**File Processing:**
- pdfminer.six - PDF text extraction
- python-docx - DOCX text extraction
- python-pptx - PPTX text extraction
- python-magic - File type detection

**Security:**
- slowapi - Rate limiting
- passlib[argon2] - Password hashing (for future use)
- python-multipart - File upload handling

**Frontend:**
- Vanilla JavaScript (ES6+) - No framework
- HTML5 - Semantic markup
- CSS3 - Glassmorphism + animations
- Chart.js 4.4+ - Analytics visualization
- Particles.js 2.0+ - Animated background
- Font Awesome 6.4+ - Icons

**Database:**
- SQLite 3 (default) - Embedded database
- PostgreSQL/MySQL (optional) - Production databases


## Components and Interfaces

### Backend Components

#### 1. Main Application (backend/app/main.py)

**Purpose:** Application entry point, configuration, and middleware setup

**Key Responsibilities:**
- Initialize FastAPI application with metadata
- Configure CORS middleware for cross-origin requests
- Mount static file directories for frontend
- Register all API routers
- Set up global exception handlers
- Configure rate limiting
- Serve frontend HTML at root

**Configuration:**
```python
app = FastAPI(
    title="Hintify Professional API",
    description="AI-Powered Learning Platform with Intelligent Hints",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

#### 2. Database Module (backend/app/database.py)

**Purpose:** Database connection and session management

**Key Components:**
- `engine`: SQLAlchemy engine with configurable URL
- `SessionLocal`: Session factory for dependency injection
- `Base`: Declarative base for all models
- `get_db()`: FastAPI dependency for database sessions

**Connection Configuration:**
```python
# Read from environment or default to SQLite
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./hintify.db"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_pre_ping=True,
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

#### 3. AI Provider Layer (backend/app/ai/)

**Purpose:** Provider-agnostic AI integration with fallback

**Structure:**
```
backend/app/ai/
├── __init__.py
├── base.py          # Abstract base provider
├── openai_provider.py
├── deepseek_provider.py
├── local_provider.py
├── fallback.py      # Rule-based hints
└── cache.py         # Response caching
```

**Base Provider Interface:**
```python
class AIProvider(ABC):
    @abstractmethod
    async def generate_hint(
        self,
        question: str,
        options: List[str],
        difficulty: str,
        pre_submit: bool = True
    ) -> str:
        """Generate hint without revealing answer"""
        pass
    
    @abstractmethod
    async def generate_explanation(
        self,
        question: str,
        correct_answer: str,
        user_answer: str = None
    ) -> str:
        """Generate detailed explanation"""
        pass
    
    @abstractmethod
    async def generate_questions(
        self,
        text: str,
        count: int = 45
    ) -> List[QuestionData]:
        """Generate MCQs from text"""
        pass
    
    @abstractmethod
    async def calibrate_difficulty(
        self,
        question: str,
        options: List[str]
    ) -> str:
        """Determine question difficulty"""
        pass
```

**Provider Factory:**
```python
def get_ai_provider() -> AIProvider:
    provider_name = os.getenv("AI_PROVIDER", "fallback").lower()
    api_key = os.getenv("AI_API_KEY")
    model = os.getenv("AI_MODEL", "gpt-3.5-turbo")
    
    if not api_key:
        logger.warning("No AI_API_KEY provided, using fallback")
        return FallbackProvider()
    
    if provider_name == "openai":
        return OpenAIProvider(api_key, model)
    elif provider_name == "deepseek":
        return DeepSeekProvider(api_key, model)
    elif provider_name == "local":
        return LocalProvider(model)
    else:
        return FallbackProvider()
```

**Caching Strategy:**
```python
# Cache hints for 24 hours
@cached(cache=TTLCache(maxsize=1000, ttl=86400))
async def get_cached_hint(question_id: int, pre_submit: bool) -> str:
    # Cache key includes question_id and pre_submit flag
    pass
```

**Fallback Provider:**
```python
class FallbackProvider(AIProvider):
    async def generate_hint(self, question, options, difficulty, pre_submit=True):
        # Extract keywords from question
        keywords = self._extract_keywords(question)
        
        # Eliminate one wrong answer
        if pre_submit:
            wrong_options = [opt for i, opt in enumerate(options) if i != correct_idx]
            eliminated = random.choice(wrong_options)
            return f"Hint: Option '{eliminated}' is incorrect. Focus on {keywords[0]}."
        
        # Post-submit: provide template explanation
        return self._template_explanation(question, keywords)
```


#### 4. Database Models (backend/app/models/)

**Subject Model:**
```python
class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    icon = Column(String(10))  # Emoji or icon class
    color = Column(String(7))  # Hex color
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    questions = relationship("Question", back_populates="subject", cascade="all, delete-orphan")
```

**Question Model:**
```python
class DifficultyLevel(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    explanation = Column(Text)
    source_document = Column(String(255), nullable=True)  # NULL for curated
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    subject = relationship("Subject", back_populates="questions")
    choices = relationship("Choice", back_populates="question", cascade="all, delete-orphan")
    hint = relationship("Hint", back_populates="question", uselist=False, cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="question")
```

**Choice Model:**
```python
class Choice(Base):
    __tablename__ = "choices"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    choice_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    letter = Column(String(1), nullable=False)  # A, B, C, D
    
    # Relationships
    question = relationship("Question", back_populates="choices")
    
    __table_args__ = (
        Index('idx_question_letter', 'question_id', 'letter'),
    )
```

**Hint Model:**
```python
class Hint(Base):
    __tablename__ = "hints"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False, unique=True)
    hint_text = Column(Text, nullable=False)
    is_ai_generated = Column(Boolean, default=False)
    
    # Relationships
    question = relationship("Question", back_populates="hint")
```

**TestSession Model:**
```python
class TestSession(Base):
    __tablename__ = "test_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    total_questions = Column(Integer, default=15)
    
    # Relationships
    subject = relationship("Subject")
    attempts = relationship("Attempt", back_populates="test_session", cascade="all, delete-orphan")
```

**Attempt Model:**
```python
class Attempt(Base):
    __tablename__ = "attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    test_session_id = Column(Integer, ForeignKey("test_sessions.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    selected_answer = Column(Integer, nullable=True)  # 0-3 or NULL if skipped
    is_correct = Column(Boolean, nullable=True)
    time_taken = Column(Integer, nullable=True)  # seconds
    hint_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    test_session = relationship("TestSession", back_populates="attempts")
    question = relationship("Question", back_populates="attempts")
```

#### 5. API Routers

**Subjects Router (backend/app/routers/subjects.py):**

Endpoints:
- `GET /api/subjects` - List all active subjects with question counts

Response:
```json
[
  {
    "id": 1,
    "name": "Technology",
    "description": "Computer science, programming, and digital technology",
    "icon": "💻",
    "color": "#3B82F6",
    "question_count": 45,
    "is_active": true
  }
]
```

**Questions Router (backend/app/routers/questions.py):**

Endpoints:
- `GET /api/questions` - Get questions with filters
  - Query params: `subject_id`, `difficulty`, `limit` (default 15), `offset` (default 0)
  - Returns only curated questions (source_document IS NULL)
- `GET /api/questions/{id}` - Get single question details
- `GET /api/questions/{id}/hint` - Get hint for question
- `GET /api/questions/uploaded` - Get all uploaded questions grouped by source

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
    "explanation": "CPU stands for Central Processing Unit...",
    "source_document": null
  }
]
```

**Tests Router (backend/app/routers/tests.py):**

Endpoints:
- `POST /api/tests/start` - Start new test session
  - Body: `{"subject_id": 1, "difficulty": "EASY", "question_count": 15}`
  - Returns: `{"test_session_id": 123, "question_ids": [1, 5, 8, ...]}`
- `GET /api/tests/{id}/summary` - Get test results
  - Returns: Score, accuracy, time taken, streaks, per-question breakdown

**Attempts Router (backend/app/routers/attempts.py):**

Endpoints:
- `POST /api/attempts/submit` - Submit answer for immediate feedback
  - Body: `{"test_session_id": 123, "question_id": 1, "selected_answer": 0, "time_taken": 15}`
  - Returns: `{"is_correct": true, "explanation": "...", "hint": "..."}`

**Upload Router (backend/app/routers/upload.py):**

Endpoints:
- `POST /api/uploads` - Upload document and generate questions
  - Form data: `file` (PDF/DOCX/PPTX), `subject_id`
  - Returns: `{"filename": "doc.pdf", "questions_generated": 45, "questions": [...]}`

**Reports Router (backend/app/routers/reports.py):**

Endpoints:
- `GET /api/reports/overview` - Get analytics data
  - Returns: Aggregated stats for charts (accuracy by subject, difficulty distribution, time trends, topic heatmap)

**Admin Router (backend/app/routers/admin.py):**

Endpoints:
- `GET /api/admin/export` - Export questions as JSON/CSV
- `POST /api/admin/import` - Import questions from JSON/CSV


#### 6. Services Layer

**Document Parser Service (backend/app/services/document_parser.py):**

Purpose: Extract text from uploaded documents

Methods:
```python
class DocumentParser:
    @staticmethod
    def parse_pdf(file_path: str) -> str:
        """Extract text from PDF using pdfminer.six"""
        pass
    
    @staticmethod
    def parse_docx(file_path: str) -> str:
        """Extract text from DOCX using python-docx"""
        pass
    
    @staticmethod
    def parse_pptx(file_path: str) -> str:
        """Extract text from PPTX using python-pptx"""
        pass
    
    @staticmethod
    def detect_file_type(file_path: str) -> str:
        """Detect file type using python-magic"""
        pass
```

**Question Generator Service (backend/app/services/question_generator.py):**

Purpose: Generate questions from document content using AI

Methods:
```python
class QuestionGenerator:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider
    
    async def generate_from_text(
        self,
        text: str,
        subject_id: int,
        filename: str
    ) -> List[QuestionData]:
        """
        Generate 45 MCQs (15 easy, 15 medium, 15 hard)
        Each with 4 options, hint, and explanation
        """
        questions = await self.ai_provider.generate_questions(text, count=45)
        
        # Calibrate difficulty for each question
        for q in questions:
            q.difficulty = await self.ai_provider.calibrate_difficulty(
                q.question_text,
                q.options
            )
        
        # Ensure distribution: 15 easy, 15 medium, 15 hard
        questions = self._balance_difficulty(questions)
        
        return questions
    
    def _balance_difficulty(self, questions: List[QuestionData]) -> List[QuestionData]:
        """Ensure exactly 15 of each difficulty level"""
        pass
```

**Analytics Service (backend/app/services/analytics.py):**

Purpose: Calculate statistics and generate report data

Methods:
```python
class AnalyticsService:
    @staticmethod
    def calculate_test_stats(test_session_id: int, db: Session) -> Dict:
        """Calculate score, accuracy, time, streaks"""
        pass
    
    @staticmethod
    def get_accuracy_by_subject(db: Session) -> Dict:
        """Aggregate accuracy data for donut chart"""
        pass
    
    @staticmethod
    def get_difficulty_distribution(db: Session) -> Dict:
        """Get question attempts by difficulty for bar chart"""
        pass
    
    @staticmethod
    def get_progress_over_time(db: Session) -> Dict:
        """Get accuracy trends for line chart"""
        pass
    
    @staticmethod
    def get_topic_heatmap(db: Session) -> Dict:
        """Get topic vs performance matrix"""
        pass
```

### Frontend Components

#### 1. Application Structure

**File Organization:**
```
frontend/
├── index.html              # Main HTML file
├── manifest.json           # PWA manifest
├── service-worker.js       # Service worker for offline
├── assets/
│   ├── favicon.ico
│   ├── icon-192.png
│   ├── icon-512.png
│   └── logo.svg
└── (CSS and JS embedded in HTML for simplicity)
```

#### 2. State Management

**Global State Object:**
```javascript
const AppState = {
  // Test state
  currentTestSessionId: null,
  currentSubjectId: null,
  currentSubjectName: null,
  currentDifficulty: 'EASY',
  currentQuestions: [],
  currentQuestionIndex: 0,
  userAnswers: [],
  questionStartTime: null,
  
  // Timer state
  timerEnabled: false,
  timerSeconds: 0,
  timerInterval: null,
  
  // UI state
  currentSection: 'home',
  theme: localStorage.getItem('theme') || 'dark',
  
  // Analytics state
  testHistory: JSON.parse(localStorage.getItem('testHistory') || '[]'),
  
  // Methods
  reset() {
    this.currentQuestions = [];
    this.currentQuestionIndex = 0;
    this.userAnswers = [];
    this.questionStartTime = null;
  },
  
  startTimer() {
    if (!this.timerEnabled) return;
    this.timerInterval = setInterval(() => {
      this.timerSeconds++;
      updateTimerDisplay();
    }, 1000);
  },
  
  stopTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
  },
  
  saveTestResult(result) {
    this.testHistory.push({
      ...result,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('testHistory', JSON.stringify(this.testHistory));
  }
};
```

#### 3. Core Functions

**Navigation:**
```javascript
function showSection(sectionId) {
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.getElementById(sectionId).classList.add('active');
  
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  document.querySelector(`[onclick="showSection('${sectionId}')"]`)?.classList.add('active');
  
  AppState.currentSection = sectionId;
  
  // Load data for section
  if (sectionId === 'test') loadSubjects();
  if (sectionId === 'reports') loadAnalytics();
}
```

**Subject & Question Loading:**
```javascript
async function loadSubjects() {
  try {
    const response = await fetch('/api/subjects');
    const subjects = await response.json();
    renderSubjects(subjects);
  } catch (error) {
    showNotification('Failed to load subjects', 'error');
  }
}

async function selectSubject(id, name) {
  AppState.reset();
  AppState.currentSubjectId = id;
  AppState.currentSubjectName = name;
  AppState.currentDifficulty = 'EASY';
  
  await startTest();
}

async function startTest() {
  try {
    // Start test session
    const response = await fetch('/api/tests/start', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        subject_id: AppState.currentSubjectId,
        difficulty: AppState.currentDifficulty,
        question_count: 15
      })
    });
    
    const data = await response.json();
    AppState.currentTestSessionId = data.test_session_id;
    
    // Load questions
    await loadQuestions();
    
    // Start timer if enabled
    AppState.startTimer();
    
    showTestInterface();
  } catch (error) {
    showNotification('Failed to start test', 'error');
  }
}

async function loadQuestions() {
  const response = await fetch(
    `/api/questions?subject_id=${AppState.currentSubjectId}&difficulty=${AppState.currentDifficulty}&limit=15`
  );
  AppState.currentQuestions = await response.json();
  AppState.userAnswers = new Array(AppState.currentQuestions.length).fill(null);
  displayQuestion(0);
}
```

**Question Display & Interaction:**
```javascript
function displayQuestion(index) {
  AppState.currentQuestionIndex = index;
  AppState.questionStartTime = Date.now();
  
  const question = AppState.currentQuestions[index];
  
  // Render question HTML
  document.getElementById('question-text').textContent = question.question_text;
  document.getElementById('question-number').textContent = `Question ${index + 1} of ${AppState.currentQuestions.length}`;
  document.getElementById('difficulty-badge').textContent = question.difficulty;
  
  // Render options
  const optionsContainer = document.getElementById('options-container');
  optionsContainer.innerHTML = question.options.map((opt, i) => `
    <div class="option ${AppState.userAnswers[index]?.selected === i ? 'selected' : ''}" 
         onclick="selectOption(${i})"
         data-option="${i}">
      <div class="option-letter">${String.fromCharCode(65 + i)}</div>
      <div class="option-text">${opt}</div>
    </div>
  `).join('');
  
  // Update navigation grid
  updateNavigationGrid();
  
  // Update stats
  updateStats();
}

function selectOption(optionIndex) {
  const currentAnswer = AppState.userAnswers[AppState.currentQuestionIndex] || {};
  currentAnswer.selected = optionIndex;
  AppState.userAnswers[AppState.currentQuestionIndex] = currentAnswer;
  
  // Update UI
  document.querySelectorAll('.option').forEach((opt, i) => {
    opt.classList.toggle('selected', i === optionIndex);
  });
}

async function submitAnswer() {
  const index = AppState.currentQuestionIndex;
  const question = AppState.currentQuestions[index];
  const answer = AppState.userAnswers[index];
  
  if (answer.selected === undefined) {
    showNotification('Please select an answer', 'warning');
    return;
  }
  
  const timeTaken = Math.floor((Date.now() - AppState.questionStartTime) / 1000);
  
  try {
    const response = await fetch('/api/attempts/submit', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        test_session_id: AppState.currentTestSessionId,
        question_id: question.id,
        selected_answer: answer.selected,
        time_taken: timeTaken
      })
    });
    
    const result = await response.json();
    
    // Store result
    answer.is_correct = result.is_correct;
    answer.submitted = true;
    
    // Show feedback
    showAnswerFeedback(result);
    
  } catch (error) {
    showNotification('Failed to submit answer', 'error');
  }
}
```


**Keyboard Shortcuts:**
```javascript
document.addEventListener('keydown', (e) => {
  if (AppState.currentSection !== 'test') return;
  
  switch(e.key.toLowerCase()) {
    case 'n':
      nextQuestion();
      break;
    case 'p':
      previousQuestion();
      break;
    case 's':
      submitAnswer();
      break;
    case 'h':
      getHint();
      break;
    case 'd':
      toggleDifficultyMenu();
      break;
  }
});
```

**Analytics & Charts:**
```javascript
async function loadAnalytics() {
  try {
    const response = await fetch('/api/reports/overview');
    const data = await response.json();
    
    renderAccuracyBySubject(data.accuracy_by_subject);
    renderDifficultyDistribution(data.difficulty_distribution);
    renderProgressOverTime(data.progress_over_time);
    renderTopicHeatmap(data.topic_heatmap);
    
  } catch (error) {
    showNotification('Failed to load analytics', 'error');
  }
}

function renderAccuracyBySubject(data) {
  const ctx = document.getElementById('accuracy-chart').getContext('2d');
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        data: data.values,
        backgroundColor: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {position: 'bottom'},
        title: {display: true, text: 'Accuracy by Subject'}
      }
    }
  });
}

function renderDifficultyDistribution(data) {
  const ctx = document.getElementById('difficulty-chart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Easy', 'Medium', 'Hard'],
      datasets: [{
        label: 'Score',
        data: data.values,
        backgroundColor: ['#10B981', '#F59E0B', '#EF4444']
      }]
    },
    options: {
      responsive: true,
      scales: {y: {beginAtZero: true, max: 100}}
    }
  });
}

function renderProgressOverTime(data) {
  const ctx = document.getElementById('progress-chart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.dates,
      datasets: [{
        label: 'Accuracy %',
        data: data.accuracy,
        borderColor: '#667eea',
        tension: 0.4
      }]
    },
    options: {
      responsive: true,
      scales: {y: {beginAtZero: true, max: 100}}
    }
  });
}

function renderTopicHeatmap(data) {
  // Use Chart.js matrix plugin or custom grid
  const container = document.getElementById('heatmap-container');
  container.innerHTML = data.topics.map((topic, i) => `
    <div class="heatmap-row">
      <div class="topic-label">${topic}</div>
      ${data.difficulties.map((diff, j) => `
        <div class="heatmap-cell" 
             style="background-color: ${getHeatColor(data.values[i][j])}">
          ${data.values[i][j]}%
        </div>
      `).join('')}
    </div>
  `).join('');
}

function getHeatColor(value) {
  // Green (high) to red (low)
  const hue = (value / 100) * 120;
  return `hsl(${hue}, 70%, 50%)`;
}
```

**File Upload:**
```javascript
async function uploadFile() {
  const fileInput = document.getElementById('file-input');
  const file = fileInput.files[0];
  
  if (!file) {
    showNotification('Please select a file', 'warning');
    return;
  }
  
  // Validate file type
  const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'];
  if (!validTypes.includes(file.type)) {
    showNotification('Invalid file type. Please upload PDF, DOCX, or PPTX', 'error');
    return;
  }
  
  // Validate file size (10MB)
  if (file.size > 10 * 1024 * 1024) {
    showNotification('File too large. Maximum size is 10MB', 'error');
    return;
  }
  
  const formData = new FormData();
  formData.append('file', file);
  formData.append('subject_id', AppState.currentSubjectId);
  
  try {
    showUploadProgress();
    
    const response = await fetch('/api/uploads', {
      method: 'POST',
      body: formData
    });
    
    const result = await response.json();
    
    hideUploadProgress();
    showNotification(`Generated ${result.questions_generated} questions!`, 'success');
    
    // Display generated questions for editing
    displayGeneratedQuestions(result.questions);
    
  } catch (error) {
    hideUploadProgress();
    showNotification('Upload failed', 'error');
  }
}
```

**Theme Toggle:**
```javascript
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  // Update icon
  const icon = document.getElementById('theme-icon');
  icon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  
  AppState.theme = newTheme;
}

// Initialize theme on load
document.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme') || 
                     (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', savedTheme);
  AppState.theme = savedTheme;
});
```

**PWA Service Worker:**
```javascript
// service-worker.js
const CACHE_NAME = 'hintify-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/assets/logo.svg',
  '/assets/icon-192.png',
  '/assets/icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

## Data Models

### Database Schema

```sql
-- Subjects
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    icon VARCHAR(10),
    color VARCHAR(7),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Questions
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    difficulty VARCHAR(10) NOT NULL CHECK(difficulty IN ('EASY', 'MEDIUM', 'HARD')),
    explanation TEXT,
    source_document VARCHAR(255),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Choices
CREATE TABLE choices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    choice_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT 0,
    letter VARCHAR(1) NOT NULL CHECK(letter IN ('A', 'B', 'C', 'D')),
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Hints
CREATE TABLE hints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL UNIQUE,
    hint_text TEXT NOT NULL,
    is_ai_generated BOOLEAN DEFAULT 0,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Test Sessions
CREATE TABLE test_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    difficulty VARCHAR(10) NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    total_questions INTEGER DEFAULT 15,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Attempts
CREATE TABLE attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_session_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    selected_answer INTEGER,
    is_correct BOOLEAN,
    time_taken INTEGER,
    hint_used BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (test_session_id) REFERENCES test_sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Indexes
CREATE INDEX idx_questions_subject_difficulty ON questions(subject_id, difficulty);
CREATE INDEX idx_questions_source ON questions(source_document);
CREATE INDEX idx_choices_question ON choices(question_id);
CREATE INDEX idx_hints_question ON hints(question_id);
CREATE INDEX idx_attempts_session ON attempts(test_session_id);
CREATE INDEX idx_attempts_question ON attempts(question_id);
```

### Seed Data Structure

**Subject Data:**
```json
[
  {
    "name": "Technology",
    "description": "Computer science, programming, and digital technology concepts",
    "icon": "💻",
    "color": "#3B82F6"
  },
  {
    "name": "Science",
    "description": "Physics, chemistry, biology, and scientific principles",
    "icon": "🔬",
    "color": "#10B981"
  },
  {
    "name": "Geography",
    "description": "World geography, countries, capitals, and landmarks",
    "icon": "🌍",
    "color": "#F59E0B"
  },
  {
    "name": "General Knowledge",
    "description": "History, culture, current events, and general facts",
    "icon": "📚",
    "color": "#EF4444"
  }
]
```

**Question Data Example:**
```json
{
  "subject": "Technology",
  "question_text": "What does CPU stand for?",
  "difficulty": "EASY",
  "choices": [
    {"letter": "A", "text": "Central Processing Unit", "is_correct": true},
    {"letter": "B", "text": "Computer Personal Unit", "is_correct": false},
    {"letter": "C", "text": "Central Program Unit", "is_correct": false},
    {"letter": "D", "text": "Computer Processing Unit", "is_correct": false}
  ],
  "hint": "Think about the main component that processes instructions - it's the 'brain' of the computer.",
  "explanation": "CPU stands for Central Processing Unit. It's the primary component that executes instructions and performs calculations in a computer system."
}
```


## Error Handling

### Backend Error Handling

**Strategy:** Use FastAPI exception handlers with appropriate HTTP status codes

**Error Response Format:**
```json
{
  "detail": "Error message",
  "error_code": "SPECIFIC_ERROR_CODE",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

**Common Error Scenarios:**

1. **File Upload Errors:**
   - Invalid file type → 400 Bad Request
   - File too large → 413 Payload Too Large
   - Corrupted file → 422 Unprocessable Entity

2. **Resource Not Found:**
   - Question not found → 404 Not Found
   - Subject not found → 404 Not Found

3. **AI Provider Errors:**
   - API timeout → 504 Gateway Timeout
   - API rate limit → 429 Too Many Requests
   - Fallback to rule-based hints

4. **Database Errors:**
   - Connection error → 500 Internal Server Error
   - Constraint violation → 400 Bad Request

**Implementation:**
```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "error_code": getattr(exc, 'error_code', 'HTTP_ERROR'),
            "timestamp": datetime.utcnow().isoformat()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error_code": "INTERNAL_ERROR",
            "timestamp": datetime.utcnow().isoformat()
        }
    )
```

### Frontend Error Handling

**Strategy:** Try-catch blocks with user-friendly notifications

**Notification System:**
```javascript
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.innerHTML = `
    <i class="fas fa-${getIconForType(type)}"></i>
    <span>${message}</span>
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.classList.add('fade-out');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

function getIconForType(type) {
  const icons = {
    success: 'check-circle',
    error: 'exclamation-circle',
    warning: 'exclamation-triangle',
    info: 'info-circle'
  };
  return icons[type] || 'info-circle';
}
```

**Error Handling Patterns:**
```javascript
async function apiCall(url, options = {}) {
  try {
    const response = await fetch(url, options);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || `HTTP ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    showNotification(error.message || 'Network error', 'error');
    throw error;
  }
}
```

## Testing Strategy

### Backend Testing

**Unit Tests:**
```python
# tests/test_ai_provider.py
def test_openai_provider_hint_generation():
    provider = OpenAIProvider(api_key="test", model="gpt-3.5-turbo")
    hint = await provider.generate_hint(
        question="What is 2+2?",
        options=["3", "4", "5", "6"],
        difficulty="EASY",
        pre_submit=True
    )
    assert hint is not None
    assert "4" not in hint  # Should not reveal answer

# tests/test_question_generator.py
def test_generate_questions_from_text():
    generator = QuestionGenerator(FallbackProvider())
    text = "Python is a programming language..."
    questions = await generator.generate_from_text(text, subject_id=1, filename="test.pdf")
    assert len(questions) == 45
    assert sum(1 for q in questions if q.difficulty == "EASY") == 15

# tests/test_routers.py
def test_get_questions_by_subject(client, db_session):
    response = client.get("/api/questions?subject_id=1&difficulty=EASY&limit=15")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 15
    assert all(q["difficulty"] == "EASY" for q in data)
```

**Integration Tests:**
```python
def test_complete_test_flow(client, db_session):
    # Start test
    response = client.post("/api/tests/start", json={
        "subject_id": 1,
        "difficulty": "EASY",
        "question_count": 15
    })
    assert response.status_code == 200
    test_id = response.json()["test_session_id"]
    
    # Submit answers
    for question_id in response.json()["question_ids"]:
        response = client.post("/api/attempts/submit", json={
            "test_session_id": test_id,
            "question_id": question_id,
            "selected_answer": 0,
            "time_taken": 10
        })
        assert response.status_code == 200
    
    # Get summary
    response = client.get(f"/api/tests/{test_id}/summary")
    assert response.status_code == 200
    assert "accuracy" in response.json()
```

### Frontend Testing

**Manual Testing Checklist:**
- [ ] Subject selection loads correct questions
- [ ] Difficulty switching maintains subject context
- [ ] Question navigation (prev/next/jump) works
- [ ] Answer submission provides immediate feedback
- [ ] Hint display works without revealing answer
- [ ] Timer counts correctly
- [ ] Keyboard shortcuts function properly
- [ ] Test completion shows accurate results
- [ ] File upload generates 45 questions
- [ ] Analytics charts render correctly
- [ ] Theme switching works smoothly
- [ ] Responsive design on mobile/tablet/desktop
- [ ] PWA installation works
- [ ] Offline mode caches assets

**Browser Compatibility:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Security Considerations

### Input Validation

**Backend:**
```python
from pydantic import BaseModel, validator, Field

class QuestionFilter(BaseModel):
    subject_id: int = Field(..., gt=0)
    difficulty: DifficultyLevel
    limit: int = Field(15, ge=1, le=50)
    offset: int = Field(0, ge=0)

class UploadRequest(BaseModel):
    subject_id: int = Field(..., gt=0)
    
    @validator('subject_id')
    def subject_must_exist(cls, v, values, **kwargs):
        # Validate subject exists in database
        return v
```

**File Upload Security:**
```python
ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.pptx'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def validate_upload(file: UploadFile):
    # Check extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, "Invalid file type")
    
    # Check file size
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    if size > MAX_FILE_SIZE:
        raise HTTPException(413, "File too large")
    
    # Verify MIME type
    mime = magic.from_buffer(file.file.read(1024), mime=True)
    file.file.seek(0)
    if mime not in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', ...]:
        raise HTTPException(400, "Invalid file content")
```

### Rate Limiting

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@router.get("/questions/{id}/hint")
@limiter.limit("30/minute")
async def get_hint(request: Request, id: int, db: Session = Depends(get_db)):
    # Hint endpoint limited to 30 requests per minute
    pass

@router.post("/uploads")
@limiter.limit("5/hour")
async def upload_file(request: Request, file: UploadFile, db: Session = Depends(get_db)):
    # Upload limited to 5 per hour
    pass
```

### CORS Configuration

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### SQL Injection Prevention

SQLAlchemy ORM automatically prevents SQL injection through parameterized queries:
```python
# Safe - uses parameterized query
questions = db.query(Question).filter(
    Question.subject_id == subject_id,
    Question.difficulty == difficulty
).all()
```

## Deployment

### Environment Variables

**.env.example:**
```bash
# Database
DATABASE_URL=sqlite:///./hintify.db
# For PostgreSQL: postgresql://user:password@localhost/hintify
# For MySQL: mysql://user:password@localhost/hintify

# AI Provider
AI_PROVIDER=openai  # openai | deepseek | local | fallback
AI_API_KEY=your_api_key_here
AI_MODEL=gpt-3.5-turbo

# Server
HOST=0.0.0.0
PORT=8000
RELOAD=true

# Security
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
SECRET_KEY=your_secret_key_here

# Rate Limiting
RATE_LIMIT_ENABLED=true

# Logging
LOG_LEVEL=INFO
```

### Makefile

```makefile
.PHONY: install dev format lint test seed reset-db run build-frontend

install:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt

dev:
	. .venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

format:
	. .venv/bin/activate && black app/ tests/
	. .venv/bin/activate && isort app/ tests/

lint:
	. .venv/bin/activate && ruff check app/ tests/

test:
	. .venv/bin/activate && pytest tests/ -v --cov=app --cov-report=html

seed:
	. .venv/bin/activate && python -m app.scripts.seed_database

reset-db:
	rm -f hintify.db
	. .venv/bin/activate && alembic upgrade head
	make seed

run:
	. .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000

build-frontend:
	@echo "Frontend is vanilla JS - no build needed"
```

### Project Structure

```
hintify-professional/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── subject.py
│   │   │   ├── question.py
│   │   │   ├── choice.py
│   │   │   ├── hint.py
│   │   │   ├── test_session.py
│   │   │   └── attempt.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── subjects.py
│   │   │   ├── questions.py
│   │   │   ├── tests.py
│   │   │   ├── attempts.py
│   │   │   ├── uploads.py
│   │   │   ├── reports.py
│   │   │   └── admin.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── document_parser.py
│   │   │   ├── question_generator.py
│   │   │   └── analytics.py
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── openai_provider.py
│   │   │   ├── deepseek_provider.py
│   │   │   ├── local_provider.py
│   │   │   ├── fallback.py
│   │   │   └── cache.py
│   │   └── scripts/
│   │       ├── __init__.py
│   │       └── seed_database.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_ai_provider.py
│   │   ├── test_question_generator.py
│   │   └── test_routers.py
│   ├── alembic/
│   │   ├── versions/
│   │   └── env.py
│   ├── requirements.txt
│   ├── alembic.ini
│   └── .env.example
├── frontend/
│   ├── index.html
│   ├── manifest.json
│   ├── service-worker.js
│   └── assets/
│       ├── favicon.ico
│       ├── icon-192.png
│       ├── icon-512.png
│       └── logo.svg
├── Makefile
├── README.md
├── LICENSE
└── .gitignore
```

## Design Decisions and Rationales

### 1. Provider-Agnostic AI Layer

**Decision:** Abstract AI providers behind a common interface

**Rationale:**
- Flexibility to switch providers without code changes
- Cost optimization (use cheaper providers when appropriate)
- Graceful degradation with fallback
- Easy to add new providers

### 2. SQLite Default with PostgreSQL Support

**Decision:** Use SQLite by default, support PostgreSQL/MySQL via SQLAlchemy

**Rationale:**
- Zero configuration for development
- Easy deployment (single file database)
- Production-ready migration path
- SQLAlchemy abstracts database differences

### 3. Vanilla JavaScript (No Framework)

**Decision:** Use vanilla JS instead of React/Vue/Angular

**Rationale:**
- No build process required
- Faster initial load
- Easier to understand and maintain
- Sufficient for application complexity
- Smaller bundle size

### 4. Embedded CSS/JS in HTML

**Decision:** Embed styles and scripts in single HTML file

**Rationale:**
- Reduces HTTP requests
- Simplifies deployment
- No bundler needed
- Easier caching strategy
- Suitable for application size

### 5. localStorage for Client-Side State

**Decision:** Use localStorage for theme, test history, preferences

**Rationale:**
- No authentication required
- Persists across sessions
- Simple API
- Sufficient for user preferences
- No server-side storage needed

### 6. Chart.js for Analytics

**Decision:** Use Chart.js instead of D3.js or custom charts

**Rationale:**
- Simpler API
- Responsive by default
- Good documentation
- Sufficient chart types
- Smaller bundle size

### 7. Particles.js for Background

**Decision:** Use Particles.js for animated background

**Rationale:**
- Professional appearance
- Configurable and performant
- CDN available
- Widely used and tested
- Minimal performance impact

## Future Enhancements

1. **User Authentication** - Add optional user accounts for progress tracking
2. **Social Features** - Leaderboards, sharing, challenges
3. **Advanced AI** - Question rephrasing, adaptive difficulty
4. **Mobile Apps** - Native iOS/Android apps
5. **Collaborative Learning** - Study groups, shared tests
6. **Gamification** - Badges, achievements, streaks
7. **Content Marketplace** - User-generated question packs
8. **API for Third-Party Integration** - Allow external apps to use Hintify
9. **Advanced Analytics** - ML-powered insights, learning patterns
10. **Accessibility Improvements** - Screen reader support, high contrast mode
