# 10_DOCKER_DEPLOYMENT.md

# AI Software Factory
## Docker & Deployment Specification

Version: 1.0

Status: Approved

Dependencies

- 01_SYSTEM_ARCHITECTURE.md
- 02_TECH_STACK.md

---

# Purpose

Every component of the platform must run inside Docker.

Development and production environments should be nearly identical.

No application component should depend on the host machine.

---

# Goals

- One-command startup
- Isolated services
- Disposable coding environments
- Easy deployment
- Easy scaling

---

# Services

V1 deployment contains

```
api

dashboard

worker

postgres

redis

sandbox-runner
```

---

# Architecture

```
                Dashboard
                     │
                     ▼
                  FastAPI
                     │
        ┌────────────┴────────────┐
        │                         │
      Redis                  PostgreSQL
        │
        ▼
   Worker Manager
        │
        ▼
 Sandbox Containers
        │
        ▼
 GitHub Repository
```

---

# Docker Compose

Root

```
docker-compose.yml
```

Services

```
api

dashboard

postgres

redis

worker

sandbox-runner
```

Future

```
nginx

prometheus

grafana

sentry
```

---

# API Container

Responsibilities

- REST API
- Webhooks
- Authentication
- Event Publishing

Must not

- Execute coding tasks

---

# Dashboard Container

Responsibilities

- UI
- WebSocket Client

Must remain stateless.

---

# Worker Container

Responsibilities

- Execute LangGraph
- Schedule workers
- Start sandboxes

Workers never edit repositories directly.

---

# Sandbox Runner

Purpose

Creates disposable coding environments.

Every task receives

```
Fresh Container

↓

Clone Repository

↓

Execute Provider

↓

Destroy Container
```

Never reuse containers.

---

# PostgreSQL

Stores

- Projects
- Tasks
- Workers
- Events
- Graph Metadata

Persistent Volume required.

---

# Redis

Stores

- Queue
- Locks
- Cache
- Pub/Sub

Redis data is disposable.

---

# Networks

Single internal network.

```
platform-network
```

All services communicate internally.

Expose only

```
API

Dashboard
```

---

# Volumes

Persistent

```
postgres-data
```

Temporary

```
sandbox-workspaces
```

Never persist coding containers.

---

# Environment Variables

API

```
DATABASE_URL

REDIS_URL

GITHUB_TOKEN

CODING_PROVIDER

LOG_LEVEL
```

Worker

```
WORKER_COUNT

MAX_RETRIES

SANDBOX_IMAGE
```

Dashboard

```
API_URL
```

---

# Health Checks

API

```
/health
```

Worker

Heartbeat every

```
30 seconds
```

Postgres

Native health check.

Redis

PING.

---

# Sandbox Image

Base image

```
Ubuntu
```

Contains

- Git
- Python
- Node
- Docker CLI
- Build tools

Provider-specific software installed separately.

---

# Resource Limits

Every sandbox

CPU

```
2 cores
```

Memory

```
4 GB
```

Timeout

```
30 minutes
```

Limits configurable.

---

# Logging

Every container outputs

stdout

stderr

Structured JSON logs.

No local log files.

---

# Restart Policy

API

```
unless-stopped
```

Worker

```
always
```

Dashboard

```
unless-stopped
```

Postgres

```
always
```

Redis

```
always
```

---

# Scaling

V1

```
1 API

1 Worker

3 Internal Workers
```

Future

```
N Worker Containers

Load Balancer

Kubernetes
```

Worker count configurable.

---

# Secrets

Never bake secrets into images.

Use

```
.env

Docker Secrets (future)
```

Required

```
GitHub Token

Provider Keys
```

---

# Production

Deployment target

```
Docker Compose
```

Future

```
Kubernetes

Azure Container Apps

AWS ECS
```

No architecture changes required.

---

# AI Agent Notes

Owner

Infrastructure Team

Allowed

- Dockerfiles
- Compose
- Networks
- Health Checks

Forbidden

- Business Logic
- Database Schema
- Graph Logic

---

# Acceptance Criteria

✓ Everything Dockerized

✓ One-command startup

✓ Disposable sandboxes

✓ Persistent PostgreSQL

✓ Internal networking

✓ Configurable resources

✓ Health checks

✓ Environment-based configuration

✓ Easy horizontal scaling

---

# Related Documents

02_TECH_STACK.md

04_LANGGRAPH_ARCHITECTURE.md

11_IMPLEMENTATION_ROADMAP.md

---

End of Document