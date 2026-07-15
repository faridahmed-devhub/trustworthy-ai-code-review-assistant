# Architecture Diagrams

## Overview

This directory contains the architecture diagrams for the **Trustworthy AI Code Review Assistant** project.

These diagrams document the overall system architecture, software components, deployment strategy, database design, research workflow, and AI evaluation pipeline.

The diagrams are intended to support:

* Software Architecture documentation
* Research reproducibility
* System understanding
* Project maintenance
* PhD research portfolio

---

## Directory Structure

```text
diagrams/
├── source/
│   └── Mermaid (.mmd) source files
└── generated/
    └── Generated PNG images
```

---

## Diagram List

| Diagram                   | Description                                    |
| ------------------------- | ---------------------------------------------- |
| system_architecture       | Overall system architecture                    |
| component_diagram         | Major software components and interactions     |
| deployment_diagram        | Deployment architecture using Docker           |
| database_schema           | Database tables and schema                     |
| er_diagram                | Entity relationship model                      |
| sequence_diagram          | End-to-end request sequence                    |
| data_flow                 | Data movement across the system                |
| ci_cd_pipeline            | Continuous Integration and Deployment workflow |
| trust_evaluation_pipeline | AI trustworthiness evaluation process          |
| ai_review_workflow        | Internal AI code review workflow               |

---

## Editing Diagrams

All diagrams are written in **Mermaid**.

Modify the `.mmd` files inside the `source/` directory.

After editing, regenerate the PNG images.

Example:

```bash
mmdc \
-i source/system_architecture.mmd \
-o generated/system_architecture.png
```

---

## Mermaid CLI

Install Mermaid CLI:

```bash
npm install -g @mermaid-js/mermaid-cli
```

Check installation:

```bash
mmdc --version
```

---

## Naming Convention

Source files:

```
diagram_name.mmd
```

Generated images:

```
diagram_name.png
```

Each source file should have a corresponding generated image with the same name.

---

## Documentation Guidelines

* Keep diagrams simple and readable.
* Update diagrams whenever the architecture changes.
* Ensure generated images are committed along with the Mermaid source.
* Use consistent naming and layout across all diagrams.
* Avoid duplicating information across diagrams.

---

## Purpose

These diagrams provide a visual representation of the project's architecture and serve as supporting documentation for software engineering research, implementation, and future maintenance.
