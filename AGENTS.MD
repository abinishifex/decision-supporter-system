# AGENTS.MD

## Project Overview

This repository is a two-part application:

- Frontend: a Vite + React single-page application in `frontend/`
- Backend: a Django API in `backend/`

The product is a guided decision-support system. A user enters a problem, adds options, chooses a category, answers a fixed set of category questions for every option, and submits the full payload to Django. Django validates the payload, scores each option, stores the decision session in SQLite, and returns ranked results plus a short analysis string.

## High-Level Architecture

### Frontend

The frontend is responsible for presentation, navigation, local form state, and assembling the payload sent to the backend.

Primary responsibilities:

- Render the marketing pages and the multi-step decision flow
- Hold the list of decision categories and question sets
- Capture user input for problem statement, options, category selection, and answers
- Submit decision and chatbot requests to the Django API
- Render the saved decision result returned by the backend

Main files:

- `frontend/src/main.jsx`: mounts the React app
- `frontend/src/App.jsx`: top-level router and shared layout
- `frontend/src/pages/Home.jsx`: landing page
- `frontend/src/pages/About.jsx`: product description page
- `frontend/src/pages/Decision.jsx`: multi-step decision workflow
- `frontend/src/lib/api.js`: fetch wrapper for backend API calls
- `frontend/src/utils/questionGenerator.js`: static category and question definitions
- `frontend/src/components/*.jsx`: reusable UI pieces for options, questions, results, navbar, footer, hero, chatbot

### Backend

The backend is responsible for API routing, validation, decision scoring, session persistence, and the rule-based chatbot response.

Primary responsibilities:

- Expose REST-style endpoints under `/api/`
- Validate the decision payload received from the frontend
- Compute scores, rankings, percentages, and summary analysis
- Persist completed decision sessions in SQLite
- Return canned chatbot responses based on keyword matching

Main files:

- `backend/manage.py`: Django entry point
- `backend/config/settings.py`: Django settings, SQLite, CORS, env-driven config
- `backend/config/urls.py`: mounts API routes at `/api/`
- `backend/decisioning/urls.py`: decisioning endpoint map
- `backend/decisioning/views.py`: request handlers
- `backend/decisioning/services.py`: validation and scoring logic
- `backend/decisioning/models.py`: `DecisionSession` persistence model
- `backend/decisioning/migrations/0001_initial.py`: initial schema for the decision session table

## Frontend Classification

### Routing and Layout

- `frontend/src/App.jsx` uses `react-router-dom` to expose:
  - `/`
  - `/about`
  - `/decision`
- `Navbar`, `Footer`, and `Chatbot` are rendered globally around the routed page content.

### Decision Workflow

The real user flow lives in `frontend/src/pages/Decision.jsx`.

State owned by this page:

- `step`
- `problem`
- `options`
- `selectedCategory`
- `answers`
- `results`
- `analysis`
- `maxScore`
- `decisionId`
- `error`
- `isSubmitting`

Step breakdown:

1. Step 1 collects the problem statement and option names.
2. Step 2 asks the user to choose a category.
3. Step 3 renders every question for every option and records numeric answers.
4. Step 4 shows the ranked result list returned by the backend.

Important implementation detail:

- The frontend does not generate questions dynamically at runtime.
- It imports a fixed `categories` array from `frontend/src/utils/questionGenerator.js`.
- The selected category object, including all questions and answer values, is sent to the backend as part of the request payload.

### API Client

`frontend/src/lib/api.js` provides two calls:

- `evaluateDecision(payload)` -> `POST /api/decisions/evaluate/`
- `sendChatMessage(message)` -> `POST /api/chat/`

`VITE_API_BASE_URL` defaults to `http://localhost:8000/api`.

### UI Components

- `OptionInput.jsx`: collects option names and supports add/remove
- `QuestionCard.jsx`: renders selectable answers per question
- `ResultCard.jsx`: renders a score card with progress bar
- `Chatbot.jsx`: floating assistant widget bound to `/api/chat/`
- `HeroSection.jsx`, `FeatureCard.jsx`, `Navbar.jsx`, `Footer.jsx`: presentation-only components

## Backend Classification

### URL Surface

The backend exposes these endpoints:

- `GET /api/health/`
- `POST /api/decisions/evaluate/`
- `GET /api/decisions/<id>/`
- `POST /api/chat/`

### Request Handling

`backend/decisioning/views.py` contains four handlers:

- `health_view`
  - simple health response
- `evaluate_view`
  - parses JSON
  - validates and normalizes the payload
  - computes recommendation data
  - saves a `DecisionSession`
  - returns the evaluation response plus `decisionId`
- `decision_detail_view`
  - loads a saved decision session by primary key
  - returns the stored payload and result data
- `chat_view`
  - validates `message`
  - returns a rule-based reply from `build_chat_response`

### Business Logic

`backend/decisioning/services.py` is the core backend domain module.

Key functions:

- `validate_category(category)`
  - checks category shape, id/name presence, and question/option structure
- `validate_decision_payload(payload)`
  - checks the problem text
  - requires at least two options
  - validates every answer against the allowed values in the submitted category
  - normalizes keys to strings
- `build_strengths(category, option_answers)`
  - maps numeric answers back to their question labels
- `evaluate_decision(problem, category, options, answers)`
  - computes `maxScore`
  - sums answer values per option
  - computes ranking and percentages
  - returns the recommended option and top strengths
- `build_analysis(problem, category, ranked_results)`
  - creates a short natural-language summary
- `build_chat_response(message)`
  - keyword-based helper replies, not model-backed AI

### Persistence

`backend/decisioning/models.py` defines `DecisionSession`.

Stored fields:

- `problem`
- `category_id`
- `category_name`
- `category_payload`
- `options`
- `answers`
- `results`
- `recommendation`
- `analysis`
- `created_at`

Storage characteristics:

- Uses SQLite through Django’s default database config
- Stores most structured content in `JSONField`
- Orders sessions newest-first via model `Meta.ordering`

## Runtime Flow

### Decision Evaluation Flow

1. The user navigates to `/decision`.
2. React collects the problem text and candidate options.
3. React shows a static category list from `frontend/src/utils/questionGenerator.js`.
4. The user selects one category.
5. React renders that category’s questions for each option.
6. React builds a payload containing:
   - `problem`
   - `options`
   - `category`
   - `answers`
7. React sends the payload to `POST /api/decisions/evaluate/`.
8. Django validates the payload in `validate_decision_payload`.
9. Django scores each option in `evaluate_decision`.
10. Django persists the result in `DecisionSession`.
11. Django returns:
   - ranked `results`
   - `analysis`
   - `maxScore`
   - `recommendedOption`
   - `decisionId`
12. React renders the recommendation and score cards.

### Chat Flow

1. The user opens the floating chatbot.
2. React sends `{ message }` to `POST /api/chat/`.
3. Django routes to `build_chat_response`.
4. A canned text response is returned and appended to chat history in the browser.

## Data Ownership

### Owned by Frontend

- Category catalog
- Question text
- Answer labels and values
- Multi-step wizard state
- Display logic and page content

### Owned by Backend

- Input validation
- Score calculation
- Ranking rules
- Analysis string generation
- Decision session persistence
- Chat reply rules

### Shared Contract

The frontend and backend are coupled through the decision payload shape:

- category ids and question ids
- per-question answer values
- option index mapping inside `answers`

This means backend validation depends on the frontend sending the full category payload consistently.

## Configuration and Startup

### Frontend

Main commands from `frontend/package.json`:

- `cd frontend && npm run dev`
- `cd frontend && npm run build`
- `cd frontend && npm run preview`
- `cd frontend && npm run lint`

Frontend env:

- `VITE_API_BASE_URL`

### Backend

Main commands:

- `python backend/manage.py migrate`
- `python backend/manage.py runserver 8000`

Backend env:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `CORS_ALLOWED_ORIGINS`
- `DJANGO_TIME_ZONE`

## Current Architectural Notes

### Strengths

- Clear split between UI and scoring API
- Backend validates client-submitted decision payloads instead of trusting the browser
- Decision results are persisted and retrievable
- The app is small enough that the flow is easy to trace end-to-end

### Constraints and Tradeoffs

- Question/category definitions live only in the frontend, not in the backend or database
- Backend scoring is tightly coupled to the category payload shape sent by the client
- Chat is heuristic and not connected to any real LLM service
- SQLite is fine for local use but not ideal for concurrent production traffic
- There is no authentication, authorization, or per-user ownership of saved decisions
- There are no automated tests in the repository

### Accuracy Notes About Current Behavior

The implementation currently works like this:

- Category selection is manual, not inferred from the problem text
- Questions are static, not dynamically generated
- The chatbot is rule-based, not AI-generated
- Analysis text is template-built on the backend, not generated by Gemini or another model

## Suggested Next Refactor Boundaries

If the project grows, the cleanest next separations would be:

- Move category/question definitions into the backend or a shared schema module
- Introduce serializers or Django REST Framework for request/response validation
- Add tests around `validate_decision_payload` and `evaluate_decision`
- Add a service layer for decision retrieval history and listing endpoints
- Replace the rule-based chatbot only after deciding whether model usage is actually required
