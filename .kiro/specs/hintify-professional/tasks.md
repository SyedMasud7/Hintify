# Hintify Professional - Implementation Plan

## Task Overview

This implementation plan breaks down Hintify Professional into discrete, manageable coding tasks. Each task builds incrementally, ensuring a stable application at every step. The plan follows implementation-first development with optional testing tasks marked with *.

## Implementation Tasks

- [x] 1. Set up project structure and dependencies
- [x] 1.1 Create project directory structure
  - Create backend/app/ with subdirectories: models/, routers/, services/, ai/, scripts/
  - Create frontend/ with assets/ subdirectory
  - Create tests/ directory
  - _Requirements: 15.1_

- [x] 1.2 Create requirements.txt with all dependencies
  - Add FastAPI, SQLAlchemy, Alembic, Uvicorn
  - Add AI libraries: openai, litellm, tenacity, cachetools
  - Add file processing: pdfminer.six, python-docx, python-pptx, python-magic
  - Add security: slowapi, passlib, python-multipart
  - Add dev tools: pytest, black, isort, ruff, httpx
  - _Requirements: 15.2_

- [x] 1.3 Create Makefile with common commands
  - Implement install, dev, format, lint, test, seed, reset-db, run targets
  - _Requirements: 14.5_

- [x] 1.4 Create .env.example with all environment variables
  - Add DATABASE_URL, AI_PROVIDER, AI_API_KEY, AI_MODEL
  - Add HOST, PORT, ALLOWED_ORIGINS, SECRET_KEY
  - _Requirements: 15.5_

- [-] 2. Implement database foundation
- [x] 2.1 Create database.py with SQLAlchemy configuration
  - Implement engine with configurable DATABASE_URL
  - Create SessionLocal factory
  - Define Base declarative class
  - Implement get_db() dependency
  - _Requirements: 12.1_

- [x] 2.2 Create Subject model
  - Define Subject class with id, name, description, icon, color, is_active, created_at
  - Set up relationship to questions
  - _Requirements: 12.1_

- [x] 2.3 Create Question model with DifficultyLevel enum
  - Define DifficultyLevel enum (EASY, MEDIUM, HARD)
  - Define Question class with all fields including source_document
  - Set up relationships to subject, choices, hint, attempts
  - _Requirements: 12.2_

- [x] 2.4 Create Choice model
  - Define Choice class with id, question_id, choice_text, is_correct, letter
  - Set up relationship to question with cascade delete
  - _Requirements: 12.3_

- [x] 2.5 Create Hint model
  - Define Hint class with id, question_id, hint_text, is_ai_generated
  - Set up one-to-one relationship with question
  - _Requirements: 12.4_

- [ ] 2.6 Create TestSession model
  - Define TestSession class with id, subject_id, difficulty, timestamps, total_questions
  - Set up relationships to subject and attempts
  - _Requirements: 12.5_

- [x] 2.7 Create Attempt model
  - Define Attempt class with id, test_session_id, question_id, selected_answer, is_correct, time_taken, hint_used
  - Set up relationships to test_session and question
  - _Requirements: 12.6_

- [x] 2.8 Set up Alembic for migrations
  - Initialize Alembic configuration
  - Create initial migration from models
  - _Requirements: 12.7_


- [x] 3. Implement AI provider layer
- [x] 3.1 Create base AI provider interface
  - Define abstract AIProvider class with generate_hint(), generate_explanation(), generate_questions(), calibrate_difficulty() methods
  - _Requirements: 1.1_

- [x] 3.2 Implement OpenAI provider
  - Create OpenAIProvider class implementing AIProvider interface
  - Implement retry logic with tenacity
  - Implement timeout handling (30 seconds)
  - Add prompt templates for hints, explanations, question generation
  - _Requirements: 1.1, 1.4, 1.5_

- [x] 3.3 Implement DeepSeek provider
  - Create DeepSeekProvider class implementing AIProvider interface
  - Use LiteLLM or direct API calls
  - Implement same retry and timeout logic
  - _Requirements: 1.1_

- [x] 3.4 Implement local model provider
  - Create LocalProvider class for local LLM inference
  - Implement same interface methods
  - _Requirements: 1.1_

- [x] 3.5 Implement fallback rule-based provider
  - Create FallbackProvider with keyword extraction
  - Implement distractor elimination logic
  - Create template-based explanations
  - _Requirements: 1.3, 2.5_

- [x] 3.6 Implement AI response caching
  - Create cache.py with TTLCache (24 hour TTL)
  - Implement cache decorators for hint and explanation methods
  - _Requirements: 1.5_

- [x] 3.7 Create AI provider factory
  - Implement get_ai_provider() function reading from environment
  - Handle missing API key gracefully with fallback
  - _Requirements: 1.2, 1.3_

- [x] 4. Create seed data with 180 curated questions
- [x] 4.1 Create seed_database.py script structure
  - Implement main seeding function with transaction management
  - Add logging for progress tracking
  - _Requirements: 3.1, 15.4_

- [x] 4.2 Define and seed 4 subjects
  - Create Technology subject (💻, #3B82F6)
  - Create Science subject (🔬, #10B981)
  - Create Geography subject (🌍, #F59E0B)
  - Create General Knowledge subject (📚, #EF4444)
  - _Requirements: 3.2_

- [x] 4.3 Create Technology questions (45 total: 15 easy, 15 medium, 15 hard)
  - Define 15 EASY Technology questions with 4 choices, hints, explanations
  - Define 15 MEDIUM Technology questions with 4 choices, hints, explanations
  - Define 15 HARD Technology questions with 4 choices, hints, explanations
  - _Requirements: 3.3, 3.4_

- [x] 4.4 Create Science questions (45 total: 15 easy, 15 medium, 15 hard)
  - Define 15 EASY Science questions with 4 choices, hints, explanations
  - Define 15 MEDIUM Science questions with 4 choices, hints, explanations
  - Define 15 HARD Science questions with 4 choices, hints, explanations
  - _Requirements: 3.3, 3.4_

- [x] 4.5 Create Geography questions (45 total: 15 easy, 15 medium, 15 hard)
  - Define 15 EASY Geography questions with 4 choices, hints, explanations
  - Define 15 MEDIUM Geography questions with 4 choices, hints, explanations
  - Define 15 HARD Geography questions with 4 choices, hints, explanations
  - _Requirements: 3.3, 3.4_

- [x] 4.6 Create General Knowledge questions (45 total: 15 easy, 15 medium, 15 hard)
  - Define 15 EASY General Knowledge questions with 4 choices, hints, explanations
  - Define 15 MEDIUM General Knowledge questions with 4 choices, hints, explanations
  - Define 15 HARD General Knowledge questions with 4 choices, hints, explanations
  - _Requirements: 3.3, 3.4_

- [x] 4.7 Implement seed execution and verification
  - Execute seeding with proper error handling
  - Verify 180 total questions created
  - Verify correct distribution (4 subjects × 45 questions)
  - _Requirements: 3.1, 3.2, 3.3_

- [x] 5. Implement document processing services
- [x] 5.1 Create document parser service
  - Implement parse_pdf() using pdfminer.six
  - Implement parse_docx() using python-docx
  - Implement parse_pptx() using python-pptx
  - Implement detect_file_type() using python-magic
  - Add error handling for corrupted files
  - _Requirements: 4.1_

- [x] 5.2 Create question generator service
  - Implement QuestionGenerator class with AI provider dependency
  - Implement generate_from_text() method
  - Generate exactly 45 questions (15 per difficulty)
  - Use AI for difficulty calibration
  - Implement _balance_difficulty() to ensure distribution
  - _Requirements: 4.3, 4.6_

- [ ] 6. Implement backend API routers
- [ ] 6.1 Create Subjects router
  - Implement GET /api/subjects endpoint
  - Return subjects with question counts
  - Add error handling
  - _Requirements: 11.1_

- [ ] 6.2 Create Questions router
  - Implement GET /api/questions with subject_id, difficulty, limit, offset filters
  - Filter out uploaded questions (source_document IS NULL)
  - Implement GET /api/questions/{id} for single question
  - Implement GET /api/questions/{id}/hint with rate limiting (30/min)
  - Implement GET /api/questions/uploaded for uploaded questions
  - _Requirements: 11.2, 2.6_

- [ ] 6.3 Create Tests router
  - Implement POST /api/tests/start endpoint
  - Create test session and return question IDs
  - Implement GET /api/tests/{id}/summary for results
  - Calculate score, accuracy, time taken, streaks
  - _Requirements: 11.3, 11.5_

- [ ] 6.4 Create Attempts router
  - Implement POST /api/attempts/submit endpoint
  - Check answer correctness
  - Return immediate verdict with explanation
  - Track time taken and hint usage
  - _Requirements: 11.4_

- [x] 6.5 Create Upload router
  - Implement POST /api/uploads endpoint with rate limiting (5/hour)
  - Validate file type (PDF, DOCX, PPTX)
  - Validate file size (max 10MB)
  - Verify MIME type with python-magic
  - Parse document content
  - Generate 45 questions using AI
  - Store questions with source_document reference
  - Return generated questions
  - _Requirements: 11.6, 4.1, 4.2, 4.3, 13.2, 13.6_

- [ ] 6.6 Create Reports router
  - Implement GET /api/reports/overview endpoint
  - Calculate accuracy by subject for donut chart
  - Calculate difficulty distribution for bar chart
  - Calculate progress over time for line chart
  - Calculate topic heatmap data
  - _Requirements: 11.7_

- [ ] 6.7 Create Admin router
  - Implement GET /api/admin/export for JSON/CSV export
  - Implement POST /api/admin/import for JSON/CSV import
  - _Requirements: 11.8_


- [ ] 7. Create main FastAPI application
- [ ] 7.1 Implement main.py with app configuration
  - Initialize FastAPI app with title, description, version
  - Configure CORS middleware with ALLOWED_ORIGINS from env
  - Set up rate limiting with slowapi
  - Register all routers (subjects, questions, tests, attempts, uploads, reports, admin)
  - _Requirements: 11.9, 13.4_

- [ ] 7.2 Add static file serving
  - Mount frontend directory for static files
  - Serve index.html at root path
  - _Requirements: 15.6_

- [ ] 7.3 Add global exception handlers
  - Implement HTTPException handler with error_code and timestamp
  - Implement general Exception handler with logging
  - _Requirements: 13.5_

- [-] 8. Create frontend HTML structure
- [x] 8.1 Create index.html with semantic HTML5 structure
  - Add meta tags including viewport, description, OpenGraph tags
  - Include Font Awesome 6.4+ CDN
  - Include Chart.js 4.4+ CDN
  - Include Particles.js 2.0+ CDN
  - Link manifest.json for PWA
  - _Requirements: 8.1, 10.5_

- [ ] 8.2 Create navigation header
  - Add Hintify logo with graduation cap icon
  - Create nav links: Home, Take Test, Upload, Reports
  - Add theme toggle button with moon/sun icon
  - _Requirements: 8.7_

- [ ] 8.3 Create Home section
  - Add hero with title, tagline, and CTA buttons
  - Add features grid showcasing AI hints, analytics, file upload
  - _Requirements: 8.1_

- [ ] 8.4 Create Take Test section
  - Create subject selection grid
  - Create test interface with difficulty selector
  - Add question display container
  - Add options container with A-D labels
  - Add question navigation grid (15 boxes)
  - Add statistics panel (attempted, correct, remaining, accuracy)
  - Add timer display
  - Add navigation buttons (Previous, Next, Submit Test, Exit)
  - Add hint button and hint display area
  - _Requirements: 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10_

- [ ] 8.5 Create Upload Files section
  - Add file input with drag-and-drop area
  - Add subject selector for uploaded questions
  - Add upload button
  - Create upload progress indicator
  - Create generated questions display with edit capability
  - _Requirements: 7.1, 7.2, 7.3, 7.4_

- [ ] 8.6 Create Reports section
  - Add summary cards (total tests, avg accuracy, avg time)
  - Add canvas elements for Chart.js charts
  - Add chart containers for donut, bar, line, heatmap
  - Add export buttons (PNG, PDF)
  - _Requirements: 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8_

- [ ] 8.7 Create professional footer
  - Add footer sections: Help, Resources, Company, Social
  - Add links: Help Center, Docs, Terms, Privacy, Contact
  - Add links: Status, Release Notes, Careers
  - Add social icons: GitHub, Twitter/X, LinkedIn
  - Style with glassmorphism
  - _Requirements: 9.1, 9.2, 9.3, 9.4_

- [ ] 9. Implement frontend CSS styling
- [ ] 9.1 Create CSS variables for theming
  - Define color palette (primary #667eea, secondary #764ba2, success #10b981, error #ef4444, warning #f59e0b)
  - Define glassmorphism variables (glass-bg, glass-border, glass-shadow)
  - Create [data-theme="dark"] and [data-theme="light"] variants
  - _Requirements: 8.3, 8.4_

- [ ] 9.2 Implement glassmorphism base styles
  - Create .glass-card class with backdrop-filter blur(20px)
  - Add transparent backgrounds with rgba
  - Implement subtle borders and box shadows
  - _Requirements: 8.1_

- [ ] 9.3 Implement Particles.js animated background
  - Initialize particles.js with floating particles configuration
  - Configure particle count, size, speed, connections
  - Optimize for 60fps performance
  - _Requirements: 8.2_

- [ ] 9.4 Style navigation and header
  - Style header with glassmorphism and sticky positioning
  - Style nav links with hover effects and active states
  - Style theme toggle button with smooth transitions
  - _Requirements: 8.7_

- [ ] 9.5 Style subject cards
  - Create grid layout with auto-fit minmax(280px, 1fr)
  - Add glassmorphism effects
  - Implement hover animations (translateY, scale, box-shadow)
  - Style subject icons (4rem font-size)
  - _Requirements: 8.1, 8.9_

- [ ] 9.6 Style test interface
  - Style difficulty selector with active state highlighting
  - Style statistics cards with glassmorphism
  - Style question container with proper spacing
  - Style options with hover, selected, correct, incorrect states
  - Style question navigation grid with status colors
  - Add animations for correct (pulse) and incorrect (shake)
  - _Requirements: 5.3, 5.4, 5.5, 5.6, 8.9_

- [ ] 9.7 Style buttons and interactive elements
  - Create .btn base styles with padding, border-radius
  - Create .btn-primary, .btn-secondary, .btn-success, .btn-error variants
  - Add hover and active states with transform
  - Implement smooth transitions (300ms)
  - Add focus states for accessibility
  - _Requirements: 8.6, 8.9_

- [ ] 9.8 Implement responsive design
  - Add mobile breakpoints (@media max-width: 768px)
  - Adjust grid layouts for smaller screens
  - Ensure touch-friendly button sizes (min 44px)
  - Stack navigation on mobile
  - _Requirements: 8.8_

- [ ] 9.9 Style timer with warning and danger states
  - Style timer display with icon
  - Add .timer.warning class (yellow, pulse animation)
  - Add .timer.danger class (red, faster pulse)
  - _Requirements: 5.7_

- [ ] 9.10 Style charts and analytics
  - Style chart containers with glassmorphism
  - Style summary cards with large numbers
  - Style heatmap grid with color gradients
  - _Requirements: 6.2, 6.7_


- [ ] 10. Implement frontend JavaScript - Core functionality
- [ ] 10.1 Create global AppState object
  - Define state properties: currentTestSessionId, currentSubjectId, currentDifficulty, currentQuestions, currentQuestionIndex, userAnswers
  - Define timer properties: timerEnabled, timerSeconds, timerInterval
  - Define UI properties: currentSection, theme
  - Define analytics properties: testHistory (from localStorage)
  - Implement reset() method
  - Implement startTimer() and stopTimer() methods
  - Implement saveTestResult() method
  - _Requirements: 5.1, 5.7, 6.9_

- [ ] 10.2 Implement section navigation
  - Create showSection() function to show/hide sections
  - Update active nav link styling
  - Load section-specific data (subjects for test, analytics for reports)
  - _Requirements: 8.7_

- [ ] 10.3 Implement theme switching
  - Create toggleTheme() function
  - Switch between dark and light themes on html[data-theme]
  - Save preference to localStorage
  - Update theme icon (moon/sun)
  - Detect system preference with prefers-color-scheme on load
  - _Requirements: 8.3, 8.4, 8.5_

- [ ] 10.4 Initialize Particles.js background
  - Configure particles.js with particle count, size, color, speed
  - Set up particle connections and interactions
  - Ensure smooth 60fps animation
  - _Requirements: 8.2_

- [ ] 11. Implement frontend JavaScript - Subject and test management
- [ ] 11.1 Implement subject loading
  - Create loadSubjects() async function
  - Fetch from GET /api/subjects
  - Render subject cards with icon, name, description, question count
  - Add click handlers for subject selection
  - _Requirements: 5.2_

- [ ] 11.2 Implement subject selection and test start
  - Create selectSubject() function
  - Reset AppState
  - Set currentSubjectId and currentSubjectName
  - Call startTest() function
  - _Requirements: 5.1, 5.2_

- [ ] 11.3 Implement test session creation
  - Create startTest() async function
  - POST to /api/tests/start with subject_id, difficulty, question_count
  - Store test_session_id in AppState
  - Call loadQuestions()
  - Start timer if enabled
  - Show test interface
  - _Requirements: 5.1, 11.3_

- [ ] 11.4 Implement question loading
  - Create loadQuestions() async function
  - Fetch from GET /api/questions with subject_id, difficulty, limit=15
  - Store questions in AppState.currentQuestions
  - Initialize userAnswers array
  - Call displayQuestion(0)
  - _Requirements: 5.4, 11.2_

- [ ] 11.5 Implement difficulty switching
  - Create switchDifficulty() function
  - Maintain current subject
  - Reset test state
  - Load questions for new difficulty
  - Update active difficulty button styling
  - _Requirements: 5.3_

- [ ] 12. Implement frontend JavaScript - Question display and interaction
- [ ] 12.1 Implement question display
  - Create displayQuestion(index) function
  - Render question text, number, difficulty badge
  - Render 4 options with A-D labels
  - Highlight selected option if exists
  - Update question navigation grid
  - Update statistics panel
  - Store question start time
  - _Requirements: 5.4, 5.5, 5.6_

- [ ] 12.2 Implement option selection
  - Create selectOption(optionIndex) function
  - Store selected answer in userAnswers[currentIndex]
  - Update UI to show selected option
  - Enable submit button
  - _Requirements: 5.5_

- [ ] 12.3 Implement answer submission
  - Create submitAnswer() async function
  - Calculate time taken since question start
  - POST to /api/attempts/submit with test_session_id, question_id, selected_answer, time_taken
  - Store is_correct in userAnswers
  - Show visual feedback (green for correct, red for incorrect)
  - Display explanation text
  - Disable option selection after submission
  - _Requirements: 5.5, 11.4_

- [ ] 12.4 Implement question navigation
  - Create nextQuestion() function
  - Create previousQuestion() function
  - Create jumpToQuestion(index) function for grid navigation
  - Update currentQuestionIndex
  - Call displayQuestion() with new index
  - _Requirements: 5.6_

- [ ] 12.5 Implement hint functionality
  - Create getHint() async function
  - Fetch from GET /api/questions/{id}/hint
  - Display hint in dedicated container with slide-down animation
  - Mark hint_used in userAnswers
  - _Requirements: 5.8, 2.1, 2.2_

- [ ] 12.6 Implement real-time statistics display
  - Create updateStats() function
  - Calculate attempted, correct, remaining, accuracy
  - Update statistics cards in real-time
  - Update progress bar
  - _Requirements: 5.9, 6.1, 6.2_

- [ ] 12.7 Implement timer display
  - Create updateTimerDisplay() function
  - Format seconds as MM:SS
  - Add warning class when > 10 minutes
  - Add danger class when > 15 minutes
  - _Requirements: 5.7_

- [ ] 12.8 Implement question navigation grid
  - Create updateNavigationGrid() function
  - Render 15 numbered boxes
  - Apply status classes: current, answered-correct, answered-incorrect, unanswered
  - Add click handlers to jump to questions
  - _Requirements: 5.6_

- [ ] 13. Implement frontend JavaScript - Test completion
- [ ] 13.1 Implement test submission
  - Create submitTest() async function
  - Stop timer
  - Fetch from GET /api/tests/{id}/summary
  - Calculate final statistics
  - Save test result to localStorage
  - Display results screen
  - _Requirements: 6.1, 11.5_

- [ ] 13.2 Implement results display
  - Create displayResults() function
  - Render summary cards: total, correct, incorrect, unanswered
  - Display accuracy percentage with progress bar
  - Display time taken
  - Display streak information
  - Show per-question breakdown
  - Provide "Back to Subjects" and "Try Again" buttons
  - _Requirements: 6.1, 6.2, 6.3_

- [ ] 13.3 Implement exit test functionality
  - Create exitTest() function
  - Confirm with user before exiting
  - Stop timer
  - Reset AppState
  - Return to subject selection
  - _Requirements: 5.10_


- [ ] 14. Implement frontend JavaScript - File upload
- [ ] 14.1 Implement file upload validation
  - Create validateFile() function
  - Check file type (PDF, DOCX, PPTX)
  - Check file size (max 10MB)
  - Show validation errors
  - _Requirements: 7.1, 4.2_

- [ ] 14.2 Implement file upload
  - Create uploadFile() async function
  - Create FormData with file and subject_id
  - POST to /api/uploads
  - Show upload progress indicator
  - Handle errors gracefully
  - _Requirements: 7.1, 11.6_

- [ ] 14.3 Implement generated questions display
  - Create displayGeneratedQuestions() function
  - Group questions by difficulty (15 easy, 15 medium, 15 hard)
  - Display each question with options, hint, explanation
  - Add edit capability for each question
  - Add save button to persist edited questions
  - _Requirements: 7.3, 7.4, 7.5_

- [ ] 14.4 Implement question editing
  - Create editQuestion() function
  - Make question text, options, hint, explanation editable
  - Validate edited data
  - Update question in memory before saving
  - _Requirements: 7.4, 7.5_

- [ ] 14.5 Implement save edited questions
  - Create saveEditedQuestions() async function
  - Validate all edited questions
  - Send to backend for database update
  - Show success/error notification
  - _Requirements: 7.6_

- [ ] 15. Implement frontend JavaScript - Analytics and charts
- [ ] 15.1 Implement analytics data loading
  - Create loadAnalytics() async function
  - Fetch from GET /api/reports/overview
  - Store analytics data
  - Call chart rendering functions
  - _Requirements: 6.9, 11.7_

- [ ] 15.2 Implement accuracy by subject chart (donut)
  - Create renderAccuracyBySubject() function
  - Use Chart.js to create doughnut chart
  - Configure colors matching subject colors
  - Add legend and title
  - _Requirements: 6.4_

- [ ] 15.3 Implement difficulty distribution chart (bar)
  - Create renderDifficultyDistribution() function
  - Use Chart.js to create bar chart
  - Show Easy (green), Medium (yellow), Hard (red)
  - Configure y-axis from 0-100%
  - _Requirements: 6.5_

- [ ] 15.4 Implement progress over time chart (line)
  - Create renderProgressOverTime() function
  - Use Chart.js to create line chart
  - Plot accuracy percentage over dates
  - Add smooth curve with tension
  - _Requirements: 6.6_

- [ ] 15.5 Implement topic heatmap
  - Create renderTopicHeatmap() function
  - Create grid with topics vs difficulties
  - Color cells based on performance (green=high, red=low)
  - Display percentage in each cell
  - _Requirements: 6.7_

- [ ] 15.6 Implement report export
  - Create exportReport() function
  - Export charts as PNG using Chart.js toBase64Image()
  - Generate PDF using jsPDF library
  - Download file to user's device
  - _Requirements: 6.8_

- [ ] 16. Implement frontend JavaScript - Keyboard shortcuts
- [ ] 16.1 Implement keyboard event handler
  - Add keydown event listener on document
  - Check if currentSection is 'test'
  - Handle N key for nextQuestion()
  - Handle P key for previousQuestion()
  - Handle S key for submitAnswer()
  - Handle H key for getHint()
  - Handle D key for toggleDifficultyMenu()
  - _Requirements: 5.10_

- [ ] 17. Implement PWA functionality
- [ ] 17.1 Create manifest.json
  - Define app name, short_name, description
  - Add icons (192x192, 512x512)
  - Set start_url, display: standalone
  - Set theme_color and background_color
  - _Requirements: 10.1_

- [ ] 17.2 Create service worker
  - Implement install event to cache static assets
  - Implement fetch event for offline support
  - Cache index.html, manifest.json, icons, CDN resources
  - _Requirements: 10.2, 10.3_

- [ ] 17.3 Register service worker
  - Add service worker registration in main JavaScript
  - Handle registration success/failure
  - _Requirements: 10.2_

- [ ] 17.4 Create favicon and app icons
  - Create favicon.ico
  - Create icon-192.png for mobile
  - Create icon-512.png for high-res devices
  - _Requirements: 10.4_

- [ ] 17.5 Add OpenGraph meta tags
  - Add og:title, og:description, og:image
  - Add og:url, og:type
  - Add Twitter card tags
  - _Requirements: 10.5_

- [ ] 18. Testing and quality assurance
- [ ] 18.1 Write unit tests for AI providers
  - Test OpenAI provider hint generation
  - Test fallback provider logic
  - Test caching mechanism
  - _Requirements: 14.1, 14.2_

- [ ] 18.2 Write unit tests for services
  - Test document parser for PDF, DOCX, PPTX
  - Test question generator
  - Test analytics calculations
  - _Requirements: 14.1, 14.2_

- [ ] 18.3 Write integration tests for API routes
  - Test GET /api/subjects
  - Test GET /api/questions with filters
  - Test POST /api/tests/start flow
  - Test POST /api/attempts/submit
  - Test POST /api/uploads
  - Test GET /api/reports/overview
  - _Requirements: 14.2_

- [ ] 18.4 Run code formatting and linting
  - Run black on all Python files
  - Run isort on all Python files
  - Run ruff check on all Python files
  - Fix any linting errors
  - _Requirements: 14.4, 14.5_

- [ ] 18.5 Measure test coverage
  - Run pytest with coverage report
  - Ensure minimum 80% coverage
  - Identify untested code paths
  - _Requirements: 14.3_

- [ ] 19. Documentation and deployment preparation
- [ ] 19.1 Create comprehensive README.md
  - Add project description and features
  - Add setup instructions (install, seed, run)
  - Add environment variable documentation
  - Add API documentation overview
  - Add troubleshooting section
  - Add screenshots or ASCII art
  - _Requirements: 15.1_

- [ ] 19.2 Create terminal setup script
  - Create setup.sh for macOS/Linux
  - Check Python version (3.11+)
  - Create virtual environment
  - Install dependencies
  - Initialize database
  - Run seed script
  - Display success message with next steps
  - _Requirements: 15.1, 15.2, 15.3, 15.4_

- [ ] 19.3 Verify all acceptance criteria
  - Test app starts with make dev
  - Test frontend served at http://localhost:8000
  - Test API docs at http://localhost:8000/docs
  - Test 4 subjects with 3 difficulties each
  - Test per-question submit with immediate feedback
  - Test hint functionality
  - Test file upload generates 45 questions
  - Test analytics charts render correctly
  - Test dark/light theme toggle
  - Test responsive design on mobile
  - Test keyboard shortcuts
  - Test PWA installation
  - Verify 180 curated questions in database
  - Test AI provider fallback when no API key
  - Test rate limiting on hint and upload endpoints
  - _Requirements: All_

- [ ] 19.4 Create SECURITY.md
  - Document security features
  - Explain rate limiting
  - Explain input validation
  - Explain file upload security
  - Provide security contact information
  - _Requirements: 13.1, 13.2, 13.3, 13.5, 13.6_

- [ ] 19.5 Create CONTRIBUTING.md
  - Explain how to contribute
  - Document code style guidelines
  - Explain pull request process
  - Add code of conduct
  - _Requirements: 14.4_

- [ ] 19.6 Create LICENSE file
  - Add MIT License
  - _Requirements: 15.1_

- [ ] 19.7 Final verification and cleanup
  - Remove debug logging
  - Verify all environment variables documented
  - Test complete user flow end-to-end
  - Verify no console errors
  - Check for TODO comments
  - Ensure all files have proper headers
  - _Requirements: All_
