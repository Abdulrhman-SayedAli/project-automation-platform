# 02_TECH_STACK.md

# AI Software Factory
## Technology Stack Specification

Version: 1.0

Status: Approved

Dependencies:

- MASTER_PLAN.md
- 00_PROJECT_OVERVIEW.md
- 01_SYSTEM_ARCHITECTURE.md

---

# Purpose

This document defines every technology used by the platform and the reason it was selected.

The primary objective is to keep every component replaceable while maintaining a stable architecture.

Technology decisions must not leak into business logic.

---

# Core Principles

- Prefer mature technologies.
- Every component should be replaceable.
- Keep infrastructure simple for local development.
- Everything must run through Docker.
- Development and production environments should remain as similar as possible.

---

# High-Level Stack

| Layer | Technology |
|---------|------------|
| Backend API | FastAPI |
| Orchestration | LangGraph |
| Database | PostgreSQL |
| Cache / Queue | Redis |
| Dashboard | Next.js |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Validation | Pydantic |
| Background Jobs | FastAPI + Redis Workers |
| Containers | Docker |
| Repository | GitHub |
| CI | GitHub Actions |
| Coding Provider | Codex (replaceable) |
| Logging | Structlog |
| Configuration | Pydantic Settings |

---

# Backend

Framework

FastAPI

Reason

- Async
- Excellent typing
- Automatic OpenAPI
- Mature ecosystem
- Easy dependency injection

Responsibilities

- REST API
- Webhooks
- Authentication
- Project Management
- Dashboard Backend

---

# LangGraph

Responsibilities

- Project Planning
- Task Planning
- Workflow Orchestration
- State Machine
- Recovery
- Retry Logic

LangGraph owns workflow execution.

It never owns business data.

---

# Database

Technology

PostgreSQL

Reason

- Reliable
- ACID compliant
- Row locking
- JSON support
- Excellent SQLAlchemy support

Stores

- Projects
- Tasks
- Workers
- Events
- Graph State Metadata
- Settings

Never stores

- Git history
- Repository files

---

# Redis

Responsibilities

- Queue
- Distributed locks
- Cache
- Pub/Sub
- Worker coordination

Redis is temporary.

Persistent state belongs in PostgreSQL.

---

# Dashboard

Technology

Next.js

Responsibilities

- Project Monitoring
- Worker Monitoring
- Task View
- Logs
- Settings

Business logic always belongs to the API.

---

# ORM

SQLAlchemy

Reason

- Stable
- Well documented
- Async support
- Alembic integration

No raw SQL except when performance or locking requires it.

---

# Migrations

Alembic

Every schema change must have a migration.

Never modify production schema manually.

---

# Validation

Pydantic

Responsibilities

- Request validation
- Response validation
- Configuration
- Internal DTOs

---

# Coding Provider

Current implementation

Codex

The provider is hidden behind an abstraction.

The rest of the platform must never reference Codex directly.

Future providers may include

- Claude Code
- GitHub Copilot
- Cursor
- Internal Providers

---

# Container Runtime

Docker

Every service runs inside Docker.

Every coding task runs inside its own disposable container.

Workers never execute code directly on the host machine.

---

# GitHub

GitHub owns

- Repository
- Branches
- Pull Requests
- Issues
- Labels
- Reviews
- CI

GitHub is always the source of truth.

---

# Logging

Structlog

Every log entry should contain

- Project ID
- Task ID
- Worker ID
- Graph Node
- Timestamp
- Log Level

Logs should be machine readable.

---

# Configuration

Configuration should be environment-based.

Never hardcode

- Tokens
- Secrets
- Repository URLs
- Provider Settings

All configuration is loaded through Pydantic Settings.

---

# Dependency Injection

Every service should receive dependencies through constructors.

Example

ProjectService

↓

GitHubService

↓

Repository

↓

Logger

Never instantiate dependencies directly inside services.

---

# Project Structure

```
app/

api/
graph/
services/
providers/
workers/
db/
core/
models/
schemas/

dashboard/

docker/

docs/
```

---

# External Dependencies

Required

- GitHub API
- Codex
- Docker Engine

Optional

- Slack
- Teams
- Sentry

---

# Future Extensions

The architecture should support replacing

- Redis
- Coding Provider
- Dashboard
- Queue System

without redesigning the platform.

---

# AI Agent Notes

This document defines technology choices.

Implementation agents must not replace technologies unless explicitly instructed.

All implementation must follow this stack.

---

# Acceptance Criteria

✓ Everything runs inside Docker

✓ Coding provider is replaceable

✓ GitHub remains source of truth

✓ PostgreSQL stores persistent state

✓ Redis stores temporary state

✓ Dashboard remains presentation-only

✓ FastAPI owns all business logic

✓ LangGraph owns orchestration only

---

End of Document