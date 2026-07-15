# ADR-009: Background Job Processing Architecture

## Status

Accepted

## Date

2026-07-15

---

# Decision

Implement an asynchronous background job processing system using:

* Celery as task processing framework
* Redis as message broker
* PostgreSQL as result storage

Long-running operations will execute asynchronously through worker processes instead of blocking API requests.

---

# Context

The Trustworthy AI Code Review Assistant performs several computationally expensive operations:

* Repository cloning
* Source code scanning
* Static analysis execution
* LLM-based code review
* Trust score calculation
* Report generation

These operations may take several seconds or minutes depending on repository size and complexity.

Executing these tasks directly inside API requests would cause:

* Long response times
* API timeout issues
* Poor user experience
* Limited scalability

Therefore, a distributed background processing architecture is required.

---

# Problem Statement

The system needs a mechanism to:

* Execute long-running tasks asynchronously
* Support multiple concurrent analysis jobs
* Track job status
* Handle failures and retries
* Scale workers independently

---

# Decision Drivers

## Performance

Users should receive immediate feedback after starting analysis.

Example:

```text
User starts analysis

        |
        ▼

API returns job_id immediately

        |
        ▼

Background worker processes task
```

---

## Scalability

The system should allow adding more workers when workload increases.

Example:

```text
Worker 1
Worker 2
Worker 3
Worker N
```

---

## Reliability

The system should support:

* Retry mechanism
* Error handling
* Task monitoring

---

## AI Processing Requirement

LLM requests are unpredictable in duration and require isolated execution.

---

# Selected Architecture

```text
                 User

                  |
                  ▼

            Next.js Dashboard

                  |
                  ▼

            FastAPI Backend

                  |
                  ▼

          Create Background Task

                  |
                  ▼

             Redis Queue

                  |
        ┌─────────┼─────────┐

        ▼         ▼         ▼

    Worker 1   Worker 2   Worker N

        |
        ▼

 Analysis Pipeline

        |
 ┌──────┼────────┐

 ▼      ▼        ▼

Static  AI    Trust
Analysis Review Evaluation

        |
        ▼

    PostgreSQL
```

---

# Background Tasks

## Repository Scanning

Purpose:

* Clone repository
* Detect files
* Identify programming languages

Task:

```text
scan_repository()
```

---

## Static Analysis

Purpose:

Run:

* Ruff
* Bandit
* Semgrep
* Radon

Task:

```text
run_static_analysis()
```

---

## AI Code Review

Purpose:

* Generate AI recommendations
* Analyze code quality
* Explain issues

Task:

```text
run_ai_review()
```

---

## Trust Evaluation

Purpose:

Calculate:

* Confidence score
* Reliability score
* Hallucination risk

Task:

```text
calculate_trust_score()
```

---

## Report Generation

Purpose:

Generate:

* JSON report
* HTML report
* PDF report

Task:

```text
generate_report()
```

---

# Job Lifecycle

```text
Created

  |
  ▼

Queued

  |
  ▼

Running

  |
  ▼

Completed

  |
  ▼

Stored
```

Failure flow:

```text
Running

  |
  ▼

Failed

  |
  ▼

Retry

  |
  ▼

Completed / Error
```

---

# Task Status Management

Each task maintains:

| Status    | Meaning               |
| --------- | --------------------- |
| Pending   | Waiting in queue      |
| Running   | Worker processing     |
| Completed | Successfully finished |
| Failed    | Error occurred        |
| Cancelled | User cancelled        |

---

# Alternatives Considered

## FastAPI BackgroundTasks

### Advantages

* Built-in
* Simple implementation

### Disadvantages

* Limited scalability
* No distributed workers
* Poor monitoring

Decision:

Rejected for production workloads.

---

## RabbitMQ + Custom Workers

### Advantages

* Enterprise message broker
* High reliability

### Disadvantages

* Additional infrastructure complexity

Decision:

Not selected initially.

---

## Synchronous Processing

### Advantages

* Simple design

### Disadvantages

* Poor performance
* API blocking
* Cannot scale

Decision:

Rejected.

---

# Consequences

## Positive Consequences

* Faster API responses
* Independent worker scaling
* Better reliability
* Supports large repositories
* Suitable for AI workloads

---

## Negative Consequences

* Additional infrastructure
* Task monitoring required
* More complex debugging

---

# Monitoring Strategy

Monitor:

* Queue length
* Task duration
* Worker health
* Failure rate

Future tools:

* Flower
* Prometheus
* Grafana

---

# Security Considerations

Background workers must protect:

* Repository source code
* Task payload data
* API credentials

Security practices:

* Isolated execution
* Secure queues
* Environment-based secrets

---

# Future Improvements

Future extensions:

* Kubernetes worker autoscaling
* Distributed task execution
* GPU-based AI workers
* Priority queues
* Scheduled analysis jobs

---

# Conclusion

The background job processing architecture enables the Trustworthy AI Code Review Assistant to execute complex software analysis and AI workloads efficiently.

Celery and Redis provide a scalable, reliable, and maintainable solution for handling asynchronous operations while keeping the API layer responsive.
