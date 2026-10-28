# ✈️ AI Travel Planner

An AI-powered travel planning web application that generates personalized day-by-day travel itineraries based on a user's destination, trip duration, budget, number of travelers, and interests.

The application combines **FastAPI, MySQL, SQLAlchemy, JWT authentication, LangChain, and Groq LLMs** to provide a secure backend with AI-powered itinerary generation and trip management.

---

## 📌 Overview

Planning a trip manually can require significant time to research destinations, attractions, food, transportation, and budget allocation.

**AI Travel Planner** simplifies this process by allowing authenticated users to provide their travel preferences and receive an AI-generated itinerary organized by day and time.

The system also provides a backend for managing user accounts and saved trip information through REST APIs.

### Core workflow

```text
User
  │
  ▼
Web Interface
  │
  ▼
FastAPI Backend
  │
  ├───────────────┐
  ▼               ▼
Authentication    Trip Management
  │               │
  ▼               ▼
JWT + MySQL      SQLAlchemy + MySQL
  │
  ▼
AI Travel Planner
  │
  ▼
LangChain + Groq LLM
  │
  ▼
Personalized Itinerary
```

---

## 🎯 Problem Statement

Traditional travel planning often requires users to manually research:

- Tourist attractions
- Daily activities
- Food recommendations
- Transportation options
- Trip duration
- Budget allocation
- Personal interests

This application automates the initial itinerary-planning process by using an LLM to transform structured travel requirements into a practical day-by-day travel plan.

---

## 💡 Solution

The application accepts the user's travel requirements:

- Destination
- Number of days
- Budget
- Number of travelers
- Interests

These inputs are passed to an AI service, where a structured travel prompt is constructed and sent to a Groq-hosted LLM through LangChain.

The generated response contains:

- Day-by-day activities
- Morning, afternoon, and evening plans
- Tourist attractions
- Food recommendations
- Transportation suggestions
- Estimated daily budget

The prompt also instructs the model to keep the estimated total cost within the user's specified budget.

---

# 🚀 Key Features

## 🔐 1. User Authentication

The application provides a complete authentication workflow:

- User registration
- User login
- Password hashing
- JWT access-token generation
- Protected API endpoints
- Current-user retrieval
- Token validation
- Token expiration

Passwords are stored as bcrypt hashes rather than plain text.

---

## 🤖 2. AI-Powered Itinerary Generation

Users can generate personalized itineraries by providing:

```text
Destination
Number of Days
Budget
Number of Travelers
Interests
```

The AI service constructs a dedicated travel-planning prompt and invokes the configured Groq LLM through LangChain's `ChatGroq` integration.

---

## 🗓️ 3. Trip Management

Authenticated users can manage their trips through REST APIs.

Supported operations include:

- Create a trip
- View all personal trips
- View a specific trip
- Update a trip
- Delete a trip

Trip records are associated with the authenticated user, preventing users from accessing another user's trips through the service-layer ownership checks.

---

## 💾 4. MySQL Database

MySQL is used for persistent application data.

The application uses **SQLAlchemy ORM** as the database abstraction layer between Python and MySQL.

Current database entities include:

### Users

Stores:

- User ID
- Name
- Email
- Hashed password

### Trips

Stores:

- Trip ID
- Title
- Destination
- Start date
- End date
- Budget
- Number of travelers
- Transportation
- Accommodation
- Preferences
- Status
- Itinerary
- User ID
- Created timestamp
- Updated timestamp

The `User` and `Trip` models have a relationship in SQLAlchemy, with trips associated with their owning user.

---

## 🔑 5. JWT-Based Authorization

Protected endpoints use Bearer-token authentication.

The authentication flow is:

```text
User
  │
  ▼
Login
  │
  ▼
Verify email + password
  │
  ▼
Generate JWT
  │
  ▼
Client receives access token
  │
  ▼
Client sends Bearer token
  │
  ▼
FastAPI verifies JWT
  │
  ▼
Identify current user
  │
  ▼
Access protected resource
```

FastAPI's `OAuth2PasswordBearer` is used for extracting the bearer token, while the JWT utility creates and verifies access tokens.

---

# 🧠 AI Architecture

The AI generation pipeline is intentionally separated from the API layer.

```text
Travel Request
      │
      ▼
AI Router
      │
      ▼
AIService
      │
      ▼
Travel Prompt Builder
      │
      ▼
LangChain ChatGroq
      │
      ▼
Groq LLM
      │
      ▼
Generated Itinerary
      │
      ▼
FastAPI Response
```

The `AIService` class encapsulates the LLM-related functionality, while the travel prompt is maintained separately in the prompts module.

---

# 📝 AI Prompt Design

The travel prompt instructs the LLM to behave as an expert AI Travel Planner.

The generated itinerary is required to include:

- Day-by-day planning
- Morning activities
- Afternoon activities
- Evening activities
- Tourist attractions
- Food recommendations
- Transportation
- Estimated daily budget

The prompt also instructs the model to stay within the user's budget and return the result in Markdown format.

---

# 🏗️ Application Architecture

The project follows a layered backend architecture:

```text
Frontend
   │
   ▼
FastAPI Routers
   │
   ├───────────────┐
   │               │
   ▼               ▼
Schemas         Dependencies
   │               │
   ▼               ▼
Services       Authentication
   │               │
   ├───────────────┤
   │
   ├── SQLAlchemy → MySQL
   │
   └── AIService → LangChain → Groq
```

### Router Layer

Responsible for:

- Receiving HTTP requests
- Validating request data
- Calling appropriate services
- Returning API responses

### Schema Layer

Pydantic models are used for:

- Request validation
- Response validation
- Authentication data
- Trip data
- AI request/response structures

### Service Layer

Contains application/business logic.

Current services include:

- `AuthService`
- `TripService`
- `AIService`

### Model Layer

Contains SQLAlchemy ORM models representing database entities.

### Utility Layer

Contains reusable functionality such as:

- Password hashing
- Password verification
- JWT creation
- JWT verification

This separation keeps the application modular and easier to maintain.

---

# 📁 Project Structure

```text
travel-agent-users/
│
├── app/
│   │
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── trip.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── trip.py
│   │   └── ai.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── trips.py
│   │   └── ai.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── trip_service.py
│   │   └── ai_service.py
│   │
│   ├── prompts/
│   │   └── travel_prompt.py
│   │
│   ├── utils/
│   │   ├── security.py
│   │   └── jwt.py
│   │
│   ├── templates/
│   │
│   └── static/
│
├── test_groq.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| API Style | REST API |
| Database | MySQL |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Authentication | JWT |
| Password Hashing | bcrypt / Passlib |
| LLM Framework | LangChain |
| LLM Provider | Groq |
| LLM Integration | ChatGroq |
| Templating | Jinja2 |
| Server | Uvicorn |
| Configuration | python-dotenv |
| API Documentation | FastAPI / Swagger UI |

The repository's current dependency file confirms the FastAPI, SQLAlchemy, MySQL driver, LangChain, LangChain-Groq, Groq, JWT, Passlib, bcrypt, Uvicorn, Jinja2, and dotenv dependencies.

---

# 🔌 REST API

The backend exposes three main API areas.

## Authentication

### Register

```http
POST /auth/signup
```

Creates a new user account.

### Login

```http
POST /auth/login
```

Authenticates a user and returns a JWT access token.

### Current User

```http
GET /auth/me
```

Returns information about the currently authenticated user.

---

## Trips

### Create Trip

```http
POST /trips/
```

Creates a trip for the authenticated user.

### Get All Trips

```http
GET /trips/
```

Returns the authenticated user's trips.

### Get Trip

```http
GET /trips/{trip_id}
```

Returns a specific trip belonging to the authenticated user.

### Update Trip

```http
PUT /trips/{trip_id}
```

Updates an existing trip.

### Delete Trip

```http
DELETE /trips/{trip_id}
```

Deletes an existing trip.

The trip router implements these CRUD operations and applies the current-user dependency to the endpoints.

---

## AI

### Generate Itinerary

```http
POST /ai/generate
```

Generates an AI-powered itinerary using:

```text
destination
days
budget
travelers
interests
```

The endpoint requires authentication and passes the request to `AIService`.

---

# 🔄 Complete Application Workflow

## 1. User Registration

```text
User enters name, email and password
              ↓
       POST /auth/signup
              ↓
       Validate request
              ↓
      Hash the password
              ↓
       Store user in MySQL
              ↓
       Return user details
```

---

## 2. User Login

```text
User enters email + password
              ↓
       POST /auth/login
              ↓
     Find user in database
              ↓
     Verify password hash
              ↓
       Generate JWT
              ↓
       Return access token
```

---

## 3. Trip Management

```text
Authenticated Request
        ↓
    JWT Validation
        ↓
    Current User
        ↓
    Trip Router
        ↓
    Trip Service
        ↓
   SQLAlchemy ORM
        ↓
      MySQL
```

---

## 4. AI Itinerary Generation

```text
User Travel Preferences
          ↓
     POST /ai/generate
          ↓
      AI Router
          ↓
       AIService
          ↓
   Build Travel Prompt
          ↓
     ChatGroq / LLM
          ↓
  Generate Itinerary
          ↓
   AITripResponse
          ↓
      Frontend
```

---

# 🔐 Security

The application implements several basic security mechanisms.

### Password Hashing

Passwords are hashed
