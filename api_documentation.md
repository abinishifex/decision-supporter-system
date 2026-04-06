# Decision Supporter System - API Documentation

Base URL: `http://localhost:8000/api/v1` (Update for Production)

---

## 1. Authentication Endpoints

### 1.1 Register User
- **Endpoint**: `POST /auth/register/`
- **Description**: Creates a new user account and sends a verification email.
- **Request Body**:
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "SecurePassword123!"
}
```
- **Response** `201 Created`:
```json
{
  "message": "User created successfully. Please check your email to verify your account."
}
```

### 1.2 Login User
- **Endpoint**: `POST /auth/login/`
- **Description**: Authenticates a user and returns a JWT access and refresh token.
- **Request Body**:
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!"
}
```
- **Response** `200 OK`:
```json
{
  "access": "eyJ...",
  "refresh": "eyJ..."
}
```

### 1.3 Get Current User Profile
- **Endpoint**: `GET /auth/me/`
- **Headers**: `Authorization: Bearer <access_token>`
- **Description**: Returns the currently authenticated user's profile.
- **Response** `200 OK`:
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "is_verified": true
}
```

---

## 2. Gemini AI Decision Engine Endpoints

These endpoints power the multi-step dynamic decisioning wizard. 

### 2.1 Initiate Decision (Step 1)
- **Endpoint**: `POST /decisions/decisions/initiate/`
- **Headers**: `Authorization: Bearer <access_token>` (Optional but recommended so history is saved).
- **Description**: The user submits their problem and options. The Gemini AI generates custom investigative questions.
- **Request Body**:
```json
{
  "problem": "I want to start a side-hustle but don't know what to choose inside Ethiopia.",
  "options": [
    "Freelance coding",
    "Selling clothes on Telegram",
    "Starting a YouTube channel"
  ],
  "category_id": 3
}
```
- **Response** `201 Created`:
```json
{
  "session_id": 42,
  "category": "Business",
  "questions": [
    {
      "id": 1,
      "text": "Which option is more feasible to fund through Iqub or family contributions?",
      "options": [
        { "label": "Freelance coding", "value": "A" },
        { "label": "Selling clothes on Telegram", "value": "B" },
        { "label": "Starting a YouTube channel", "value": "C" }
      ]
    }
  ]
}
```

### 2.2 Evaluate Decision (Step 2)
- **Endpoint**: `POST /decisions/decisions/evaluate/`
- **Headers**: `Authorization: Bearer <access_token>` (Optional).
- **Description**: The user submits their answers to the generated questions. The Gemini AI evaluates the answers and returns rankings, pros, cons, and a winner.
- **Request Body**:
```json
{
  "session_id": 42,
  "answers": {
    "1": "B",
    "2": "A",
    "3": "A",
    "4": "C",
    "5": "A"
  }
}
```
- **Response** `200 OK`:
```json
{
  "id": 42,
  "problem": "I want to start a side-hustle but don't know what to choose inside Ethiopia.",
  "options": ["Freelance coding", "Selling clothes on Telegram", "Starting a YouTube channel"],
  "dynamic_questions": [...],
  "answers": {"1": "B", "2": "A", ...},
  "results": [
    { "name": "Freelance coding", "score": 85 },
    { "name": "Selling clothes on Telegram", "score": 60 },
    { "name": "Starting a YouTube channel", "score": 40 }
  ],
  "recommendation": "Freelance coding",
  "analysis_summary": "Based on the investigative survey...",
  "analysis_pros": "Low capital requirement, high foreign currency potential.",
  "analysis_cons": "Requires reliable internet connectivity and a laptop.",
  "status": "completed",
  "created_at": "2026-04-06T10:00:00Z"
}
```

### 2.3 Retrieve Decision History
- **Endpoint**: `GET /decisions/decisions/`
- **Headers**: `Authorization: Bearer <access_token>` **(Required)**
- **Description**: Fetches all past completed decision sessions for the currently logged-in user.
- **Response** `200 OK`: Returns an array of completed Session objects (matching the `2.2 Evaluate` payload).

---

## 3. Legacy Categories Endpoint
*(Used if you want to hardcode fallback categories on the frontend instead of completely relying on AI strings).*

### 3.1 List Categories
- **Endpoint**: `GET /decisions/categories/`
- **Description**: Returns all configured local categories (e.g., Business, Health, Relationships).

---

## 4. Swagger UI Documentation
A fully interactive documentation portal is available locally.
Visit: `http://localhost:8000/api/docs/` in your browser.
