# Research Reproducibility

## Overview

Reproducibility is a fundamental requirement for the **Trustworthy AI Code Review Assistant** research.

This document defines the practices used to ensure that experiments, evaluations, and results can be reproduced by researchers and developers using the same configurations and resources.

The reproducibility strategy covers:

* Source code management
* Environment configuration
* Dataset versioning
* Model configuration
* Experiment tracking
* Result storage

---

# Reproducibility Goals

The research aims to achieve:

## 1. Repeatable Experiments

The same experiment should produce comparable results when executed with the same configuration.

---

## 2. Transparent Evaluation

All evaluation decisions should be documented and traceable.

---

## 3. Environment Consistency

Experiments should run consistently across different machines.

---

## 4. Research Verification

Other researchers should be able to validate the reported findings.

---

# Reproducibility Architecture

```text
                 Experiment Definition

                         |
                         ▼

              Configuration Management

                         |
        ┌────────────────┼────────────────┐

        ▼                ▼                ▼

 Source Code        Dataset Version    Model Config


        |                |                |

        ▼                ▼                ▼


             Experiment Execution


                         |

                         ▼


              Result Collection


                         |

                         ▼


              Research Report
```

---

# Source Code Management

The project uses version control to track all changes.

Managed components:

* Backend source code
* Frontend source code
* AI pipeline
* Evaluation scripts
* Experiment notebooks
* Documentation

Repository stores:

```text
project/

├── src/

├── experiments/

├── evaluation/

├── datasets/

├── configs/

└── results/
```

---

# Version Control Strategy

Each experiment records:

* Git commit hash
* Branch name
* Release version
* Experiment date

Example:

```text
Experiment ID:
EXP-001

Git Commit:
1d9e491

Date:
2026-07-15
```

---

# Environment Reproducibility

The system uses containerized environments.

Technologies:

* Docker
* Docker Compose
* Python virtual environment

Environment includes:

* Python version
* Package versions
* Database version
* Runtime dependencies

Example:

```text
Python:
3.12

FastAPI:
0.115.0

PostgreSQL:
16

Docker:
latest
```

---

# Dependency Management

All dependencies are version controlled.

Files:

```text
requirements.txt

package.json

docker-compose.yml

Dockerfile
```

Example:

```text
fastapi==0.115.0
numpy==2.1.2
pandas==2.2.3
torch==2.5.0
```

---

# Dataset Reproducibility

Every dataset version stores:

* Dataset source
* Download date
* Version number
* Processing script
* Metadata

Example:

```json
{
 "dataset": "Security Benchmark",
 "version": "v1.0",
 "source": "Open Source Repository",
 "created": "2026-07-15"
}
```

---

# Dataset Structure

```text
datasets/

├── raw/

│   └── original_source_code/


├── processed/

│   └── labeled_data/


├── metadata/

│   └── dataset_info.json


└── versions/

    └── v1.0/
```

---

# Experiment Configuration Management

All experiments use configuration files.

Example:

```yaml
experiment_id: EXP-001

model:
  provider: openai
  temperature: 0

dataset:
  name: security_dataset
  version: v1

evaluation:
  metrics:
    - precision
    - recall
    - f1_score
```

---

# Prompt Version Control

Since LLM output depends on prompts, prompt versions are stored.

Structure:

```text
prompts/

├── code_review_v1.txt

├── security_review_v1.txt

└── refactoring_review_v1.txt
```

Each experiment records:

* Prompt version
* Model version
* Parameters

---

# Model Configuration Tracking

The following information is recorded:

## Commercial Models

* Provider name
* Model name
* API version
* Parameters

Example:

```text
Provider:
OpenAI

Model:
GPT

Temperature:
0
```

---

## Local Models

Recorded:

* Model checkpoint
* Quantization settings
* Hardware requirements

---

# Experiment Tracking

Each experiment produces metadata.

Example:

```json
{
 "experiment_id": "EXP-001",
 "repository": "sample-project",
 "model": "GPT",
 "prompt": "review-v2",
 "metrics": {
    "accuracy": 0.91,
    "trust_score": 0.86
 }
}
```

---

# Result Management

Results are stored with:

* Raw output
* Processed metrics
* Visualization data
* Final reports

Structure:

```text
results/

├── raw_outputs/

├── metrics/

├── charts/

└── reports/
```

---

# Documentation Requirements

Each experiment documents:

## Before Execution

* Objective
* Dataset
* Configuration
* Expected outcome

---

## After Execution

* Result
* Analysis
* Limitations
* Conclusion

---

# Reproducibility Checklist

| Item                       | Status |
| -------------------------- | ------ |
| Source code versioned      | ✅      |
| Dependencies documented    | ✅      |
| Docker environment         | ✅      |
| Dataset versioned          | ✅      |
| Prompt versioned           | ✅      |
| Model configuration stored | ✅      |
| Results archived           | ✅      |
| Documentation available    | ✅      |

---

# Limitations

## External API Dependency

Commercial LLM APIs may change over time.

Solution:

Store:

* Model name
* API version
* Response metadata

---

## Dataset Availability

Some datasets may change.

Solution:

Maintain dataset snapshots and metadata.

---

## Hardware Differences

Different hardware may affect performance.

Solution:

Record hardware specifications.

---

# Future Improvements

Future enhancements:

* Automated experiment tracking platform
* MLflow integration
* Dataset registry
* Model registry
* Public benchmark release
* Reproducible research package

---

# Conclusion

The reproducibility framework ensures that the Trustworthy AI Code Review Assistant experiments are transparent, repeatable, and scientifically reliable.

By controlling code, datasets, models, prompts, and environments, the research results can be independently verified and extended.
