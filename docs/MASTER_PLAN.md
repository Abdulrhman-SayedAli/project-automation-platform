# MASTER_PLAN.md

# AI Software Factory

## Master Implementation Plan

**Version:** 1.0

**Status:** Active

**Document Type:** Master Specification

**Audience:** AI Agents, Software Engineers, Architects

---

# Purpose

This document is the entry point for the entire project.

Every AI agent must read this document before implementing any feature.

Its purpose is to define:

* How the project is organized.
* Which documents to read.
* Implementation order.
* Ownership boundaries.
* Parallel development rules.
* Coding principles.
* Collaboration rules.

No implementation should begin before following the workflow described here.

---

# Project Vision

The objective of this project is to build an autonomous software engineering platform capable of converting a high-level software idea into a production-ready software project.

The platform coordinates multiple AI agents responsible for planning, architecture, implementation, testing, reviewing and merging software.

The platform itself is **not** a coding agent.

It is an orchestration platform.

---

# Core Principles

The following principles are mandatory.

## 1. Modularity

Every component must own exactly one responsibility.

Never combine multiple business responsibilities into one module.

Bad:

* Worker manages GitHub
* Worker updates database
* Worker creates architecture

Good:

* Worker executes task
* GitHub service manages GitHub
* Planner creates tasks

---

## 2. Loose Coupling

Every major subsystem must communicate through interfaces.

Never directly depend on implementation details.

Example:

```python
CodingProvider.run_task(...)
```

Never

```python
CodexProvider.run(...)
```

outside the provider factory.

---

## 3. Replaceable Providers

The coding provider must never be hardcoded.

Current provider:

* Codex

Future providers:

* Claude Code
* Cursor
* GitHub Copilot
* Internal Provider

Switching providers should require configuration only.

---

## 4. GitHub Owns Code

GitHub is always the source of truth.

The database stores synchronization state only.

Never duplicate Git history inside PostgreSQL.

---

## 5. Disposable Workers

Workers never keep local state.

Every worker starts with:

* empty filesystem
* cloned repository
* assigned task

Every worker exits after completing work.

---

## 6. Durable Orchestration

LangGraph owns workflow state.

Workers never own workflow state.

A crashed worker must be replaceable without losing project progress.

---

# Documentation Structure

The documentation is intentionally divided into independent specifications.

Each document owns one domain.

| Document                        | Purpose                     |
| ------------------------------- | --------------------------- |
| 00_PROJECT_OVERVIEW.md          | Business vision and scope   |
| 01_SYSTEM_ARCHITECTURE.md       | Service architecture        |
| 02_TECH_STACK.md                | Technology decisions        |
| 03_DATABASE_DESIGN.md           | Database schema             |
| 04_LANGGRAPH_ARCHITECTURE.md    | Graph implementation        |
| 05_AGENT_SPECIFICATIONS.md      | Agent contracts             |
| 06_CODING_PROVIDER_INTERFACE.md | Coding provider abstraction |
| 07_GITHUB_WORKFLOW.md           | GitHub lifecycle            |
| 08_API_SPECIFICATION.md         | Backend APIs                |
| 09_DASHBOARD_SPECIFICATION.md   | Frontend                    |
| 10_DOCKER_DEPLOYMENT.md         | Deployment                  |
| 11_IMPLEMENTATION_ROADMAP.md    | Build order                 |
| 12_DEVELOPMENT_GUIDELINES.md    | Coding standards            |
| 13_ACCEPTANCE_CRITERIA.md       | Definition of Done          |

---

# AI Agent Workflow

Every implementation agent must follow this workflow.

## Step 1

Read:

* MASTER_PLAN.md

---

## Step 2

Read the document related to the assigned module.

Examples

Backend Agent

Reads:

* 01_SYSTEM_ARCHITECTURE.md
* 03_DATABASE_DESIGN.md
* 08_API_SPECIFICATION.md
* 12_DEVELOPMENT_GUIDELINES.md

Graph Agent

Reads:

* 04_LANGGRAPH_ARCHITECTURE.md
* 05_AGENT_SPECIFICATIONS.md
* 11_IMPLEMENTATION_ROADMAP.md

Dashboard Agent

Reads:

* 09_DASHBOARD_SPECIFICATION.md
* 12_DEVELOPMENT_GUIDELINES.md

Infrastructure Agent

Reads:

* 10_DOCKER_DEPLOYMENT.md
* 07_GITHUB_WORKFLOW.md

---

## Step 3

Implement only the assigned module.

Never implement unrelated functionality.

---

## Step 4

Run required tests.

---

## Step 5

Update documentation if required.

---

## Step 6

Open Pull Request.

---

# Repository Ownership

Every directory has one owner.

| Directory     | Owner           |
| ------------- | --------------- |
| app/api       | Backend         |
| app/db        | Backend         |
| app/graph     | Graph           |
| app/providers | Coding Provider |
| app/workers   | Worker System   |
| dashboard     | Frontend        |
| docker        | Infrastructure  |
| docs          | Documentation   |

Agents should avoid modifying directories outside their ownership unless the task explicitly requires it.

---

# Parallel Development Rules

The system is designed for multiple workers.

Three workers may execute simultaneously.

Parallel work is allowed only when no dependency exists.

Example

Allowed

```
Worker 1

Database

Worker 2

Dashboard

Worker 3

Docker
```

Not allowed

```
Worker 1

Database Schema

Worker 2

Database Models
```

The second depends on the first.

Dependency order must always be respected.

---

# Branch Strategy

Every task owns exactly one branch.

Branch format

```
ai/project-{id}/task-{id}
```

Never reuse branches.

---

# Pull Request Strategy

Each PR must solve exactly one GitHub issue.

No unrelated changes.

Every PR must contain

* summary
* implementation details
* tests executed
* risks
* issue reference

---

# Coding Standards

Every implementation must

* use type hints
* include logging
* include error handling
* include unit tests
* include documentation
* follow project architecture

---

# State Management

There are three independent states.

## Project State

Overall project progress.

Examples

* Planning
* Executing
* Completed

---

## Task State

Individual GitHub issue progress.

Examples

* AI Ready
* Working
* PR Open
* Review
* Done

---

## Worker State

Worker lifecycle.

Examples

* Idle
* Running
* Failed
* Finished

Never mix these state machines.

---

# Architecture Rules

The following dependencies are allowed.

```
API

↓

Services

↓

Repositories

↓

Database
```

Not allowed

```
API

↓

Database
```

---

Graph

↓

Provider Interface

↓

Provider Implementation

Not

Graph

↓

Codex

```

---

# Definition of Complete

A module is complete when

- implementation finished
- tests pass
- documentation updated
- acceptance criteria satisfied
- PR approved

---

# Things AI Agents Must Never Do

Never

- Skip documentation.
- Change architecture without updating documentation.
- Modify unrelated modules.
- Bypass interfaces.
- Introduce circular dependencies.
- Hardcode provider implementations.
- Execute code outside sandbox.
- Commit secrets.
- Modify production deployment configuration unless explicitly assigned.

---

# Implementation Order

The implementation order is defined in

```

11_IMPLEMENTATION_ROADMAP.md

```

No module should be implemented before its dependencies.

---

# Final Rule

Whenever documentation and code disagree:

**The documentation is authoritative until it is intentionally revised.**

AI agents must not silently change the intended architecture through implementation.

---

**End of Document**
```
