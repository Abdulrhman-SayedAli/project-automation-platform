# 09_DASHBOARD_SPECIFICATION.md

# AI Software Factory
## Dashboard Specification

Version: 1.0

Status: Approved

Dependencies

- 08_API_SPECIFICATION.md

---

# Purpose

The dashboard is the operational interface for the AI Software Factory.

It is **not** responsible for business logic.

It visualizes platform state and allows operators to trigger actions.

All operations are executed through the REST API.

---

# Goals

The dashboard should allow an operator to:

- Create projects
- Monitor progress
- View running workers
- Inspect LangGraph execution
- Monitor GitHub activity
- Retry failed tasks
- Pause workers
- Resume workers
- View logs
- Configure providers

---

# Technology

Framework

```
Next.js
```

Language

```
TypeScript
```

UI

```
shadcn/ui

TailwindCSS
```

State

```
TanStack Query

React Context
```

Charts

```
Recharts
```

---

# Layout

```
Sidebar

↓

Dashboard

↓

Content

↓

Right Activity Panel
```

---

# Sidebar

Sections

```
Dashboard

Projects

Tasks

Workers

Graphs

Events

Settings
```

---

# Dashboard Home

Displays

```
Projects

Running Workers

Running Graphs

Open PRs

Failed Tasks

Blocked Tasks

Provider

System Health
```

Cards update automatically.

---

# Projects Page

Table

Columns

```
Name

Status

Repository

Progress

Tasks

Workers

Created
```

Actions

```
Open

Pause

Resume

Delete
```

---

# Project Details

Tabs

```
Overview

Tasks

Pull Requests

Graphs

Events

Documents

Settings
```

Overview

Displays

- Product Spec
- Architecture
- Progress
- Statistics

---

# Task View

Displays

```
Task Status

Assigned Worker

Current Graph Node

Retries

Execution History

Related PR
```

Actions

```
Retry

Pause

Cancel
```

---

# Worker View

Displays

```
Worker Name

Provider

Current Task

CPU

Memory

Duration

Status
```

Statuses

```
Idle

Running

Offline

Failed
```

Actions

```
Restart

Pause

Resume
```

---

# Graph View

Visualizes

```
Project Graph

Task Graph
```

Highlights

Current Node

Completed Nodes

Failed Nodes

Pending Nodes

---

# Pull Request View

Displays

```
PR Number

Task

Branch

CI Status

Review Status

Merge Status
```

Actions

```
Open GitHub

View Logs

Retry Review
```

---

# Events View

Timeline

Examples

```
Project Created

Worker Started

PR Created

Review Failed

Merged

Worker Restarted
```

Supports filtering.

---

# Logs

Filter

```
Project

Worker

Task

Level

Time
```

Searchable

Downloadable

---

# Settings

Configuration

```
Coding Provider

Worker Count

Retry Limit

GitHub Repository

Templates

Logging
```

Future

LLM Settings

Notifications

Secrets

---

# Live Updates

Dashboard receives updates through

```
WebSocket
```

No polling.

Events

```
Worker Started

Worker Finished

Task Updated

Graph Updated

PR Updated

CI Updated
```

---

# Notifications

Types

```
Success

Warning

Error

Info
```

Examples

```
Project Completed

Worker Failed

CI Failed

Merge Completed
```

---

# Search

Global search

Supports

```
Projects

Tasks

Workers

PRs
```

---

# Theme

Support

```
Light

Dark

System
```

---

# Permissions

Version 1

Single administrator.

Future

```
Admin

Operator

Viewer
```

---

# Folder Structure

```
dashboard/

components/

pages/

hooks/

services/

types/

layouts/

providers/

styles/
```

---

# API Usage

Dashboard never accesses

```
Database

LangGraph

GitHub
```

Everything goes through

```
FastAPI
```

---

# Performance

Requirements

- Lazy loading
- Pagination
- Virtual tables
- WebSocket updates
- Cached queries

---

# AI Agent Notes

Owner

Frontend Team

Allowed

- UI
- Components
- Routing
- API Client

Forbidden

- Business Logic
- Graph Logic
- Database

---

# Acceptance Criteria

✓ Responsive

✓ Dark Mode

✓ WebSocket Updates

✓ No Business Logic

✓ API Driven

✓ Search

✓ Filtering

✓ Live Worker Status

✓ Live Graph Status

✓ Project Monitoring

---

# Related Documents

08_API_SPECIFICATION.md

10_DOCKER_DEPLOYMENT.md

11_IMPLEMENTATION_ROADMAP.md

---

End of Document