# ADR-006: API Design and Communication Architecture

## Status

Accepted


## Date

2026-07-14


## Context

The Trustworthy AI Code Review Assistant contains multiple components:

- Next.js frontend
- FastAPI backend
- Repository scanner
- Static analysis engine
- AI review engine
- Trust evaluation layer
- Database services

These components require a well-defined communication interface.

A poorly designed API can make the system difficult to maintain, test, and extend.


## Decision

We will use a RESTful API architecture based on:

- FastAPI
- OpenAPI specification
- JSON-based communication
- Versioned API endpoints


## API Architecture
Frontend (Next.js)

    |
    |
    ↓

FastAPI Backend

    |
    |
    ├── Project Service
    |
    ├── Repository Service
    |
    ├── Analysis Service
    |
    ├── AI Review Service
    |
    └── Report Service


## API Versioning

All APIs will use version prefixes.

Example:


/api/v1/



Example endpoints:


POST /api/v1/projects

GET /api/v1/projects/{id}

POST /api/v1/analysis/start

GET /api/v1/analysis/{job_id}

GET /api/v1/reports/{id}

GET /api/v1/trust-score/{id}



## Authentication

The API will support:

- JWT authentication
- Role-based access control
- Secure token handling


Example:


Authorization:
Bearer <token>



## Request Flow



User

↓

Next.js Dashboard

↓

FastAPI API

↓

Analysis Pipeline

↓

AI Engine

↓

Trust Evaluation

↓

Response JSON



## Response Design

All APIs will return standardized JSON responses.


Example:

```json
{
    "success": true,
    "data": {
        "project_id": "123",
        "status": "completed"
    },
    "message": "Analysis completed"
}
Error Handling

The API will use standard HTTP status codes.

Examples:

200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error