# 03_DATABASE_DESIGN.md

# AI Software Factory
## Database Design Specification

Version: 1.0

Status: Approved

Dependencies:

- MASTER_PLAN.md
- 01_SYSTEM_ARCHITECTURE.md

---

# Purpose

This document defines the persistent data model of the platform.

PostgreSQL is the single source of truth for application state.

GitHub remains the source of truth for repositories, issues, pull requests, and commits.

---

# Design Principles

- Normalize business data.
- Store workflow state.
- Never duplicate GitHub data unnecessarily.
- Every table has timestamps.
- Every entity has UUID primary keys.
- Use soft deletes only when recovery is required.
- Support resumable workflows.

---

# Database Modules

The database is divided into logical domains.

```
Projects
Tasks
Graphs
Workers
Providers
GitHub
Events
Settings
```

---

# Entity Relationship Overview

```text
Project
   │
   ├──────────────┐
   │              │
   ▼              ▼
Task         ProjectDocument
   │
   ▼
PullRequest
   │
   ▼
Review

Task
 │
 ▼
TaskExecution

Worker
 │
 ▼
TaskExecution

Project
 │
 ▼
GraphExecution

Project
 │
 ▼
Event
```

---

# projects

Stores project metadata.

Columns

| Name | Type |
|------|------|
| id | UUID |
| name | VARCHAR |
| description | TEXT |
| github_repository | VARCHAR |
| template | VARCHAR |
| status | ENUM |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

Status

```
CREATED
PLANNING
IMPLEMENTING
REVIEWING
COMPLETED
BLOCKED
FAILED
```

---

# project_documents

Stores generated documentation.

Examples

- Product Spec
- Architecture
- Roadmap
- Requirements

Columns

| Name |
|------|
| id |
| project_id |
| type |
| content |
| version |
| created_at |

---

# tasks

Represents implementation work.

One task equals one GitHub Issue.

Columns

| Name |
|------|
| id |
| project_id |
| github_issue_number |
| parent_task_id |
| title |
| description |
| acceptance_criteria |
| priority |
| status |
| retry_count |
| estimated_tokens |
| assigned_worker |
| created_at |
| updated_at |

Status

```
PLANNED
READY
ASSIGNED
WORKING
PR_OPEN
IN_REVIEW
REWORK
MERGED
DONE
BLOCKED
FAILED
```

---

# task_dependencies

Many-to-many dependency table.

```
task_a

depends on

task_b
```

Columns

```
task_id

depends_on_task_id
```

---

# workers

Represents active workers.

Columns

| Name |
|------|
| id |
| name |
| provider |
| status |
| current_task |
| heartbeat |
| created_at |

Status

```
IDLE

RUNNING

FAILED

OFFLINE
```

---

# task_executions

Every attempt to execute a task.

Purpose

History

Retries

Cost Tracking

Columns

| Name |
|------|
| id |
| task_id |
| worker_id |
| provider |
| started_at |
| finished_at |
| result |
| tokens |
| duration |
| logs |

Never overwrite executions.

Always create new rows.

---

# graph_executions

Stores LangGraph execution metadata.

Columns

| Name |
|------|
| id |
| project_id |
| graph_name |
| current_node |
| state_snapshot |
| status |
| started_at |
| updated_at |

Purpose

Resume execution after crashes.

---

# pull_requests

Tracks GitHub PRs.

Columns

| Name |
|------|
| id |
| task_id |
| github_pr |
| branch |
| status |
| ci_status |
| merged_at |

Status

```
OPEN

REVIEW

CHANGES_REQUESTED

READY

MERGED

CLOSED
```

---

# reviews

Stores reviewer decisions.

Columns

| Name |
|------|
| id |
| pr_id |
| reviewer |
| decision |
| comments |
| created_at |

Decision

```
PASS

FAIL

BLOCK

HUMAN_REQUIRED
```

---

# events

Immutable audit log.

Every important event creates one record.

Examples

```
PROJECT_CREATED

TASK_ASSIGNED

TASK_STARTED

PR_CREATED

CI_FAILED

REVIEW_FAILED

MERGED
```

Columns

```
id

project_id

task_id

event_type

payload

created_at
```

Never delete events.

---

# settings

System configuration.

Examples

```
default_provider

worker_count

retry_limit

github_owner

docker_image
```

Key/value storage.

---

# Indexes

Required

Projects

```
status
```

Tasks

```
status

project_id

assigned_worker
```

Workers

```
status
```

Executions

```
task_id

worker_id
```

Events

```
project_id

created_at
```

---

# Transactions

Every workflow transition must execute inside a database transaction.

Example

```
Assign Worker

↓

Update Task

↓

Insert Execution

↓

Commit
```

Never partially update workflow state.

---

# Locking Strategy

Worker assignment uses row locking.

```
SELECT *

FROM tasks

WHERE status='READY'

FOR UPDATE SKIP LOCKED

LIMIT 1;
```

This prevents two workers from selecting the same task.

---

# Repository Pattern

Application code never queries PostgreSQL directly.

Architecture

```
API

↓

Service

↓

Repository

↓

Database
```

No business logic inside repositories.

---

# Migrations

Alembic manages every schema change.

Rules

- Never modify production schema manually.
- Every migration is reversible.
- Every migration is reviewed.

---

# AI Agent Notes

Module Owner

Backend Team

Allowed

- Models
- Repositories
- Alembic
- Database Tests

Forbidden

- Business Logic
- GitHub Integration
- LangGraph Nodes

---

# Acceptance Criteria

- UUID primary keys
- Foreign keys enforced
- Transactions implemented
- Repository pattern followed
- Row locking implemented
- Execution history immutable
- Event log immutable
- Migration support enabled
- No duplicated GitHub state

---

# Related Documents

- 01_SYSTEM_ARCHITECTURE.md
- 04_LANGGRAPH_ARCHITECTURE.md
- 08_API_SPECIFICATION.md

---

End of Document