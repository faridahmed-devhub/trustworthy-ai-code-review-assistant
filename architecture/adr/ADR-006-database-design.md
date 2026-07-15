# ADR-005: Database Architecture Design

## Status

Accepted


## Date

2026-07-14


## Context

The system needs to store:

- User information
- Software projects
- Repository metadata
- Static analysis results
- AI-generated reviews
- Trust evaluation scores
- Research experiments


A structured storage system is required for both production usage and research analysis.


## Decision

We will use:

Primary Database:

- PostgreSQL


Supporting Storage:

- Redis
- Vector Database


## Database Responsibilities


## PostgreSQL

Stores relational data:

- Users
- Projects
- Repositories
- Analysis Jobs
- Static Reports
- AI Reviews
- Trust Scores
- Experiment Results


## Redis

Used for:

- Background task queue
- Temporary caching
- Celery task management


## Vector Database

Used for:

- Source code embeddings
- Repository knowledge retrieval
- RAG-based AI assistance


## Data Flow
Repository Analysis

    ↓

Processing Pipeline

    ↓

PostgreSQL

    ↓

AI Evaluation

    ↓

Trust Report


## Rationale

PostgreSQL was selected because:

- Reliable relational database
- Strong analytical capability
- Open-source
- Suitable for research experiments


Redis was selected because:

- Fast in-memory processing
- Works well with asynchronous tasks


Vector storage enables:

- Future RAG implementation
- Semantic code search


## Alternatives Considered


### MongoDB

Rejected because:

- Relational relationships are important
- Research metrics require structured queries


### File-based Storage

Rejected because:

- Difficult to manage large experiments
- Poor scalability


## Consequences


Positive:

- Structured data management
- Easy experiment analysis
- Production-ready storage design


Negative:

- Requires database maintenance
- More infrastructure components