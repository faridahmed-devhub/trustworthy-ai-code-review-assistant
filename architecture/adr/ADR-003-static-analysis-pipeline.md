# ADR-003: Static Analysis Pipeline Design

## Status

Accepted

## Date

2026-07-15

---

# Decision

Use a multi-tool static analysis pipeline combining:

* Ruff
* Bandit
* Semgrep
* Radon
* AST-based custom analysis

for automated software quality, security, and maintainability assessment.

---

# Context

The Trustworthy AI Code Review Assistant requires reliable software analysis before generating AI-based recommendations.

Large Language Models can provide useful code suggestions but may produce:

* Incorrect recommendations
* Missed vulnerabilities
* Incomplete edge case analysis
* Hallucinated explanations

To improve trustworthiness, the system integrates deterministic static analysis tools as an additional validation layer.

---

# Problem Statement

A single static analysis tool cannot cover all software quality dimensions.

Required analysis areas:

* Code quality
* Security vulnerabilities
* Code complexity
* Maintainability
* Software metrics
* Coding standards

Therefore, a multi-tool analysis pipeline is required.

---

# Decision Drivers

The following factors influenced this decision:

## Accuracy Improvement

Combining multiple analysis techniques improves issue detection coverage.

---

## Trustworthy AI Requirement

Static analysis results provide evidence for evaluating LLM recommendations.

---

## Language Support

The initial implementation focuses on Python because of:

* AI ecosystem compatibility
* Research availability
* Enterprise usage

---

## Extensibility

The pipeline should support adding future analyzers.

---

# Selected Architecture

```text
Source Code Repository

        |
        ▼

Repository Scanner

        |
        ▼

Static Analysis Pipeline

        |
 ┌──────┼────────┬────────┬────────┐

 ▼      ▼        ▼        ▼        ▼

Ruff  Bandit  Semgrep  Radon  AST Analyzer

        |
        ▼

Analysis Result Aggregator

        |
        ▼

Trust Evaluation Engine
```

---

# Selected Tools

## Ruff

Purpose:

* Code quality checking
* Linting
* Formatting validation
* Python best practices

Provides:

* Fast execution
* Modern Python support

---

## Bandit

Purpose:

* Security vulnerability detection

Detects:

* Hardcoded secrets
* Unsafe function usage
* Security issues

---

## Semgrep

Purpose:

* Pattern-based security analysis

Advantages:

* Custom security rules
* Multi-language support
* Enterprise usage

---

## Radon

Purpose:

Software metrics:

* Cyclomatic complexity
* Maintainability index
* Code complexity

---

## AST Analyzer

Purpose:

Custom research-oriented analysis.

Provides:

* Function-level metrics
* Code structure analysis
* Custom software engineering features

---

# Alternatives Considered

## SonarQube Only

### Advantages

* Comprehensive dashboard
* Enterprise adoption

### Disadvantages

* Requires additional infrastructure
* Less flexible for research experiments
* Limited custom AI integration

Decision:

Rejected as the primary solution.

Can be added as optional integration.

---

## Single Static Analyzer

Example:

Only Ruff or Bandit

### Disadvantages

* Limited coverage
* Cannot measure multiple quality dimensions

Decision:

Rejected.

---

# Analysis Pipeline Workflow

```text
Repository

    |
    ▼

File Detection

    |
    ▼

Language Identification

    |
    ▼

Parallel Analysis

    |
 ┌──┼──┬──┐

 ▼  ▼  ▼  ▼

Ruff
Bandit
Semgrep
Radon

    |
    ▼

Result Normalization

    |
    ▼

Quality Metrics

    |
    ▼

AI Review Engine
```

---

# Data Output Format

All tools produce normalized results.

Example:

```json
{
  "file": "app/auth.py",
  "tool": "bandit",
  "category": "security",
  "severity": "high",
  "message": "Possible SQL injection risk",
  "line": 45
}
```

---

# Integration with Trust Evaluation

Static analysis results are used to evaluate AI responses.

Example:

```text
AI Recommendation

        +

Static Analysis Evidence

        |

        ▼

Trust Score Calculation
```

---

# Consequences

## Positive Consequences

* Better software quality assessment
* Improved AI reliability
* Evidence-based recommendations
* Research experiment support
* Extensible analysis framework

---

## Negative Consequences

* Multiple tools increase complexity
* Different tools may produce duplicate findings
* False positives require handling

Mitigation:

* Result normalization
* Rule filtering
* Confidence scoring

---

# Future Improvements

Possible extensions:

* Multi-language support
* Machine learning based issue classification
* Custom vulnerability models
* IDE integration
* Continuous analysis in CI/CD

---

# Conclusion

The multi-tool static analysis pipeline provides a reliable foundation for trustworthy AI-assisted code review. By combining deterministic software analysis with LLM-based reasoning, the system improves the accuracy, security, and explainability of AI-generated recommendations.
