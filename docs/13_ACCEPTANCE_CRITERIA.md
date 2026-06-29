# 13_ACCEPTANCE_CRITERIA.md

# AI Software Factory
## Acceptance Criteria

Version: 1.0

Status: Approved

---

# Purpose

This document defines what “done” means for the AI Software Factory.

A task, feature, milestone, or release is not complete unless the relevant criteria in this document are satisfied.

---

# Global Acceptance Criteria

Every implemented feature must:

- follow documented architecture
- include tests
- include structured logging
- expose clear errors
- avoid hardcoded secrets
- preserve provider abstraction
- avoid unrelated changes
- update documentation when needed

---

# Backend Acceptance Criteria

Backend work is complete when:

- FastAPI endpoints are implemented
- request and response schemas exist
- service layer is used
- repository layer is used
- validation exists
- errors are structured
- tests pass
- OpenAPI docs render correctly

---

# Database Acceptance Criteria

Database work is complete when:

- SQLAlchemy models exist
- Alembic migration exists
- UUID primary keys are used
- foreign keys are enforced
- indexes are added where required
- enum values match documentation
- repository methods are tested

---

# LangGraph Acceptance Criteria

Graph work is complete when:

- graph state is serializable
- nodes receive and return state
- routing is deterministic
- checkpoints are saved
- retries are implemented
- human escalation path exists
- graph tests cover success and failure paths

---

# Agent Acceptance Criteria

Agent work is complete when:

- agent has one responsibility
- input schema is defined
- output schema is defined
- prompt is configurable
- failure modes are handled
- agent does not call other agents directly
- graph controls routing

---

# Coding Provider Acceptance Criteria

Provider work is complete when:

- provider implements CodingProvider interface
- provider runs inside sandbox
- provider receives structured context
- provider returns normalized result
- provider creates commits
- provider pushes branch
- provider runs tests
- provider-specific logic is isolated

---

# GitHub Acceptance Criteria

GitHub work is complete when:

- issues can be created
- labels can be created
- branches can be created
- pull requests can be opened
- reviews can be read
- CI status can be read
- PRs can be merged when safe
- GitHub webhooks are verified

---

# Worker Acceptance Criteria

Worker work is complete when:

- workers can be registered
- workers send heartbeats
- workers pick tasks safely
- row locking prevents duplicate assignment
- workers execute sandbox jobs
- workers update task state
- workers recover from failure

---

# Sandbox Acceptance Criteria

Sandbox work is complete when:

- every task uses a fresh container
- repository is cloned inside sandbox
- provider runs inside sandbox
- resource limits exist
- workspace is cleaned up
- host filesystem is protected

---

# Dashboard Acceptance Criteria

Dashboard work is complete when:

- projects can be viewed
- tasks can be viewed
- workers can be viewed
- logs can be viewed
- settings can be edited
- live updates work
- errors are visible
- dashboard does not contain business logic

---

# Docker Acceptance Criteria

Docker work is complete when:

- docker-compose starts all services
- API health check passes
- dashboard loads
- PostgreSQL persists data
- Redis connects
- workers start
- sandbox runner works
- environment variables are documented

---

# Auto-Merge Acceptance Criteria

A PR may be auto-merged only when:

- reviewer agent passed
- security reviewer passed
- CI passed
- no unresolved review comments
- no merge conflicts
- task is not marked risky
- branch protection allows merge

If any condition fails, the PR must not be merged.

---

# Human Escalation Criteria

Escalate when:

- retry limit is exceeded
- requirements are ambiguous
- merge conflict exists
- security risk is detected
- production secrets are involved
- destructive migration is detected
- architecture decision is required

---

# Milestone Acceptance Criteria

A milestone is complete when:

- all tasks are complete
- all tests pass
- documentation is updated
- no blocked tasks remain
- dashboard reflects correct state
- GitHub state matches database state

---

# Release Acceptance Criteria

A release is complete when:

- all milestones are complete
- Docker deployment works
- health checks pass
- system can process a sample project
- three workers can run concurrently
- at least one PR can be created, reviewed, and merged automatically

---

# Final Acceptance Test

The platform must support this end-to-end flow:

```text
User submits project idea
↓
System creates project specification
↓
System creates architecture
↓
System creates GitHub issues
↓
Workers implement tasks
↓
PRs are opened
↓
Reviewer agents review PRs
↓
CI passes
↓
Safe PRs are auto-merged
↓
Project reaches completed state
```

---

End of Document