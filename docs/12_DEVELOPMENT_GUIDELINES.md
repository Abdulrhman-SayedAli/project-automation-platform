# 12_DEVELOPMENT_GUIDELINES.md

# AI Software Factory
## Development Guidelines

Version: 1.0

Status: Approved

---

# Purpose

This document defines development standards for all human and AI contributors.

All code must follow these rules.

---

# Core Rules

- Keep modules small.
- Use explicit interfaces.
- Avoid hidden side effects.
- Prefer simple code.
- Do not hardcode providers.
- Do not bypass service boundaries.
- Do not mix workflow logic with infrastructure logic.

---

# Repository Structure

Expected structure:

```text
app/
  api/
  core/
  db/
  graph/
  services/
  repositories/
  schemas/
  models/
  providers/
  workers/

dashboard/

docs/

docker/
```

---

# Backend Standards

Backend code must use:

- FastAPI routers
- Pydantic schemas
- Service layer
- Repository layer
- SQLAlchemy models
- Alembic migrations

Routers must not contain business logic.

---

# Service Pattern

Use this structure:

```text
Router
  ↓
Service
  ↓
Repository
  ↓
Database
```

Forbidden:

```text
Router
  ↓
Database
```

---

# Graph Standards

LangGraph nodes must:

- receive state
- return state
- be deterministic
- call services, not infrastructure directly

Nodes must not:

- call GitHub API directly
- call Docker directly
- call Codex directly
- mutate global state

---

# Provider Standards

Coding providers must implement the shared provider interface.

Do not reference Codex outside:

```text
app/providers/codex/
```

All other code must depend on:

```text
CodingProvider
```

---

# Database Standards

Every persistent model must have:

- UUID primary key
- created_at
- updated_at where applicable
- indexes for common lookups
- foreign keys where appropriate

Every schema change requires Alembic migration.

---

# API Standards

Every API endpoint must have:

- request schema
- response schema
- validation
- structured errors
- logging
- tests

No endpoint may expose ORM models directly.

---

# Error Handling

Errors must be classified as:

```text
Recoverable
Fatal
Human Required
```

Recoverable errors may be retried.

Fatal errors must stop execution.

Human Required errors must create an escalation event.

---

# Logging Standards

Logs must be structured.

Every important log should include:

```text
project_id
task_id
worker_id
graph_node
event_type
```

Never log secrets.

---

# Testing Standards

Required test types:

- Unit tests
- Integration tests
- API tests
- Graph tests
- Provider tests

Every PR must include relevant tests.

---

# Git Standards

Branch format:

```text
ai/project-{project_id}/task-{task_id}
```

Commit format:

```text
feat(scope): message
fix(scope): message
docs(scope): message
test(scope): message
refactor(scope): message
```

---

# Pull Request Standards

Every PR must include:

- Summary
- Issue reference
- Files changed
- Tests run
- Risks
- Screenshots if UI changed

---

# Configuration Standards

Never hardcode:

- secrets
- tokens
- provider names
- URLs
- repository owners
- retry limits
- worker counts

Use environment variables and settings.

---

# Security Standards

Never:

- commit secrets
- run code on host machine
- allow workers to access production systems
- expose provider keys to dashboard
- bypass sandbox execution

---

# Documentation Standards

Update documentation when changing:

- architecture
- APIs
- database schema
- graph state
- provider interface
- deployment behavior

---

# AI Agent Rules

AI implementation agents must:

- read assigned docs first
- modify only assigned files
- preserve architecture
- add tests
- update docs when needed
- stop if requirement is unclear

---

# Acceptance Criteria

A contribution is acceptable when:

- code follows architecture
- tests pass
- no unrelated changes
- no hardcoded secrets
- documentation updated
- PR description complete

---

End of Document