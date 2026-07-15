# ADR-004: LLM Review Engine Architecture

## Status

Accepted

## Date

2026-07-15

---

# Decision

Implement a modular **LLM-based Review Engine** that provides AI-assisted software engineering analysis using multiple Large Language Model providers.

The LLM Review Engine will support:

* Code explanation
* Bug detection
* Security analysis
* Code improvement suggestions
* Test generation assistance
* Refactoring recommendations

The AI output will be validated using static analysis results and trust evaluation mechanisms.

---

# Context

Large Language Models have demonstrated strong capabilities in software engineering tasks such as:

* Code understanding
* Bug detection
* Code generation
* Documentation generation
* Software maintenance assistance

However, LLM-based systems have limitations:

* Hallucination
* Incorrect suggestions
* Missing security issues
* Overconfidence
* Inconsistent reasoning

The goal of this project is not only to generate AI recommendations but also to measure and improve their trustworthiness.

Therefore, an independent LLM Review Engine is required.

---

# Problem Statement

A simple direct LLM integration creates several problems:

* No control over AI responses
* Difficult model comparison
* Poor reproducibility
* Lack of confidence measurement
* Limited research capability

The system requires a structured AI processing layer.

---

# Decision Drivers

The following factors influenced the design:

## Trustworthiness

AI recommendations must be:

* Explainable
* Validated
* Measurable

---

## Model Flexibility

The system should support multiple providers:

* OpenAI GPT models
* Anthropic Claude
* Google Gemini
* Open-source LLMs

---

## Research Capability

The architecture should support:

* Model comparison
* Experiment tracking
* Evaluation datasets
* Benchmarking

---

## Maintainability

LLM integration should be isolated from the main application.

---

# Selected Architecture

```text id="zj8c5x"
                Source Code

                    |
                    ▼

             Context Builder

                    |
                    ▼

              Prompt Manager

                    |
                    ▼

              LLM Router

        ┌───────────┼───────────┐

        ▼           ▼           ▼

      GPT        Claude      Local LLM


                    |
                    ▼

             Response Processor

                    |
                    ▼

          Trust Evaluation Layer

                    |
                    ▼

             Final Recommendation
```

---

# LLM Engine Components

## 1. Context Builder

Responsible for preparing information for the model.

Input:

* Source code
* Static analysis findings
* Project metadata
* Previous analysis history

Output:

Structured AI context.

---

## 2. Prompt Management System

Manages:

* Prompt templates
* System instructions
* Task-specific prompts

Examples:

* Security review prompt
* Bug detection prompt
* Code quality prompt

Benefits:

* Reproducibility
* Experiment comparison

---

## 3. LLM Router

Provides model abstraction.

Example:

```text
Review Request

      |
      ▼

LLM Router

      |
 ┌────┼────┐

GPT Claude Gemini
```

Benefits:

* Provider independence
* Cost optimization
* Research comparison

---

## 4. Response Processor

Processes raw LLM responses.

Tasks:

* Response formatting
* JSON conversion
* Recommendation extraction
* Confidence estimation

---

# AI Review Workflow

```text id="o0l9jd"
Developer Code

      |
      ▼

Static Analysis Results

      |
      ▼

Context Preparation

      |
      ▼

LLM Analysis

      |
      ▼

AI Recommendation

      |
      ▼

Trust Validation

      |
      ▼

Final Report
```

---

# Prompt Engineering Strategy

The system uses structured prompts.

Example:

```text
Role:
You are an expert software security reviewer.

Task:
Analyze the following code.

Evidence:
Static analysis findings.

Output:
Provide:
- Issue
- Severity
- Explanation
- Fix suggestion
- Confidence score
```

---

# Hallucination Mitigation Strategy

The system reduces hallucination using:

## Evidence-Based Review

LLM receives:

* Static analysis findings
* Code context
* Software metrics

---

## Output Validation

AI suggestions are checked against:

* Static analyzers
* Security rules
* Software metrics

---

## Confidence Scoring

Each recommendation receives:

* Confidence level
* Supporting evidence
* Risk level

---

# Alternatives Considered

## Direct API Integration

Example:

Application → OpenAI API

Advantages:

* Simple implementation

Disadvantages:

* No abstraction
* Hard to change models
* Poor research flexibility

Decision:

Rejected.

---

## Self-Hosted Only LLM

Advantages:

* Full data control

Disadvantages:

* High infrastructure requirements
* Large computational cost

Decision:

Not selected as primary approach.

---

# Consequences

## Positive Consequences

* Flexible AI architecture
* Multiple model support
* Better research capability
* Improved trust evaluation
* Easier future expansion

---

## Negative Consequences

* Increased system complexity
* API cost management required
* Model behavior differences

Mitigation:

* Model abstraction layer
* Evaluation framework
* Usage monitoring

---

# Security Considerations

The LLM engine must protect:

* Source code privacy
* API credentials
* Sensitive information

Security practices:

* Secret management
* Secure API communication
* Data filtering
* Optional local model support

---

# Future Improvements

Future extensions:

* Agent-based code review
* Repository-level reasoning
* Fine-tuned software engineering models
* IDE assistant integration
* Autonomous test generation

---

# Conclusion

The LLM Review Engine provides an extensible and trustworthy AI layer for software engineering analysis.

By combining multiple LLM providers, structured prompting, validation mechanisms, and trust evaluation, the system moves beyond simple AI code generation toward reliable AI-assisted software engineering.
