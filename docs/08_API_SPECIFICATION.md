# 08_API_SPECIFICATION.md

# AI Software Factory
## Backend API Specification

Version: 1.0

Status: Approved

Dependencies

- 01_SYSTEM_ARCHITECTURE.md
- 03_DATABASE_DESIGN.md
- 04_LANGGRAPH_ARCHITECTURE.md

---

# Purpose

The FastAPI backend is the central service of the platform.

Responsibilities

- REST API
- Project Management
- Worker Management
- Webhook Processing
- Dashboard Backend
- Event Publishing

The API never performs orchestration directly.

Business workflows are delegated to LangGraph.

---

# Architecture

```
Dashboard

↓

REST API

↓

Service Layer

↓

Repositories

↓

PostgreSQL
```

Graph execution

```
REST API

↓

Graph Service

↓

LangGraph
```

---

# API Principles

- REST only
- JSON only
- Async endpoints
- Typed DTOs
- No business logic in routers
- Services own business logic
- Repositories own persistence

---

# Modules

```
Projects

Tasks

Workers

GitHub

Settings

Events

Health
```

---

# Projects API

## Create Project

POST

```
/api/projects
```

Request

```json
{
  "name": "",
  "description": "",
  "repository": "",
  "template": "backend",
  "documents": []
}
```

Response

```
Project
```

Automatically starts

Project Graph.

---

## List Projects

GET

```
/api/projects
```

---

## Get Project

GET

```
/api/projects/{id}
```

---

## Delete Project

DELETE

```
/api/projects/{id}
```

Deletes only platform metadata.

Never delete GitHub repository.

---

# Task API

List

```
GET /api/tasks
```

Details

```
GET /api/tasks/{id}
```

Retry

```
POST /api/tasks/{id}/retry
```

Pause

```
POST /api/tasks/{id}/pause
```

Resume

```
POST /api/tasks/{id}/resume
```

---

# Worker API

Workers

```
GET /api/workers
```

Worker Details

```
GET /api/workers/{id}
```

Pause

```
POST /api/workers/{id}/pause
```

Resume

```
POST /api/workers/{id}/resume
```

---

# Settings API

```
GET /api/settings

PUT /api/settings
```

Configuration

- Provider
- Worker Count
- Retry Limit
- GitHub Owner
- Templates

---

# GitHub Webhooks

Endpoint

```
POST /api/github/webhook
```

Supported

- issues
- issue_comment
- pull_request
- pull_request_review
- check_suite
- check_run
- push

Never expose webhook processing publicly without signature verification.

---

# Events API

List

```
GET /api/events
```

Project Events

```
GET /api/projects/{id}/events
```

Task Events

```
GET /api/tasks/{id}/events
```

Events are read-only.

---

# Health

```
GET /health
```

Checks

- PostgreSQL
- Redis
- GitHub
- Docker
- Worker Status

---

# DTOs

Every endpoint uses

Pydantic models.

Never expose ORM models.

Example

```
ProjectCreate

ProjectResponse

TaskResponse

WorkerResponse
```

---

# Service Layer

Every router

↓

Service

↓

Repository

Never

Router

↓

Database

---

# Repository Layer

Repositories own

- Queries
- Transactions
- Persistence

Repositories never

- Call GitHub
- Execute Graphs
- Execute Providers

---

# Event Bus

Every important action emits an event.

Example

```
ProjectCreated

TaskCreated

TaskAssigned

PRCreated

PRMerged

WorkerStarted

WorkerStopped
```

Consumers

- Dashboard
- LangGraph
- Notifications
- Audit Log

The API publishes events.

It never consumes them directly.

---

# Authentication

Version 1

Single admin token.

Future

JWT

OAuth

GitHub Login

Enterprise SSO

Authentication should be isolated behind middleware.

---

# Error Format

Every endpoint returns

```json
{
    "success": false,
    "error": {
        "code": "",
        "message": ""
    }
}
```

Never expose stack traces.

---

# Logging

Every request logs

- Request ID
- Project ID
- User
- Duration
- Status Code

Structured logs only.

---

# Dependency Injection

All services resolved through FastAPI DI.

Never instantiate services manually.

---

# Folder Structure

```
app/

api/

services/

repositories/

schemas/

models/

core/

graph/
```

---

# AI Agent Notes

Owner

Backend Team

Allowed

- Routers
- DTOs
- Services
- Middleware

Forbidden

- Graph Logic
- Provider Logic
- GitHub Logic

---

# Acceptance Criteria

✓ RESTful

✓ Async

✓ Typed DTOs

✓ Service Layer

✓ Repository Layer

✓ Event Publishing

✓ Health Endpoints

✓ Webhook Support

✓ Structured Errors

✓ Dependency Injection

---

# Related Documents

03_DATABASE_DESIGN.md

04_LANGGRAPH_ARCHITECTURE.md

07_GITHUB_WORKFLOW.md

09_DASHBOARD_SPECIFICATION.md

---

End of Document