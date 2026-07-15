# API Architecture

## Overview

This document describes the API architecture of the **Trustworthy AI Code Review Assistant**.

The API layer provides communication between the frontend dashboard, backend services, static analysis engine, AI review engine, and trust evaluation components.

The API is designed using RESTful principles with FastAPI as the backend framework.

---

# API Design Goals

The API architecture focuses on:

* Clear resource-based design
* Secure communication
* Scalability
* Asynchronous processing
* Easy integration
* Research experiment support
* Reproducibility

---

# Technology Stack

| Component             | Technology        |
| --------------------- | ----------------- |
| API Framework         | FastAPI           |
| Language              | Python            |
| Authentication        | JWT               |
| Database ORM          | SQLAlchemy        |
| Validation            | Pydantic          |
| API Documentation     | OpenAPI / Swagger |
| Background Processing | Celery + Redis    |

---

# High-Level API Flow

```text
Developer
    |
    |
Next.js Dashboard
    |
    |
FastAPI Backend
    |
    ├── Project Management API
    |
    ├── Repository Scanner API
    |
    ├── Static Analysis API
    |
    ├── AI Review API
    |
    ├── Trust Evaluation API
    |
    └── Report API
```

---

# API Modules

## 1. Authentication API

Responsible for:

* User registration
* Login
* Token management
* Access control

Endpoints:

```
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/refresh
GET    /api/v1/auth/profile
```

---

# 2. Project Management API

Manage code review projects.

Endpoints:

```
POST   /api/v1/projects

GET    /api/v1/projects

GET    /api/v1/projects/{project_id}

PUT    /api/v1/projects/{project_id}

DELETE /api/v1/projects/{project_id}
```

Example:

```json
{
  "name": "FastAPI Enterprise Project",
  "repository_url": "https://github.com/example/project",
  "language": "Python"
}
```

---

# 3. Repository Scanner API

Responsible for:

* Git repository cloning
* Source file detection
* Language identification

Endpoints:

```
POST /api/v1/scanner/start

GET  /api/v1/scanner/status/{job_id}
```

Request:

```json
{
  "repository_url": "github_repository_url",
  "branch": "main"
}
```

Response:

```json
{
  "job_id": "scan_001",
  "status": "started"
}
```

---

# 4. Static Analysis API

Integrates:

* Ruff
* Bandit
* Semgrep
* Radon
* AST Analyzer

Endpoints:

```
POST /api/v1/analysis/static

GET  /api/v1/analysis/static/{analysis_id}
```

Output:

```json
{
  "bugs": 5,
  "security_issues": 2,
  "complexity_score": 78
}
```

---

# 5. AI Code Review API

Responsible for LLM-based analysis.

Features:

* Code explanation
* Bug detection
* Security suggestions
* Refactoring recommendations

Endpoints:

```
POST /api/v1/review/start

GET  /api/v1/review/{review_id}
```

Request:

```json
{
  "project_id": 1,
  "llm_provider": "openai"
}
```

---

# 6. Trust Evaluation API

Evaluates AI output quality.

Metrics:

* Correctness Score
* Security Score
* Maintainability Score
* Edge Case Coverage
* Confidence Score
* Hallucination Detection

Endpoints:

```
POST /api/v1/trust/evaluate

GET  /api/v1/trust/{evaluation_id}
```

Response:

```json
{
  "correctness": 92,
  "security": 88,
  "maintainability": 81,
  "confidence": 85,
  "overall_score": 86
}
```

---

# 7. Report API

Generates analysis reports.

Formats:

* JSON
* PDF
* HTML

Endpoints:

```
GET /api/v1/reports/{report_id}

GET /api/v1/reports/{report_id}/download
```

---

# API Versioning

The API uses version-based routing.

Example:

```
/api/v1/
```

Future versions:

```
/api/v2/
```

This allows backward compatibility.

---

# Authentication Architecture

Authentication flow:

```text
User Login

      |
      ▼

FastAPI Authentication Service

      |
      ▼

JWT Access Token

      |
      ▼

Protected API Resources
```

Security mechanisms:

* JWT Token
* Password hashing
* Role-based access control
* HTTPS

---

# Error Handling

Standard error format:

```json
{
  "error": "Validation Error",
  "message": "Invalid repository URL",
  "status_code": 400
}
```

---

# Background Processing

Long-running tasks are handled asynchronously.

Examples:

* Repository scanning
* Static analysis
* LLM review
* Report generation

Flow:

```text
API Request

      |
      ▼

Celery Task Queue

      |
      ▼

Worker Process

      |
      ▼

Database Update
```

---

# API Documentation

Automatic documentation:

Swagger:

```
/docs
```

OpenAPI:

```
/openapi.json
```

---

# Future API Extensions

Future support:

* GraphQL API
* WebSocket live analysis updates
* GitHub App integration
* CI/CD integration
* IDE plugins

---

# Conclusion

The API architecture provides a scalable and secure communication layer between users, software analysis components, AI models, and trust evaluation modules. The design supports both production deployment and research experimentation.
