# 05_AGENT_SPECIFICATIONS.md

# AI Software Factory
## Agent Specifications

Version: 1.0

Status: Approved

Dependencies

- 04_LANGGRAPH_ARCHITECTURE.md

---

# Purpose

This document defines every AI agent used by the platform.

Agents are **specialists**.

They do not communicate directly.

All communication goes through LangGraph.

Agents must never own workflow state.

---

# Agent Design Principles

Every agent:

- Has one responsibility.
- Receives structured input.
- Produces structured output.
- Never edits unrelated project state.
- Never calls another agent directly.
- Never makes infrastructure decisions.

---

# Agent Lifecycle

```
Receive Context

↓

Execute

↓

Return Result

↓

Terminate
```

Agents are stateless.

---

# Shared Context

Every agent receives:

```python
ProjectContext

TaskContext

RepositoryContext

ExecutionContext

Settings
```

Agents must treat all context as read-only.

---

# Available Tools

Depending on the agent:

- GitHub Service
- Project Service
- Task Service
- Provider Service
- Docker Service
- Documentation Service

Agents must use services.

Never call external APIs directly.

---

# 1. Intake Agent

Purpose

Convert the user request into a normalized project request.

Input

- Project description
- User documentation
- Constraints

Output

```python
NormalizedProject
```

Responsibilities

- Understand project
- Detect missing information
- Normalize input

Never

- Create tasks
- Generate architecture
- Write code

---

# 2. Product Manager Agent

Purpose

Transform business requirements into implementable requirements.

Output

- Product Specification
- User Stories
- Acceptance Criteria
- Functional Requirements

Responsibilities

- Split business requirements
- Identify actors
- Define success

Never

- Decide technology
- Write code

---

# 3. Architect Agent

Purpose

Design the technical solution.

Produces

- Modules
- Components
- APIs
- Database outline
- Risks

Responsibilities

- Architecture
- Module boundaries
- Dependency rules

Never

- Implement features
- Generate GitHub issues

---

# 4. Planner Agent

Purpose

Create implementation tasks.

Produces

GitHub-ready tasks.

Responsibilities

- Split work
- Estimate complexity
- Detect dependencies
- Prioritize work

Every task should be completable by one worker.

Bad

```
Build CRM
```

Good

```
Implement Lead CRUD API
```

---

# 5. Dependency Resolver

Purpose

Create task dependency graph.

Input

Task list.

Output

Directed Acyclic Graph.

Responsibilities

- Detect blockers
- Detect independent tasks

Never create circular dependencies.

---

# 6. Reviewer Agent

Purpose

Validate implementation.

Input

- Task
- PR
- Test results

Checks

- Acceptance Criteria
- Scope
- Quality
- Architecture

Output

```
PASS

FAIL

BLOCK
```

Reviewer never edits code.

---

# 7. Security Reviewer

Purpose

Protect the repository.

Checks

- Secrets
- Permissions
- Dangerous code
- Dependency risks
- Unsafe changes

If unsafe

↓

BLOCK

---

# 8. Rework Agent

Purpose

Handle failed reviews.

Input

Review comments.

Responsibilities

- Explain failures
- Generate rework instructions

Never modify code directly.

Rework is executed by a coding worker.

---

# 9. Merge Agent

Purpose

Merge validated Pull Requests.

Requirements

- Review passed
- Security passed
- CI passed
- Branch up to date

Otherwise

↓

Do not merge.

---

# 10. Escalation Agent

Purpose

Determine when humans must intervene.

Escalation reasons

- Ambiguous requirement
- Architecture conflict
- Merge conflict
- Retry limit exceeded
- Repository corruption
- Missing information

Everything else should be resolved automatically.

---

# Coding Workers

Coding workers are NOT agents.

They are execution engines.

Current implementation

```
Codex
```

Future

```
Claude

Cursor

GitHub Copilot
```

Workers execute.

Agents decide.

---

# Communication Rules

Allowed

```
Graph

↓

Planner

↓

Graph

↓

Worker
```

Forbidden

```
Planner

↓

Reviewer
```

```
Architect

↓

Planner
```

All communication returns to LangGraph.

---

# Agent Contracts

Every agent must expose

```python
run(
    context
) -> AgentResult
```

Result

```python
class AgentResult:

    status

    output

    messages

    warnings

    next_action
```

---

# Agent Configuration

Every agent has

- System Prompt
- Temperature
- Available Tools
- Maximum Iterations
- Timeout

Configuration belongs outside code.

---

# Failure Handling

If an agent fails

↓

Graph decides

- Retry
- Escalate
- Abort

Agents never retry themselves.

---

# AI Agent Notes

Owner

Graph Team

Allowed

- Agent prompts
- Agent contracts
- Agent configuration

Forbidden

- GitHub logic
- Provider logic
- Database implementation

---

# Acceptance Criteria

✓ Single responsibility

✓ Stateless

✓ Structured input

✓ Structured output

✓ Tool-based execution

✓ No direct communication

✓ No business state ownership

✓ Graph controls workflow

✓ Workers execute code

✓ Agents make decisions

---

# Related Documents

04_LANGGRAPH_ARCHITECTURE.md

06_CODING_PROVIDER_INTERFACE.md

11_IMPLEMENTATION_ROADMAP.md

---

End of Document