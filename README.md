
# Decision Supporter System

This project now has:

- a Vite/React frontend in `frontend/`
- a Django backend for decision evaluation, chatbot replies, and saved decision sessions
- SQLite persistence for completed decision runs

## Project Structure

- `frontend/`: React frontend app, Vite config, and frontend dependencies
- `backend/`: Django API and data model

## Run Locally

### Frontend

1. Install Node dependencies:
   `cd frontend && npm install`
2. Copy `frontend/.env.example` to `frontend/.env.local`
3. Set `VITE_API_BASE_URL=http://localhost:8000/api`
4. Start the frontend:
   `cd frontend && npm run dev`

### Backend

1. Install Python 3.12+ if it is not already available
2. Create and activate a virtual environment inside `backend/`
3. Install backend dependencies:
   `pip install -r backend/requirements.txt`
4. Apply migrations:
   `python backend/manage.py migrate`
5. Start Django:
   `python backend/manage.py runserver 8000`

## API Endpoints

- `GET /api/health/`
- `POST /api/decisions/evaluate/`
- `GET /api/decisions/<id>/`
- `POST /api/chat/`

## Notes

- Decision categories and question sets currently live in the frontend and are submitted to Django for server-side validation and scoring.
- Completed decision sessions are saved in SQLite through the `DecisionSession` model.
