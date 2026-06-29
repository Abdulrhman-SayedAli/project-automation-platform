# 06_CODING_PROVIDER_INTERFACE.md

# AI Software Factory
## Coding Provider Interface

Version: 1.0

Status: Approved

Dependencies

- 04_LANGGRAPH_ARCHITECTURE.md
- 05_AGENT_SPECIFICATIONS.md

---

# Purpose

This document defines the abstraction between the orchestration platform and any coding engine.

The platform must never depend directly on Codex, Claude Code, GitHub Copilot, Cursor, or any future provider.

All coding providers must implement the same interface.

---

# Design Goals

The provider layer must:

- Hide provider implementation details.
- Support multiple providers.
- Be easily replaceable.
- Return normalized execution results.
- Execute inside an isolated workspace.

---

# Provider Responsibilities

A coding provider is responsible for:

- Understanding the assigned task.
- Reading the repository.
- Modifying files.
- Running project commands.
- Committing changes.
- Pushing branches.
- Returning execution results.

The provider is **not** responsible for:

- Planning
- Task prioritization
- GitHub issue management
- Workflow orchestration
- Retry logic

---

# Provider Architecture

```
LangGraph

↓

CodingProvider Interface

↓

Provider Implementation

↓

Sandbox

↓

Repository
```

LangGraph only knows about the interface.

---

# Provider Interface

Every provider must implement:

```python
class CodingProvider(ABC):

    async def run_task(
        self,
        context: CodingContext
    ) -> CodingResult:
        ...
```

---

# Coding Context

Every execution receives the same context.

```python
class CodingContext:

    project

    repository

    task

    branch

    workspace

    commands

    settings
```

---

# Repository Context

Contains

```
Repository URL

Default Branch

Working Branch

Local Path

Project Type

Framework
```

---

# Task Context

Contains

```
Title

Description

Acceptance Criteria

Dependencies

Priority

Related Files

Labels
```

---

# Workspace Context

Contains

```
Workspace Path

Temporary Directory

Environment Variables

Container ID
```

---

# Provider Result

Every provider returns

```python
class CodingResult:

    success: bool

    summary: str

    files_changed: list[str]

    commit_sha: str | None

    branch: str

    tests_passed: bool

    execution_time: float

    warnings: list[str]

    errors: list[str]
```

No provider-specific objects.

---

# Provider Lifecycle

```
Receive Context

↓

Load Repository

↓

Analyze Task

↓

Implement

↓

Run Tests

↓

Commit

↓

Push

↓

Return Result
```

---

# Workspace Rules

Every execution uses a fresh workspace.

Workflow

```
Create Container

↓

Clone Repository

↓

Checkout Branch

↓

Run Provider

↓

Destroy Container
```

Providers never execute on the host machine.

---

# Branch Rules

The provider must:

Create branch if missing.

Never work on main.

Never merge.

Never delete branches.

Branch format

```
ai/project-{project}/task-{task}
```

---

# Commit Rules

Every execution creates meaningful commits.

Format

```
type(scope): description

Examples

feat(api): add project endpoint

fix(worker): retry docker failures

refactor(graph): simplify routing
```

Never create empty commits.

---

# Test Rules

The provider must execute all configured commands.

Example

```
lint

typecheck

unit tests
```

If tests fail

↓

Return failure.

Never skip tests unless explicitly configured.

---

# Prompt Rules

The provider receives a generated prompt.

The provider never builds prompts.

Prompt generation belongs to the orchestration layer.

---

# Provider Configuration

Configuration example

```yaml
provider:

  name: codex

  model: gpt-5-codex

  timeout: 1800

  max_iterations: 30

  temperature: 0.1

  auto_commit: true

  run_tests: true
```

Configuration must not be hardcoded.

---

# Error Categories

Recoverable

```
Timeout

Temporary network

Provider unavailable

Container restart
```

Fatal

```
Repository corrupted

Invalid workspace

Missing branch

Invalid task
```

---

# Provider Factory

All providers are created through a factory.

Example

```python
provider = ProviderFactory.create(
    settings.provider
)
```

Never instantiate providers directly.

---

# Supported Providers

Version 1

```
CodexProvider
```

Planned

```
ClaudeCodeProvider

GitHubCopilotProvider

CursorProvider
```

No orchestration changes should be required to support new providers.

---

# Logging

Every execution logs

- Provider
- Project
- Task
- Branch
- Duration
- Token usage
- Test results
- Exit status

Logs must be structured.

---

# Security Rules

Providers may

- Read repository
- Modify files
- Run configured commands
- Commit
- Push branch

Providers may NOT

- Merge PRs
- Delete repositories
- Change secrets
- Modify infrastructure outside the workspace
- Access production systems

---

# AI Agent Notes

Owner

Provider Team

Allowed

- Provider implementations
- Prompt adapters
- Workspace execution
- Provider configuration

Forbidden

- Workflow routing
- Database schema
- GitHub orchestration
- Project planning

---

# Acceptance Criteria

✓ Single provider interface

✓ No provider-specific code in LangGraph

✓ Disposable workspace

✓ Structured result object

✓ Automatic test execution

✓ Automatic commits

✓ Automatic push

✓ Configurable provider

✓ Replaceable without orchestration changes

---

# Related Documents

04_LANGGRAPH_ARCHITECTURE.md

05_AGENT_SPECIFICATIONS.md

07_GITHUB_WORKFLOW.md

11_IMPLEMENTATION_ROADMAP.md

---

End of Document