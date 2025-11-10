# Hintify - AI-Powered Learning Platform Requirements

## Introduction

Hintify is an AI-powered learning platform that provides interactive multiple-choice tests across four subjects (Technology, Science, Geography, General Knowledge) with three difficulty levels each. The system features AI-generated hints, instant feedback, progress tracking, file upload for custom question generation, and a premium glassmorphism UI with live animated backgrounds.

## Glossary

- **System**: The Hintify web application
- **User**: A person using the platform to take tests and learn
- **Question**: A multiple-choice question with 4 options, one correct answer, a hint, and an explanation
- **Subject**: A category of questions (Technology, Science, Geography, or General Knowledge)
- **Difficulty Level**: Easy, Medium, or Hard classification of questions
- **Test Session**: A single instance of a user taking questions from a specific subject and difficulty
- **Curated Questions**: The 180 pre-loaded questions (45 per subject)
- **Uploaded Questions**: Questions generated from user-uploaded documents
- **Glassmorphism**: A UI design style using transparent, blurred glass-like containers

## Requirements

### Requirement 1: Question Management System

**User Story:** As a user, I want to access a comprehensive question bank organized by subject and difficulty, so that I can learn at my appropriate skill level.

#### Acceptance Criteria

1. THE System SHALL store exactly 180 curated questions in the database
2. THE System SHALL organize questions into 4 subjects with exactly 45 questions per subject
3. THE System SHALL categorize each subject's questions into 3 difficulty levels with exactly 15 questions per level
4. WHEN a user requests questions for a specific subject and difficulty, THE System SHALL return only questions matching both criteria
5. THE System SHALL ensure each question includes question text, 4 options, correct answer index, hint text, and explanation text

### Requirement 2: Test Taking Interface

**User Story:** As a user, I want to take interactive tests with immediate feedback and navigation controls, so that I can learn effectively and track my progress.

#### Acceptance Criteria

1. WHEN a user selects a subject and difficulty, THE System SHALL load exactly 15 questions for that combination
2. THE System SHALL display one question at a time with 4 clearly labeled options (A, B, C, D)
3. WHEN a user selects an answer, THE System SHALL provide immediate visual feedback indicating correct (green) or incorrect (red)
4. WHEN a user selects an answer, THE System SHALL display the explanation text before allowing navigation to the next question
5. THE System SHALL provide a question navigation grid showing all 15 question numbers with visual indicators for current, answered correctly, and answered incorrectly
6. THE System SHALL allow users to jump to any question by clicking its number in the navigation grid
7. THE System SHALL provide Previous and Next navigation buttons
8. THE System SHALL provide a "Get Hint" button that displays the hint text for the current question
9. THE System SHALL provide a "Submit Test" button that calculates and displays final results
10. WHEN a user switches difficulty levels during a test, THE System SHALL load questions for the same subject with the new difficulty level

### Requirement 3: Results and Analytics

**User Story:** As a user, I want to see detailed results and analytics after completing a test, so that I can understand my performance and track my learning progress.

#### Acceptance Criteria

1. WHEN a user clicks "Submit Test", THE System SHALL calculate total questions, correct answers, incorrect answers, and unanswered questions
2. THE System SHALL calculate accuracy as (correct answers / answered questions) × 100
3. THE System SHALL display results in a dedicated results screen with visual cards for each metric
4. THE System SHALL display accuracy percentage prominently with a visual progress bar
5. THE System SHALL provide options to return to subject selection or take another test
6. THE System SHALL display analytics charts including performance by subject, difficulty distribution, and accuracy trends

### Requirement 4: File Upload and Question Generation

**User Story:** As a user, I want to upload my own documents and have questions generated from them, so that I can create custom learning content.

#### Acceptance Criteria

1. THE System SHALL accept file uploads in PDF, DOCX, and PPTX formats
2. THE System SHALL validate file size to be maximum 10MB
3. WHEN a user uploads a valid document, THE System SHALL generate exactly 45 questions (15 easy, 15 medium, 15 hard)
4. THE System SHALL store uploaded questions separately from curated questions with a source document reference
5. THE System SHALL display uploaded questions only in the "My Questions" section, not in regular tests
6. THE System SHALL provide a dedicated interface for viewing and testing uploaded questions grouped by source document

### Requirement 5: User Interface and Experience

**User Story:** As a user, I want a beautiful, modern interface with smooth animations and intuitive navigation, so that learning is enjoyable and engaging.

#### Acceptance Criteria

1. THE System SHALL implement a glassmorphism design with transparent containers, backdrop blur effects, and subtle borders
2. THE System SHALL provide a live animated background with floating particles and wave effects
3. THE System SHALL support theme switching between Dark and Light modes with smooth transitions
4. THE System SHALL use a premium color palette with primary (#667eea), secondary (#764ba2), success (#10b981), error (#ef4444), and warning (#f59e0b) colors
5. THE System SHALL provide smooth animations for all interactions with transitions under 300ms
6. THE System SHALL be fully responsive and work on mobile, tablet, and desktop devices
7. THE System SHALL include navigation between Home, Take Test, Upload Files, My Questions, and Analytics sections

### Requirement 6: State Management and Data Integrity

**User Story:** As a user, I want the application to maintain correct state when I navigate between sections and switch difficulties, so that I always see the appropriate content.

#### Acceptance Criteria

1. WHEN a user switches between subjects, THE System SHALL clear all previous question data before loading new questions
2. WHEN a user switches difficulty levels, THE System SHALL maintain the current subject and load questions for that subject with the new difficulty
3. THE System SHALL store current subject ID, difficulty level, question index, and user answers in application state
4. THE System SHALL preserve user progress when switching difficulties within the same test session
5. THE System SHALL reset all state variables (currentQuestions, currentIndex, userAnswers) when starting a new test

### Requirement 7: Backend API

**User Story:** As a developer, I want a well-structured REST API that serves questions and handles uploads, so that the frontend can reliably access data.

#### Acceptance Criteria

1. THE System SHALL provide a GET endpoint at /api/subjects/ that returns all subjects with their metadata
2. THE System SHALL provide a GET endpoint at /api/questions/ that accepts subject_id and difficulty parameters and returns matching questions
3. THE System SHALL provide a GET endpoint at /api/questions/{id}/hint that returns the hint for a specific question
4. THE System SHALL provide a GET endpoint at /api/questions/uploaded that returns only questions with source_document references
5. THE System SHALL provide a POST endpoint at /api/upload/ that accepts file uploads and generates questions
6. THE System SHALL return questions in JSON format with id, question_text, difficulty, options array, correct_answer index, and explanation
7. THE System SHALL handle errors gracefully and return appropriate HTTP status codes

### Requirement 8: Database Schema

**User Story:** As a developer, I want a properly structured database schema that maintains data integrity, so that questions and relationships are stored correctly.

#### Acceptance Criteria

1. THE System SHALL implement a subjects table with id, name, description, icon, color, and is_active fields
2. THE System SHALL implement a questions table with id, subject_id, question_text, difficulty, source_document, and is_active fields
3. THE System SHALL implement a choices table with id, question_id, choice_text, is_correct, and letter fields
4. THE System SHALL implement a hints table with id, question_id, and hint_text fields
5. THE System SHALL enforce foreign key relationships between questions and subjects, choices and questions, and hints and questions
6. THE System SHALL use an enum for difficulty levels with values EASY, MEDIUM, HARD
