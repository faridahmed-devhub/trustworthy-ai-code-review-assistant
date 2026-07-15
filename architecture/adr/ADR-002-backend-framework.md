# ADR-002: Backend Framework Selection

## Status

Accepted

## Date

2026-07-15

## Decision

Use **FastAPI** as the backend framework for the **Trustworthy AI Code Review Assistant**.

---

# Context

The Trustworthy AI Code Review Assistant requires a backend service responsible for:

* REST API development
* User authentication
* Project management
* Repository processing
* Static analysis orchestration
* AI review workflow management
* Trust evaluation execution
* Report generation

The backend framework must support:

* High performance
* Asynchronous processing
* Machine Learning and AI integration
* API documentation
* Type safety
* Research experimentation

---

# Decision Drivers

The following factors influenced the decision:

## Performance

The system handles:

* Repository scanning
* Background analysis jobs
* AI model requests
* Multiple concurrent users

A high-performance asynchronous framework is required.

---

## Python Ecosystem

The project heavily depends on Python-based technologies:

* Machine Learning
* LLM frameworks
* Static analysis tools
* Data processing libraries

Using a Python-native framework provides better ecosystem compatibility.

---

## API Development

The backend requires:

* REST APIs
* OpenAPI documentation
* Request validation
* Schema management

---

## Developer Productivity

The framework should provide:

* Fast development
* Clear code structure
* Easy testing
* Maintainability

---

# Alternatives Considered

## Option 1: Django

### Advantages

* Mature framework
* Built-in ORM
* Authentication support
* Large ecosystem

### Disadvantages

* Heavier architecture
* Less optimized for API-first systems
* More overhead for AI service development

Decision:

Rejected because the project requires a lightweight AI service-oriented backend.

---

## Option 2: Flask

### Advantages

* Simple
* Flexible
* Large community

### Disadvantages

* Requires additional libraries for:

  * Validation
  * Documentation
  * Authentication
  * Async support

Decision:

Rejected because more manual configuration would be required.

---

## Option 3: Node.js / Express

### Advantages

* Good API performance
* Large ecosystem

### Disadvantages:

* Less suitable for Python-based AI/ML ecosystem
* Additional service integration complexity

Decision:

Rejected because AI and research components are primarily Python-based.

---

# Why FastAPI Was Selected

FastAPI provides:

## Async Support

Useful for:

* Repository processing
* External AI API calls
* Background tasks

---

## Automatic Documentation

Provides:

* Swagger UI
* OpenAPI schema

---

## Type Validation

Using:

* Python type hints
* Pydantic models

Benefits:

* Fewer runtime errors
* Better maintainability

---

## AI/ML Integration

Native compatibility with:

* PyTorch
* Scikit-learn
* LangChain
* OpenAI SDK
* Transformers

---

# Architecture Impact

Selecting FastAPI influences the system architecture:

```text
Frontend (Next.js)

        |

        ▼

FastAPI Backend

        |

 ┌──────┼────────┐

 ▼      ▼        ▼

Database  AI Engine  Analysis Engine
```

---

# Consequences

## Positive Consequences

* High-performance API layer
* Excellent AI ecosystem compatibility
* Automatic API documentation
* Easy testing
* Modern Python architecture

---

## Negative Consequences

* Requires external solutions for:

  * Background tasks
  * Admin interface
  * Full ORM features

These are addressed using:

* Celery
* Redis
* SQLAlchemy
* PostgreSQL

---

# Implementation Details

Selected stack:

| Component         | Technology       |
| ----------------- | ---------------- |
| Backend Framework | FastAPI          |
| Language          | Python           |
| ORM               | SQLAlchemy       |
| Validation        | Pydantic         |
| Server            | Uvicorn/Gunicorn |
| Task Queue        | Celery + Redis   |

---

# Future Considerations

The backend architecture allows future migration to:

* Microservices
* Kubernetes deployment
* Distributed AI workers
* Enterprise API gateway

---

# Conclusion

FastAPI was selected as the backend framework because it provides the performance, flexibility, and Python ecosystem compatibility required for building a scalable and research-oriented Trustworthy AI Software Engineering platform.
