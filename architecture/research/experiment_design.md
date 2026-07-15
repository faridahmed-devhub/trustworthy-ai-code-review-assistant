# Experiment Design

## Overview

This document describes the experimental design for evaluating the **Trustworthy AI Code Review Assistant**.

The experiments are designed to measure:

* AI code review effectiveness
* Static analysis contribution
* Hybrid AI + static analysis performance
* Trustworthiness of AI recommendations
* LLM provider performance

The goal is to experimentally validate whether combining deterministic software analysis with LLM reasoning improves automated code review reliability.

---

# Experiment Objectives

The experiments aim to answer the following questions:

## Objective 1

Evaluate the ability of AI models to identify software issues.

Measured:

* Bug detection
* Security vulnerability detection
* Code quality issues

---

## Objective 2

Compare different code review approaches.

Compared systems:

1. Static Analysis Only

2. LLM Review Only

3. Hybrid AI Review

---

## Objective 3

Evaluate AI trustworthiness.

Measured:

* Confidence accuracy
* Hallucination rate
* Evidence support

---

# Experimental Framework

```text
                Dataset

                   |
                   ▼

          Repository Preparation

                   |
                   ▼

          Analysis Configuration

                   |
        ┌──────────┼──────────┐

        ▼          ▼          ▼

 Static Tool    LLM       Hybrid System


        |          |          |

        ▼          ▼          ▼


        Evaluation & Comparison


                   |

                   ▼


              Final Results
```

---

# Experiment Categories

## Experiment 1: Static Analysis Evaluation

### Goal

Measure the performance of traditional static analysis tools.

### Tools

* Ruff
* Bandit
* Semgrep
* Radon

### Input

Software repositories with known issues.

### Output

```json
{
 "tool": "bandit",
 "issue": "security vulnerability",
 "severity": "high",
 "location": "file.py:45"
}
```

### Metrics

* Precision
* Recall
* F1 Score

---

# Experiment 2: LLM Code Review Evaluation

## Goal

Evaluate AI-only code review capability.

## Models

Examples:

* GPT
* Claude
* Gemini
* Local LLM

## Input

```text
Source Code

+

Task Description

+

Project Context
```

## Output

```json
{
 "issue": "SQL injection risk",
 "severity": "high",
 "explanation": "...",
 "suggestion": "...",
 "confidence": 0.86
}
```

---

# Experiment 3: Hybrid AI Review Evaluation

## Goal

Evaluate whether combining static analysis and LLM improves results.

Architecture:

```text
Source Code

     |

     ▼

Static Analysis

     |

     ▼

Evidence Collection

     |

     ▼

LLM Reasoning

     |

     ▼

Trust Evaluation

     |

     ▼

Final Recommendation
```

---

# Experiment 4: LLM Provider Comparison

## Goal

Compare multiple AI models.

Models:

| Provider      | Purpose                      |
| ------------- | ---------------------------- |
| OpenAI        | Advanced reasoning           |
| Anthropic     | Long context analysis        |
| Google Gemini | Alternative commercial model |
| Local LLM     | Privacy evaluation           |

---

# Experiment Variables

## Independent Variables

Variables changed during experiments:

| Variable        | Values                |
| --------------- | --------------------- |
| LLM Model       | GPT / Claude / Gemini |
| Analysis Method | Static / LLM / Hybrid |
| Prompt Version  | v1 / v2 / v3          |
| Dataset         | Multiple repositories |

---

## Dependent Variables

Measured results:

| Metric     | Description               |
| ---------- | ------------------------- |
| Accuracy   | Correct issue detection   |
| Precision  | Correct recommendations   |
| Recall     | Coverage                  |
| F1 Score   | Overall detection quality |
| Confidence | AI certainty              |
| Latency    | Processing time           |
| Cost       | Resource usage            |

---

## Controlled Variables

Kept constant:

* Dataset version
* Execution environment
* Evaluation criteria
* Temperature settings
* Prompt format

---

# Dataset Design

## Dataset Sources

Possible sources:

* Open-source GitHub repositories
* Security vulnerability datasets
* Bug benchmark datasets
* Synthetic bug injection

---

## Dataset Categories

```text
Dataset

├── Bug Detection

├── Security Vulnerabilities

├── Code Smells

├── Performance Issues

└── Maintainability Problems
```

---

# Experimental Environment

## Hardware

Example:

```text
CPU:
RAM:
GPU:
Storage:
```

---

## Software Environment

```text
Operating System

Python Version

Docker Version

Database

LLM API Version

Analysis Tool Versions
```

---

# Experiment Execution Procedure

## Step 1: Prepare Dataset

* Download repository
* Verify source code
* Assign ground truth labels

---

## Step 2: Run Static Analysis

Execute:

* Ruff
* Bandit
* Semgrep
* Radon

Store results.

---

## Step 3: Execute LLM Review

Send:

* Source code
* Analysis evidence
* Review instructions

Collect responses.

---

## Step 4: Apply Trust Evaluation

Calculate:

* Confidence score
* Evidence matching
* Hallucination probability

---

## Step 5: Analyze Results

Compare:

```text
Static Only

vs

LLM Only

vs

Hybrid System
```

---

# Result Storage Format

Each experiment stores:

```json
{
 "experiment_id": "EXP-001",
 "dataset": "Security-Benchmark",
 "method": "Hybrid",
 "model": "GPT",
 "metrics": {
    "precision": 0.91,
    "recall": 0.87,
    "f1": 0.89,
    "confidence": 0.85
 }
}
```

---

# Experiment Repetition

Each experiment should be repeated multiple times to reduce randomness.

Recommended:

* Minimum 3 runs
* Same configuration
* Average result calculation

---

# Statistical Analysis

Results will be analyzed using:

* Average performance
* Standard deviation
* Confidence interval
* Statistical significance tests

Possible methods:

* t-test
* ANOVA

---

# Expected Results

The experiments aim to demonstrate:

1. Hybrid AI review improves issue detection.

2. Static analysis provides valuable evidence.

3. Confidence estimation improves AI reliability.

4. Multiple model evaluation identifies suitable LLM strategies.

---

# Future Experiments

Future research:

* Multi-agent AI reviewers
* Continuous repository monitoring
* Developer productivity studies
* IDE integration evaluation
* Enterprise-scale benchmarking

---

# Conclusion

The experiment design provides a structured framework for evaluating the Trustworthy AI Code Review Assistant.

Through controlled comparisons between static analysis, LLM-based review, and hybrid approaches, the research can measure the effectiveness and reliability of AI-assisted software engineering.
