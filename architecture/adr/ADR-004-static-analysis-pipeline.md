# ADR-004: Static Analysis Pipeline Design

## Status

Accepted


## Date

2026-07-14


## Context

The Trustworthy AI Code Review Assistant requires objective software quality information before generating AI-based recommendations.

Large Language Models can provide useful suggestions, but they may miss:

- Security vulnerabilities
- Code smells
- Complexity issues
- Maintainability problems

Therefore, a deterministic analysis layer is required before AI processing.


## Decision

We will implement a multi-tool static analysis pipeline using:

- Ruff
- Bandit
- Semgrep
- Radon
- AST-based code analysis


## Pipeline Flow
Source Code Repository

    ↓

Repository Scanner

    ↓

Code Parser

    ↓

Static Analysis Tools

    ↓

Quality & Security Report

    ↓

AI Review Engine


## Tool Responsibilities


### Ruff

Purpose:

- Python code quality analysis
- Lint detection
- Style issues


### Bandit

Purpose:

- Security vulnerability detection
- Unsafe coding pattern identification


### Semgrep

Purpose:

- Rule-based security scanning
- Custom vulnerability patterns


### Radon

Purpose:

- Cyclomatic complexity analysis
- Maintainability measurement


### AST Parser

Purpose:

- Code structure extraction
- Custom software metrics


## Rationale

Static analysis provides:

- Objective measurements
- Reproducible results
- Evidence for AI evaluation


AI recommendations can be compared against static analysis findings.


## Alternatives Considered


### AI-only Code Review

Rejected because:

- LLM output can hallucinate
- No deterministic validation


### Single Static Analysis Tool

Rejected because:

- Limited coverage
- Missing security and quality dimensions


## Consequences


Positive:

- Better AI evaluation
- Improved reliability
- Research reproducibility


Negative:

- Additional processing time
- Multiple tools need maintenance