# 14_PROJECT_RULES.md

# AI Software Factory
## Engineering Rules & Governance

Version: 1.0

Status: Mandatory

---

# Purpose

This document defines the non-negotiable engineering rules of the platform.

These rules exist to keep the architecture maintainable as autonomous agents contribute to the codebase.

Every implementation must comply with these rules.

---

# Rule 1 — Architecture First

No implementation may contradict the documented architecture.

If the implementation requires changing the architecture:

1. Update the documentation.
2. Review the change.
3. Implement afterward.

Never silently change architecture through code.

---

# Rule 2 — GitHub Is The Source Of Truth

GitHub owns

- Repository
- Issues
- Pull Requests
- Branches
- Reviews
- Merge History

Never duplicate Git state inside PostgreSQL.

---

# Rule 3 — LangGraph Owns Workflow

Only LangGraph decides

- Task routing
- Retries
- Scheduling
- Escalation
- Workflow transitions

No other component may make workflow decisions.

---

# Rule 4 — Workers Execute Only

Workers never

- Plan work
- Schedule work
- Merge PRs
- Review architecture

Workers execute assigned tasks only.

---

# Rule 5 — Agents Are Specialists

Every AI agent owns exactly one responsibility.

Examples

✓ Planner

✓ Reviewer

✓ Architect

✗ Planner + Reviewer

✗ Architect + Coding

---

# Rule 6 — Provider Independence

Business logic must never depend on

- Codex
- Claude
- Cursor
- GitHub Copilot

Only the Provider Interface may reference provider implementations.

---

# Rule 7 — Disposable Execution

Every coding task executes inside a fresh sandbox.

Never reuse workspaces.

Never execute code on the host.

---

# Rule 8 — Stateless Services

API

Workers

Agents

Providers

must remain stateless.

Persistent state belongs in PostgreSQL.

---

# Rule 9 — Immutable Events

Events are append-only.

Never edit historical events.

Never delete historical events.

---

# Rule 10 — Single Responsibility

Every module owns one responsibility.

If a module has multiple unrelated responsibilities,

split it.

---

# Rule 11 — Dependency Direction

Allowed

```
API

↓

Services

↓

Repositories

↓

Database
```

Forbidden

```
API

↓

Database
```

Allowed

```
Graph

↓

Provider Interface
```

Forbidden

```
Graph

↓

Codex Provider
```

---

# Rule 12 — One Task, One Branch

Every implementation task owns

- one GitHub Issue
- one branch
- one Pull Request

Never combine unrelated work.

---

# Rule 13 — One PR, One Purpose

Pull Requests should solve exactly one problem.

No mixed features.

No unrelated refactoring.

---

# Rule 14 — Retry Safety

Retries must be idempotent.

Executing the same task twice must not corrupt state.

---

# Rule 15 — Human Escalation

Humans should only be involved when

- ambiguity exists
- security risk exists
- architecture decision required
- retry limit exceeded
- merge conflict cannot be resolved

Everything else should remain autonomous.

---

# Rule 16 — Testing

Every feature requires

- Unit Tests
- Integration Tests (when applicable)

No feature is complete without automated tests.

---

# Rule 17 — Logging

Every important operation logs

- Project
- Task
- Worker
- Duration
- Result

Logs must be structured.

---

# Rule 18 — Configuration

Never hardcode

- Tokens
- URLs
- Providers
- Limits
- Secrets

Everything is configurable.

---

# Rule 19 — Security

Never

- Commit secrets
- Execute arbitrary host commands
- Access production infrastructure
- Modify repositories outside the assigned workspace

---

# Rule 20 — Documentation

Every architectural change requires updating the relevant documentation.

Documentation is part of the implementation.

---

# Rule 21 — Versioning

Breaking architectural changes require increasing the documentation version.

All affected documents must be updated together.

---

# Rule 22 — Backwards Compatibility

Public interfaces should remain stable whenever possible.

When breaking changes are required:

- document them
- migrate callers
- remove deprecated behavior only after migration

---

# Rule 23 — Observability

Every long-running operation must expose

- status
- progress
- logs
- failure reason

Operators should never need to inspect the database directly.

---

# Rule 24 — AI Agent Conduct

AI agents must never

- invent architecture
- skip acceptance criteria
- modify unrelated modules
- bypass service boundaries
- ignore documented dependencies

When uncertain,

stop and escalate.

---

# Rule 25 — Definition of Success

The platform is successful when a user can

1. Describe a project.
2. Select a template.
3. Review the generated specification.
4. Start execution.
5. Watch autonomous implementation.
6. Receive reviewed, tested, and merged pull requests.

without manually coordinating individual coding tasks.

---

# Rule 26 — Future Evolution

New features should extend the platform through

- new graph nodes
- new agents
- new provider implementations
- new services

Avoid modifying stable interfaces when extension points already exist.

---

# Final Rule

**Correct architecture is more important than fast implementation.**

The platform is expected to evolve for years.

Optimize for maintainability, extensibility, and correctness—not short-term speed.

---

End of Document