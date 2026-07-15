# Literature Mapping

## Overview

This document provides a structured mapping of existing research areas related to the **Trustworthy AI Code Review Assistant**.

The purpose of this literature mapping is to understand previous approaches, identify research gaps, and position this project within the field of **AI for Software Engineering (AI4SE)**.

The reviewed research areas include:

* Automated code review
* Static program analysis
* Large Language Models for software engineering
* AI-assisted programming
* Trustworthy and explainable AI
* Software vulnerability detection

---

# Research Area 1: Automated Code Review Systems

## Background

Traditional automated code review systems use rule-based approaches to identify software issues.

Common techniques:

* Coding rule checking
* Pattern matching
* Static analysis
* Software metrics

Examples:

* Linters
* Security scanners
* Quality analysis tools

---

## Strengths

* Fast execution
* Deterministic results
* Easy automation

---

## Limitations

* Limited understanding of developer intent
* Difficult to analyze complex logic
* High false positive rate

---

## Research Gap

Traditional tools provide reliable evidence but lack contextual reasoning.

The proposed system combines static analysis with AI reasoning.

---

# Research Area 2: Static Code Analysis

## Background

Static analysis analyzes source code without executing the program.

Common analysis areas:

* Security vulnerabilities
* Code complexity
* Maintainability issues
* Coding standard violations

Tools used in this project:

* Ruff
* Bandit
* Semgrep
* Radon

---

## Strengths

* Explainable findings
* Fast detection
* Rule-based reliability

---

## Limitations

* Limited semantic understanding
* Cannot explain complex design problems

---

## Research Gap

Static tools need AI assistance for deeper code understanding and explanation.

---

# Research Area 3: Large Language Models for Software Engineering

## Background

Recent LLMs have demonstrated strong capabilities in:

* Code generation
* Code explanation
* Bug fixing
* Documentation generation
* Code review

Examples:

* GPT-based models
* Claude models
* Gemini models
* Code-specialized models

---

## Strengths

* Natural language understanding
* Repository-level reasoning
* Context-aware suggestions

---

## Limitations

LLMs may produce:

* Hallucinated issues
* Incorrect fixes
* Overconfident responses

---

## Research Gap

LLM output requires:

* Evidence validation
* Confidence estimation
* Trust measurement

---

# Research Area 4: AI-Based Vulnerability Detection

## Background

AI approaches have been applied for detecting security problems.

Methods include:

* Machine learning classification
* Deep learning
* Transformer-based models

---

## Strengths

* Learns complex patterns
* Detects unknown patterns

---

## Limitations

* Dataset dependency
* Lack of explanation
* Limited developer trust

---

## Research Gap

Security detection needs explainable and evidence-supported AI recommendations.

---

# Research Area 5: Explainable AI (XAI)

## Background

Explainable AI focuses on making AI decisions understandable.

Important concepts:

* Transparency
* Interpretability
* Confidence estimation
* Human trust

---

## Application to Code Review

AI reviewers should provide:

* Reason for finding
* Evidence
* Suggested solution
* Confidence level

---

## Research Gap

Many AI code tools generate suggestions without measuring reliability.

---

# Research Area 6: Human-AI Collaboration in Software Engineering

## Background

Modern software development increasingly uses AI assistants.

Examples:

* Code completion
* Automated debugging
* Review assistance

---

## Benefits

* Faster development
* Better productivity
* Learning support

---

## Challenges

* Over-reliance on AI
* Trust issues
* Incorrect recommendations

---

## Research Gap

Developers need AI systems that communicate uncertainty and evidence.

---

# Literature Comparison Matrix

| Research Area           | Existing Approach | Strength             | Limitation        | Proposed Solution                  |
| ----------------------- | ----------------- | -------------------- | ----------------- | ---------------------------------- |
| Automated Review        | Rule-based tools  | Reliable             | Limited reasoning | AI-enhanced review                 |
| Static Analysis         | Code scanners     | Accurate evidence    | Limited context   | LLM reasoning                      |
| LLM Code Review         | AI assistants     | Strong understanding | Hallucination     | Trust layer                        |
| Vulnerability Detection | ML models         | Pattern learning     | Poor explanation  | Evidence-based AI                  |
| Explainable AI          | XAI methods       | Transparency         | Limited SE focus  | Software-specific trust evaluation |

---

# Identified Research Gap

Based on existing literature, several gaps remain:

## Gap 1: Lack of Trust Measurement

Many AI code review systems generate recommendations without measuring reliability.

---

## Gap 2: Limited Hybrid Approaches

Few systems combine:

```
Static Analysis

+

LLM Reasoning

+

Trust Evaluation
```

---

## Gap 3: Insufficient Explainability

AI suggestions often lack:

* Evidence
* Confidence
* Reasoning transparency

---

## Gap 4: Limited Reproducible Evaluation

Many AI software engineering studies lack:

* Standard benchmarks
* Repeatable experiments
* Comprehensive metrics

---

# Position of Proposed Research

The Trustworthy AI Code Review Assistant addresses these gaps by introducing:

```text
Traditional Analysis

        +

Large Language Models

        +

Confidence Estimation

        +

Trust Evaluation

        +

Reproducible Benchmarking
```

---

# Expected Research Contribution

The project contributes:

1. A hybrid AI-assisted code review architecture

2. A trust evaluation framework for AI recommendations

3. A reproducible experiment methodology

4. A benchmark strategy for AI software engineering evaluation

5. A foundation for reliable AI developer tools

---

# Future Literature Expansion

Future research review may include:

* AI agents for software engineering
* Repository-level code intelligence
* Automated program repair
* Human-AI interaction studies
* AI safety in software development

---

# Conclusion

The literature mapping demonstrates that existing software engineering tools provide strong analysis capabilities but lack contextual reasoning and trust measurement.

This research combines static analysis, LLM intelligence, and trustworthy AI principles to develop a more reliable AI-assisted code review framework.
