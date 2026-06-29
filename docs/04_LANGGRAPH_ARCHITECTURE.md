# 04_LANGGRAPH_ARCHITECTURE.md

# AI Software Factory
## LangGraph Architecture Specification

Version: 1.0

Status: Approved

Dependencies

- 01_SYSTEM_ARCHITECTURE.md
- 03_DATABASE_DESIGN.md

---

# Purpose

This document defines the orchestration engine of the AI Software Factory.

LangGraph is responsible for coordinating all autonomous workflows.

It is the brain of the platform.

It never edits source code directly.

It only decides:

- what happens
- when it happens
- which worker executes it

---

# Core Responsibilities

LangGraph owns

- Project lifecycle
- Task lifecycle
- Retry logic
- Failure recovery
- State transitions
- Worker scheduling
- Review routing
- Escalation

LangGraph never owns

- GitHub
- Docker
- Database logic
- Coding provider implementation

---

# Architecture

There are only **two graphs**.

```
Project Graph

Task Graph
```

Everything else is a node.

Do NOT create dozens of graphs.

---

# Project Graph

Runs once per project.

```
Create Project

↓

Analyze Requirements

↓

Generate Product Specification

↓

Generate Architecture

↓

Generate Tasks

↓

Resolve Dependencies

↓

Create GitHub Issues

↓

Queue Tasks

↓

Completed
```

Output

- Product Spec
- Architecture
- Task Backlog
- GitHub Issues

---

# Task Graph

Runs once per task.

```
Select Task

↓

Assign Worker

↓

Prepare Workspace

↓

Execute Coding Provider

↓

Run Tests

↓

Commit

↓

Push

↓

Open PR

↓

Review

↓

Decision
```

Possible outcomes

```
Merged

Rework

Blocked
```

---

# Graph State

Every graph owns one state object.

Example

```python
class GraphState(TypedDict):

    project_id: UUID

    task_id: UUID | None

    current_node: str

    status: str

    retry_count: int

    worker_id: UUID | None

    provider: str

    github: GitHubContext

    execution: ExecutionContext
```

The state object must be serializable.

---

# Node Rules

Every node

Must

- receive state
- return state

Never

- modify globals
- access unrelated services
- perform long business logic

Node structure

```
Input State

↓

Execute

↓

Output State
```

---

# Project Graph Nodes

## Intake

Reads

- Project description
- Documentation
- Constraints

Produces

Normalized project request.

---

## Product Manager

Produces

- Product Specification
- User Stories
- Acceptance Criteria

---

## Architect

Produces

- Architecture
- Modules
- Risks
- Technical decisions

---

## Planner

Produces

- GitHub Issues
- Dependencies
- Priorities

---

## Dependency Resolver

Builds

Task dependency graph.

---

## GitHub Bootstrap

Creates

- Repository (optional)
- Labels
- Issues
- Milestones

---

# Task Graph Nodes

## Pick Task

Gets next READY task.

Worker-safe.

Uses row locking.

---

## Assign Worker

Reserves worker.

Updates database.

---

## Prepare Workspace

Delegates to Docker Service.

Returns

Workspace path.

---

## Execute Provider

Delegates

```
CodingProvider.run_task()
```

Never call Codex directly.

---

## Test Node

Runs

- lint
- unit tests
- type checking

Stores results.

---

## Commit Node

Commits

Changes.

Pushes branch.

---

## PR Node

Creates

Or updates

GitHub Pull Request.

---

## Reviewer Node

Reviews

- Acceptance Criteria
- Test Results
- Code Quality

Outputs

```
PASS

FAIL

BLOCK
```

---

## Decision Node

Routes execution.

```
PASS

↓

Wait For CI

↓

Merge
```

```
FAIL

↓

Rework
```

```
BLOCK

↓

Human
```

---

# Conditional Routing

Example

```python
if review == PASS:

    return "wait_ci"

if review == FAIL:

    return "rework"

return "blocked"
```

Keep routing deterministic.

---

# Retry Policy

Retry only

- CI failure
- Provider timeout
- Temporary GitHub failure
- Temporary Docker failure

Maximum retries

```
3
```

After retry limit

↓

BLOCKED

---

# Human Escalation

Escalate only

- ambiguous requirements
- security issue
- merge conflict
- architecture conflict
- retry limit reached

Never ask humans to fix trivial issues.

---

# Checkpointing

Checkpoint after every node.

Never checkpoint during node execution.

```
Node Finished

↓

Save State

↓

Continue
```

Recovery should resume from the latest checkpoint.

---

# Parallel Execution

Project Graph

Single instance.

Task Graph

Multiple instances.

V1

```
3 concurrent workers
```

Future

Unlimited workers.

---

# Error Handling

Recoverable

- timeout
- network
- docker
- provider
- CI

Fatal

- corrupted state
- invalid architecture
- missing repository

Fatal errors terminate graph execution.

---

# Service Dependencies

Allowed

```
Graph

↓

Project Service

↓

GitHub Service

↓

Repository
```

Forbidden

```
Graph

↓

Database Session
```

```
Graph

↓

GitHub REST
```

```
Graph

↓

Docker SDK
```

Everything goes through services.

---

# Provider Abstraction

Never reference

```
Codex
```

Always use

```python
provider.run_task(...)
```

Graph must not know

- provider name
- prompt format
- execution method

---

# State Machine

Project

```
CREATED

↓

PLANNING

↓

TASKS_CREATED

↓

IMPLEMENTING

↓

COMPLETED
```

Task

```
READY

↓

WORKING

↓

PR

↓

REVIEW

↓

DONE
```

Worker

```
IDLE

↓

RUNNING

↓

FINISHED
```

Never mix state machines.

---

# AI Agent Notes

Owner

Graph Team

Allowed

- Graphs
- Nodes
- Routing
- State

Forbidden

- GitHub implementation
- Docker
- Provider logic
- Database schema

---

# Acceptance Criteria

✓ Two graphs only

✓ Stateless nodes

✓ Serializable state

✓ Checkpoint after every node

✓ Deterministic routing

✓ Retry policy implemented

✓ Human escalation implemented

✓ Parallel task execution

✓ Provider abstraction preserved

✓ No direct infrastructure access

---

# Related Documents

03_DATABASE_DESIGN.md

05_AGENT_SPECIFICATIONS.md

06_CODING_PROVIDER_INTERFACE.md

11_IMPLEMENTATION_ROADMAP.md

---

End of Document