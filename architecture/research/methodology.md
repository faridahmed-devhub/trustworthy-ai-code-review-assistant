# Research Methodology

## Overview

The Trustworthy AI Code Review Assistant follows an experimental research methodology to evaluate the effectiveness, reliability, and trustworthiness of AI-assisted software engineering systems.

The methodology combines:

* Software engineering experimentation
* Static analysis evaluation
* Large Language Model evaluation
* Human-centered assessment
* Quantitative measurement

The objective is to determine how AI-based code review can provide reliable and explainable recommendations.

---

# Research Approach

This research follows a mixed evaluation approach:

```text
Research Problem

        |
        ▼

System Development

        |
        ▼

Controlled Experiments

        |
        ▼

Quantitative Evaluation

        |
        ▼

Analysis of Results

        |
        ▼

Research Findings
```

---

# Research Method Type

## Experimental Research

The project uses controlled experiments to compare different code review approaches.

The evaluated approaches are:

### Approach A: Static Analysis Only

Tools:

* Ruff
* Bandit
* Semgrep
* Radon

Purpose:

Measure traditional automated analysis performance.

---

### Approach B: LLM-Based Review Only

Models:

* GPT
* Claude
* Gemini
* Local LLM

Purpose:

Measure AI-only code review capability.

---

### Approach C: Hybrid AI Review

Combination:

```
Static Analysis Evidence

        +

LLM Reasoning

        +

Confidence Estimation

        |

        ▼

Trustworthy AI Recommendation
```

Purpose:

Evaluate whether combining approaches improves reliability.

---

# Research Workflow

## Phase 1: Dataset Collection

The first phase collects software repositories and benchmark examples.

Sources:

* Open-source GitHub repositories
* Vulnerability datasets
* Bug-fix commits
* Artificially injected defects

Collected information:

* Programming language
* Repository size
* Issue category
* Ground truth information

---

# Phase 2: Data Preparation

Collected repositories are prepared for experiments.

Steps:

1. Repository cloning

2. Code normalization

3. Dependency installation

4. Static analysis preparation

5. Ground truth labeling

---

# Phase 3: Static Analysis Execution

Each repository is analyzed using deterministic tools.

Pipeline:

```text
Repository

    |
    ▼

Ruff

    |
    ▼

Bandit

    |
    ▼

Semgrep

    |
    ▼

Radon

    |
    ▼

Static Findings
```

Collected data:

* Issue type
* Severity
* File location
* Rule identifier

---

# Phase 4: LLM Evaluation

The same repositories are analyzed by different LLM providers.

Input:

* Source code
* Static analysis findings
* Project context

Output:

* Detected issues
* Explanation
* Fix suggestions
* Confidence score

---

# Phase 5: Trust Evaluation

AI recommendations are evaluated using multiple factors.

Evaluation dimensions:

## Correctness

Does the AI recommendation identify a real issue?

Metrics:

* True Positive
* False Positive
* False Negative

---

## Evidence Support

Does the recommendation have supporting evidence?

Example:

```
AI Finding

        +

Static Analysis Result

        |

        ▼

Evidence Score
```

---

## Confidence Calibration

Compare:

AI confidence score

vs

Actual correctness

---

# Experimental Design

Each experiment follows a controlled setup.

Example:

```text
Experiment ID:
EXP-001

Dataset:
Python Security Dataset

Model:
GPT

Prompt:
Security Review v1

Temperature:
0

Output:
JSON Recommendation
```

---

# Variables

## Independent Variables

Factors changed during experiments:

* LLM model
* Prompt strategy
* Analysis approach
* Dataset

---

## Dependent Variables

Measured results:

* Detection accuracy
* Confidence score
* Processing time
* Cost

---

## Controlled Variables

Kept constant:

* Dataset version
* Evaluation criteria
* Environment configuration

---

# Evaluation Metrics

## Classification Metrics

Used for issue detection:

### Precision

Measures correctness of detected issues.

### Recall

Measures how many actual issues were found.

### F1 Score

Balances precision and recall.

---

# Trust Metrics

## Confidence Score

Measures AI certainty.

---

## Hallucination Rate

Measures incorrect AI recommendations.

---

## Evidence Alignment Score

Measures agreement between:

* AI output
* Static analysis evidence

---

# Performance Evaluation

Measured metrics:

* Analysis execution time
* API response latency
* Token consumption
* Memory usage
* CPU utilization

---

# Human Evaluation Method

Selected developers/reviewers evaluate:

* Usefulness
* Explanation quality
* Recommendation acceptance

Evaluation scale:

```
1 - Poor

2 - Weak

3 - Acceptable

4 - Good

5 - Excellent
```

---

# Reproducibility Strategy

Every experiment stores:

* Dataset version
* Model version
* Prompt version
* Configuration
* Results
* Environment information

Example:

```json
{
 "experiment": "EXP-001",
 "model": "GPT",
 "dataset": "Benchmark-v1",
 "prompt": "security-review-v2",
 "result": {
   "accuracy": 0.92,
   "confidence": 0.87
 }
}
```

---

# Statistical Analysis

Collected results will be analyzed using:

* Mean comparison
* Standard deviation
* Confidence intervals
* Statistical significance testing

Possible methods:

* t-test
* ANOVA
* Correlation analysis

---

# Threats to Validity

## Internal Validity

Risk:

Experimental configuration may influence results.

Mitigation:

Use controlled environments.

---

## External Validity

Risk:

Limited datasets may not represent all software systems.

Mitigation:

Use diverse repositories.

---

## Construct Validity

Risk:

Metrics may not fully represent trustworthiness.

Mitigation:

Combine automated and human evaluation.

---

## Reproducibility Risk

Risk:

Different environments produce different results.

Mitigation:

Use Docker and version-controlled experiments.

---

# Expected Outcome

The methodology aims to provide evidence about:

* Effectiveness of AI code review
* Benefits of hybrid analysis
* Reliability of confidence estimation
* Best practices for trustworthy AI engineering

---

# Conclusion

This research methodology provides a systematic framework for evaluating AI-powered software engineering systems.

By combining controlled experiments, quantitative metrics, and trust evaluation, the project aims to establish a reproducible approach for building reliable AI-assisted code review systems.
