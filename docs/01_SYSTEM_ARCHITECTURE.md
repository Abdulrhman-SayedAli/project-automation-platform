# 01_SYSTEM_ARCHITECTURE.md

# AI Software Factory

## System Architecture Specification

**Version:** 1.0

**Status:** Draft

**Document Type:** Architecture Specification

**Audience:** AI Agents, Software Engineers, Architects

**Dependencies**

* MASTER_PLAN.md
* 00_PROJECT_OVERVIEW.md

---

# 1. Purpose

This document defines the logical architecture of the AI Software Factory.

It describes:

* System services
* Responsibilities
* Communication model
* Runtime architecture
* Event flow
* Ownership boundaries
* Service dependencies

This document intentionally does **not** describe implementation details of LangGraph, the database, or APIs. Those are covered in dedicated specifications.

---

# 2. Architecture Philosophy

The platform is designed around one principle:

> **The orchestration system owns the workflow. Specialized services own execution.**

The orchestrator should never perform coding.

Workers should never make orchestration decisions.

GitHub should remain the source of truth for source code.

---

# 3. High-Level Architecture

```text
                    User
                      │
               Dashboard / API
                      │
               FastAPI Backend
                      │
             Project Service Layer
                      │
          ┌───────────┴───────────┐
          │                       │
   LangGraph Engine         Infrastructure
          │                       │
          │               GitHub Integration
          │               Docker Runner
          │               Redis Queue
          │
    Project Graph
    Task Graph
          │
    Worker Scheduler
          │
    ┌─────┴─────┐
    │     │     │
 Worker1 Worker2 Worker3
          │
   Coding Provider
          │
      GitHub PR
          │
      GitHub Actions
          │
     Reviewer Graph
          │
      Auto Merge
```

---

# 4. Services

The platform consists of seven primary services.

## 4.1 API Service

### Responsibilities

* Project CRUD
* Settings
* Authentication (future)
* GitHub Webhooks
* Dashboard Backend
* Worker Management

### Does NOT

* Execute LangGraph
* Execute Coding Provider
* Clone repositories

---

## 4.2 LangGraph Service

### Responsibilities

Owns every business workflow.

Examples:

* Project Planning
* Task Planning
* Task Execution
* Review
* Rework
* Merge Decision

### Does NOT

* Write code
* Call Git directly
* Execute Docker

Instead it delegates work through services.

---

## 4.3 Worker Scheduler

Responsibilities

* Maintain worker pool
* Assign tasks
* Retry failed jobs
* Enforce concurrency limits
* Track worker health

Maximum concurrent workers (V1)

```
3
```

Workers are interchangeable.

---

## 4.4 Sandbox Runner

Responsibilities

For every coding task:

* Create container
* Clone repository
* Mount temporary workspace
* Execute provider
* Destroy container

Containers are disposable.

No container survives after task completion.

---

## 4.5 Coding Provider

Responsibilities

* Receive task context
* Generate code
* Execute edits
* Run tests
* Commit
* Push branch
* Return execution result

Current provider

```
Codex
```

Future providers

* Claude Code
* GitHub Copilot
* Cursor
* Internal Providers

The rest of the system must never know which provider is being used.

---

## 4.6 GitHub Integration

Responsibilities

* Repository creation
* Issue creation
* Branch management
* Pull requests
* Reviews
* Merge
* Labels
* CI status

GitHub owns all source control state.

---

## 4.7 Dashboard

Responsibilities

* Project monitoring
* Task monitoring
* Worker monitoring
* Logs
* Settings
* Manual interventions

The dashboard is read-heavy.

Business logic belongs in the backend.

---

# 5. Runtime Components

```text
FastAPI
│
├── REST API
├── GitHub Webhooks
├── WebSocket Events
└── Configuration

LangGraph
│
├── Project Graph
├── Task Graph
└── Review Graph

Workers
│
├── Worker 1
├── Worker 2
└── Worker 3

Infrastructure
│
├── Docker
├── Redis
├── PostgreSQL
└── GitHub
```

---

# 6. Communication Rules

Services communicate through service interfaces.

Allowed

```text
API
 ↓
Project Service
 ↓
LangGraph
 ↓
Worker Scheduler
 ↓
Coding Provider
```

Forbidden

```text
Dashboard
 ↓
Database
```

```text
LangGraph
 ↓
GitHub REST directly
```

All external integrations must pass through dedicated services.

---

# 7. Project Lifecycle

```text
Project Created
        │
Requirement Analysis
        │
Architecture
        │
Planning
        │
GitHub Issues
        │
Task Queue
        │
Workers
        │
Pull Requests
        │
Review
        │
Merge
        │
Completed
```

Each stage is represented by a LangGraph node or graph.

---

# 8. Task Lifecycle

Every task follows the same lifecycle.

```text
Created
   │
AI Ready
   │
Assigned
   │
Working
   │
PR Open
   │
Review
   │
CI
   │
Merged
```

Failure path

```text
Review Failed
        │
Rework
        │
Review
```

Blocking path

```text
Blocked
        │
Human Intervention
```

---

# 9. Worker Lifecycle

Workers are ephemeral.

```text
Idle

↓

Task Assigned

↓

Sandbox Created

↓

Repository Cloned

↓

Branch Checked Out

↓

Provider Executed

↓

Tests Executed

↓

Commit

↓

Push

↓

PR Updated

↓

Cleanup

↓

Idle
```

Workers never keep memory between tasks.

---

# 10. Dependency Rules

The dependency graph is intentionally simple.

```text
Dashboard
        │
        ▼
API
        │
        ▼
Services
        │
        ▼
LangGraph
        │
        ▼
Provider Interface
        │
        ▼
Provider Implementation
```

Database access

```text
API
 ↓
Repository Layer
 ↓
PostgreSQL
```

No service may bypass the repository layer.

---

# 11. Failure Recovery

The architecture must tolerate failures.

Recoverable failures:

* Worker crash
* Container failure
* Provider timeout
* Network interruption
* API restart

Non-recoverable failures:

* Invalid project specification
* Corrupted repository
* Human-required business decision

Recoverable failures should resume automatically from persisted graph state.

---

# 12. Scalability Strategy

Version 1

```
3 workers
1 orchestrator
1 API instance
```

Future

```
Multiple orchestrators

Horizontal workers

Dedicated queue service

Kubernetes
```

The architecture should support horizontal scaling without redesigning service interfaces.

---

# 13. AI Agent Implementation Notes

## Module Owner

**Architecture Team**

## Allowed to modify

* `app/services/**`
* `app/core/**`
* `docs/`

## Must NOT modify

* Provider implementations
* Dashboard components
* Database schema
* LangGraph nodes

## Deliverables

* Service interfaces
* Dependency graph
* Component boundaries
* Internal communication contracts

## Acceptance Criteria

* Every service has a single responsibility.
* No circular dependencies.
* Provider abstraction is preserved.
* GitHub remains the source of truth.
* Workers remain stateless.
* All service boundaries are documented.
* Architecture supports replacing the coding provider without changes to orchestration.

---

# 14. Related Documents

* MASTER_PLAN.md
* 02_TECH_STACK.md
* 03_DATABASE_DESIGN.md
* 04_LANGGRAPH_ARCHITECTURE.md
* 06_CODING_PROVIDER_INTERFACE.md

---

**End of Document**
