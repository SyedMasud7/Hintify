# Hintify Professional - Requirements Document

## Introduction

Hintify Professional is an AI-powered learning platform that provides intelligent hints for multiple-choice questions. The system features a provider-agnostic AI layer supporting OpenAI, DeepSeek, and local models, with graceful fallback to rule-based hints. It includes document ingestion from PDF/DOCX/PPTX to auto-generate questions, comprehensive analytics with modern charts, user authentication, and a professional glassmorphism UI with live animated backgrounds.

## Glossary

- **System**: The Hintify Professional web application
- **User**: An authenticated person using the platform
- **AI Provider**: External LLM service (OpenAI, DeepSeek) or local model
- **Curated Question Bank**: Pre-loaded questions organized by subject and difficulty
- **MCQ**: Multiple Choice Question with 4 options (A-D)
- **Hint**: AI-generated or rule-based guidance without revealing the answer
- **Difficulty Calibration**: AI assessment of question complexity
- **Test Session**: A timed or untimed test instance
- **Glassmorphism**: UI design with transparent, blurred glass-like elements
- **PWA**: Progressive Web App with offline capabilities

## Requirements

### Requirement 1: AI Provider Integration

**User Story:** As a system administrator, I want a provider-agnostic AI layer that supports multiple LLM providers, so that I can choose the best AI service for my needs.

#### Acceptance Criteria

1. THE System SHALL support three AI providers: OpenAI, DeepSeek, and local models
2. THE System SHALL read AI configuration from environment variables: AI_PROVIDER, AI_API_KEY, AI_MODEL
3. WHEN no AI_API_KEY is provided, THE System SHALL use a rule-based fallback hint generator
4. THE System SHALL implement retry logic with exponential backoff for AI API calls
5. THE System SHALL cache AI responses to reduce API costs and improve performance
6. THE System SHALL implement timeout handling for AI requests with a maximum of 30 seconds
7. THE System SHALL sanitize prompts to prevent answer leakage in pre-submit hints

### Requirement 2: AI Hint Generation

**User Story:** As a user, I want intelligent hints that guide me without revealing the answer, so that I can learn effectively.

#### Acceptance Criteria

1. WHEN a user requests a hint before submitting, THE System SHALL provide a nudge, eliminate one distractor, or offer an analogy without revealing the correct answer
2. WHEN a user submits an incorrect answer, THE System SHALL provide a step-by-step explanation
3. WHEN a user submits a correct answer, THE System SHALL provide enrichment information
4. THE System SHALL use AI to generate contextual hints based on question content and difficulty
5. WHEN AI is unavailable, THE System SHALL use keyword extraction and template-based hints
6. THE System SHALL rate-limit hint requests to 30 per minute per user

### Requirement 3: Question Bank Management

**User Story:** As a content manager, I want a comprehensive question bank with 180 curated questions across 4 subjects, so that users have diverse learning content.

#### Acceptance Criteria

1. THE System SHALL store exactly 180 curated MCQs in the database
2. THE System SHALL organize questions into 4 subjects: Technology, Science, Geography, General Knowledge
3. THE System SHALL provide exactly 45 questions per subject (15 easy, 15 medium, 15 hard)
4. THE System SHALL ensure each question has 4 choices (A-D), one correct answer, an AI hint, and an explanation
5. WHEN a user requests questions, THE System SHALL filter by subject and difficulty
6. THE System SHALL mark questions as active/inactive for content management

### Requirement 4: Document Ingestion and Question Generation

**User Story:** As a user, I want to upload documents and have the system automatically generate questions, so that I can create custom learning content.

#### Acceptance Criteria

1. THE System SHALL accept PDF, DOCX, and PPTX file uploads
2. THE System SHALL validate file size with a maximum of 10MB
3. WHEN a user uploads a document, THE System SHALL extract text content using appropriate parsers
4. THE System SHALL use AI to generate at least 45 MCQs (15 easy, 15 medium, 15 hard) from the document
5. THE System SHALL generate AI hints for each auto-generated question
6. THE System SHALL use AI for difficulty calibration of generated questions
7. THE System SHALL store the source document reference with each generated question
8. THE System SHALL sanitize uploaded files to prevent security vulnerabilities

### Requirement 5: Test Taking Experience

**User Story:** As a user, I want an interactive test interface with immediate feedback and navigation controls, so that I can learn effectively.

#### Acceptance Criteria

1. WHEN a user starts a test, THE System SHALL create a test session with unique ID
2. THE System SHALL provide subject tabs for Technology, Science, Geography, and General Knowledge
3. THE System SHALL provide difficulty switcher for Easy, Medium, and Hard levels
4. THE System SHALL display one question at a time with 4 labeled options
5. WHEN a user submits an answer, THE System SHALL provide immediate verdict (Correct/Incorrect)
6. THE System SHALL display a question navigator grid showing attempted/correct/incorrect states
7. THE System SHALL provide optional timer functionality
8. THE System SHALL track per-question metrics: time taken, attempts, hint usage
9. THE System SHALL calculate real-time accuracy, streak, and estimated score
10. THE System SHALL support keyboard shortcuts: N (next), P (previous), S (submit), H (hint), D (difficulty menu)

### Requirement 6: Test Results and Analytics

**User Story:** As a user, I want comprehensive test results and analytics, so that I can track my learning progress.

#### Acceptance Criteria

1. WHEN a user completes a test, THE System SHALL calculate total score, accuracy, time taken, and streaks
2. THE System SHALL display results in cards showing total tests, average accuracy, and average time per question
3. THE System SHALL provide Chart.js visualizations including donut charts, bar graphs, line graphs, and heatmaps
4. THE System SHALL show accuracy by subject using donut/circle charts
5. THE System SHALL show score by difficulty using bar charts
6. THE System SHALL show progress over time using line graphs
7. THE System SHALL show topic vs performance using heatmap visualization
8. THE System SHALL allow report export as PNG or PDF
9. THE System SHALL store test history in localStorage for trend analysis

### Requirement 7: File Upload Interface

**User Story:** As a user, I want an intuitive upload interface that shows progress and allows editing, so that I can manage generated questions.

#### Acceptance Criteria

1. THE System SHALL provide a file upload page accepting PDF, DOCX, PPTX files
2. THE System SHALL show parsing progress during document processing
3. WHEN generation completes, THE System SHALL display 45+ MCQs grouped by difficulty
4. THE System SHALL allow users to edit any question or hint before saving
5. THE System SHALL validate edited questions for completeness
6. THE System SHALL save edited questions to the database

### Requirement 8: User Interface Design

**User Story:** As a user, I want a professional, modern interface with smooth animations, so that learning is enjoyable.

#### Acceptance Criteria

1. THE System SHALL implement glassmorphism design with transparent containers and backdrop blur
2. THE System SHALL provide live animated background using particles.js or CSS gradient waves
3. THE System SHALL support Dark and Light theme modes
4. THE System SHALL remember theme preference using localStorage
5. THE System SHALL detect system theme preference using prefers-color-scheme
6. THE System SHALL ensure WCAG AA contrast ratios for accessibility
7. THE System SHALL provide focus states for keyboard navigation
8. THE System SHALL be fully responsive for mobile, tablet, and desktop devices
9. THE System SHALL animate transitions smoothly at 60fps

### Requirement 9: Professional Footer

**User Story:** As a visitor, I want access to help resources and company information, so that I can learn more about the platform.

#### Acceptance Criteria

1. THE System SHALL display a footer with Help Center, Docs, Terms, Privacy, Contact links
2. THE System SHALL provide links to Status, Release Notes, and Careers pages
3. THE System SHALL include social media links: GitHub, Twitter/X, LinkedIn
4. THE System SHALL style the footer with glassmorphism matching the site design

### Requirement 10: Progressive Web App

**User Story:** As a mobile user, I want to install the app and use it offline, so that I can learn anywhere.

#### Acceptance Criteria

1. THE System SHALL provide a manifest.json file with app metadata
2. THE System SHALL implement a service worker to cache static assets
3. THE System SHALL enable "Add to Home Screen" functionality
4. THE System SHALL provide appropriate favicon set for all devices
5. THE System SHALL include OpenGraph tags for social sharing
6. THE System SHALL generate a sitemap for SEO

### Requirement 11: API Architecture

**User Story:** As a developer, I want a well-documented REST API, so that I can integrate with the system.

#### Acceptance Criteria

1. THE System SHALL provide GET /api/subjects for listing subjects
2. THE System SHALL provide GET /api/questions with subject, difficulty, limit, offset parameters
3. THE System SHALL provide POST /api/tests/start returning test_session_id and question order
4. THE System SHALL provide POST /api/attempts/submit for immediate verdict and hint
5. THE System SHALL provide GET /api/tests/{id}/summary for test results
6. THE System SHALL provide POST /api/uploads for document upload and question generation
7. THE System SHALL provide GET /api/reports/overview for analytics data
8. THE System SHALL provide GET /api/admin/export and POST /api/admin/import for data management
9. THE System SHALL document all endpoints in FastAPI automatic docs at /docs

### Requirement 12: Database Schema

**User Story:** As a developer, I want a normalized database schema with proper relationships, so that data integrity is maintained.

#### Acceptance Criteria

1. THE System SHALL implement a subjects table with id, name, description, icon, color fields
2. THE System SHALL implement a questions table with id, subject_id, question_text, difficulty, source_document fields
3. THE System SHALL implement a choices table with id, question_id, choice_text, is_correct, letter fields
4. THE System SHALL implement a hints table with id, question_id, hint_text fields
5. THE System SHALL implement a test_sessions table with id, subject_id, difficulty, started_at, completed_at fields
6. THE System SHALL implement an attempts table with id, test_session_id, question_id, selected_answer, is_correct, time_taken fields
7. THE System SHALL use Alembic for database migrations
8. THE System SHALL enforce foreign key constraints and cascading deletes

### Requirement 13: Security

**User Story:** As a system administrator, I want comprehensive security measures, so that the system is protected.

#### Acceptance Criteria

1. THE System SHALL validate all user inputs using Pydantic models
2. THE System SHALL sanitize file uploads to prevent malicious content
3. THE System SHALL implement rate limiting using slowapi
4. THE System SHALL configure CORS with appropriate origins
5. THE System SHALL log security events for audit trails
6. THE System SHALL enforce file size limits on uploads

### Requirement 14: Testing and Quality

**User Story:** As a developer, I want comprehensive tests, so that the system is reliable.

#### Acceptance Criteria

1. THE System SHALL provide pytest tests for core services
2. THE System SHALL provide tests for all API routes
3. THE System SHALL achieve minimum 80% code coverage
4. THE System SHALL use black, isort, and ruff for code formatting and linting
5. THE System SHALL provide a Makefile with dev, format, lint, test, seed, reset-db, run commands

### Requirement 15: Deployment and Operations

**User Story:** As a system administrator, I want easy deployment and operation, so that I can manage the system efficiently.

#### Acceptance Criteria

1. THE System SHALL provide a terminal script for project scaffolding
2. THE System SHALL create a Python virtual environment automatically
3. THE System SHALL install all dependencies from requirements.txt
4. THE System SHALL seed the database with 180 curated questions
5. THE System SHALL provide .env.example with all required environment variables
6. THE System SHALL serve frontend static files through FastAPI
7. THE System SHALL run on http://localhost:8000 by default
8. THE System SHALL provide make dev command for development mode with auto-reload
