# 00_PROJECT_OVERVIEW.md

# AI Software Factory

**Version:** 1.0

**Status:** Draft

**Document Type:** Project Overview

**Audience:** Developers, AI Agents, Architects

**Last Updated:** 2026-06-29

---

# 1. Purpose

This document defines the overall vision, objectives, scope, and guiding principles for the AI Software Factory project.

It is the entry point for every developer and AI agent working on this repository.

Every implementation task must follow the architectural principles defined here.

Detailed implementation specifications are intentionally omitted from this document and are covered by the remaining project documentation.

---

# 2. Vision

Build a fully autonomous software engineering platform capable of transforming a high-level product idea into a working software project with minimal human intervention.

The system must coordinate multiple specialized AI agents that collaborate to:

* Understand business requirements
* Produce product specifications
* Design software architecture
* Generate implementation tasks
* Implement source code
* Review implementations
* Fix review comments
* Maintain project documentation
* Produce production-ready pull requests
* Merge completed work after successful validation

The platform itself is **not** a coding assistant.

It is an orchestration platform that manages autonomous software development.

---

# 3. High-Level Goal

The user should only provide:

* Project description
* Business requirements
* Supporting documentation
* Optional implementation constraints

The platform should complete the remaining engineering lifecycle automatically.

Example:

```
User
↓

Project Description

↓

Platform

↓

Product Specification

↓

Architecture

↓

Task Planning

↓

Implementation

↓

Testing

↓

Pull Requests

↓

Review

↓

Merge
```

---

# 4. Project Objectives

The platform shall:

* Build complete software projects
* Work from predefined project templates
* Support multiple coding providers
* Execute multiple coding workers simultaneously
* Maintain project state across failures
* Automatically recover from interruptions
* Minimize required human interaction
* Produce production-quality code

---

# 5. Non-Goals

The platform is **not** intended to:

* Replace GitHub
* Replace CI/CD
* Replace source control
* Replace project management tools
* Generate code directly inside the orchestration service
* Execute code on the orchestration host

The platform coordinates work.

Specialized workers execute work.

---

# 6. Guiding Principles

## 6.1 Separation of Responsibilities

Every component owns a single responsibility.

Examples:

* Planner creates tasks
* Worker writes code
* Reviewer reviews code
* Merge agent merges code

No component should perform unrelated responsibilities.

---

## 6.2 Replaceable Providers

The platform must never depend on a specific coding provider.

Current implementation:

```
Codex
```

Future implementations:

```
Claude Code

GitHub Copilot

Cursor

Custom Internal Provider
```

Changing providers should require configuration only.

No business logic should depend on provider implementation.

---

## 6.3 GitHub Is The Source Of Truth

GitHub owns:

* repositories
* issues
* pull requests
* branches
* reviews
* CI status

The internal database stores synchronization state only.

GitHub remains authoritative.

---

## 6.4 Disposable Workers

Workers are stateless.

Every coding task starts a fresh worker.

Worker lifecycle:

```
Create

↓

Clone Repository

↓

Checkout Branch

↓

Implement Task

↓

Run Tests

↓

Push Changes

↓

Exit
```

Workers never persist state locally.

---

## 6.5 Durable Orchestration

The orchestration layer must survive:

* crashes
* restarts
* deployments
* worker failures

Project execution must continue after recovery.

---

## 6.6 Autonomous First

The system should automatically resolve problems whenever safe.

Only escalate when:

* ambiguity exists
* security risk exists
* retry limit exceeded
* human decision required

---

# 7. System Scope

Included:

* Project planning
* Task planning
* Architecture generation
* GitHub integration
* Coding worker orchestration
* Review automation
* Rework automation
* Merge automation
* Dashboard
* Monitoring

Excluded:

* Production deployment
* Infrastructure provisioning
* Billing systems
* User authentication providers
* Enterprise SSO

These may be added later.

---

# 8. High-Level Architecture

```
                User

                  │

          Project Request

                  │

        AI Software Factory

                  │

      ┌───────────┴───────────┐

Planning                 Execution

      │                        │

Product Manager          Coding Workers

Architect                Reviewers

Planner                  Security

      │                        │

      └───────────┬────────────┘

                  │

              GitHub

                  │

          Pull Requests

                  │

                 CI

                  │

              Auto Merge
```

---

# 9. Major Components

The platform consists of six major subsystems.

## 1. API Service

Responsibilities:

* expose REST API
* manage projects
* manage configuration
* receive GitHub webhooks

---

## 2. LangGraph Orchestrator

Responsibilities:

* execute project graphs
* execute task graphs
* schedule work
* route execution
* recover failures

---

## 3. Worker System

Responsibilities:

* execute coding providers
* manage sandboxes
* execute tasks
* publish results

---

## 4. GitHub Integration

Responsibilities:

* repositories
* issues
* branches
* PRs
* reviews
* merges

---

## 5. Dashboard

Responsibilities:

* visualize progress
* monitor workers
* inspect projects
* manage settings

---

## 6. Database

Responsibilities:

* project state
* execution state
* worker state
* logs
* events

---

# 10. Project Lifecycle

```
Project Created

↓

Planning

↓

Architecture

↓

Task Generation

↓

Issue Creation

↓

Task Scheduling

↓

Implementation

↓

Review

↓

Rework

↓

CI

↓

Merge

↓

Completed
```

---

# 11. Worker Lifecycle

```
Idle

↓

Assigned

↓

Sandbox Created

↓

Repository Cloned

↓

Task Executed

↓

Tests Executed

↓

Commit Created

↓

PR Updated

↓

Worker Destroyed
```

---

# 12. Repository Structure

The repository shall be organized into independent modules.

Major modules include:

* API
* Dashboard
* LangGraph
* Database
* Workers
* Coding Providers
* Docker
* Documentation

The detailed structure is defined in **01_SYSTEM_ARCHITECTURE.md**.

---

# 13. Documentation Structure

This overview is the first document in the engineering specification.

Remaining documents define implementation details.

```
00_PROJECT_OVERVIEW.md

01_SYSTEM_ARCHITECTURE.md

02_TECH_STACK.md

03_DATABASE_DESIGN.md

04_LANGGRAPH_ARCHITECTURE.md

05_AGENT_SPECIFICATIONS.md

06_CODING_PROVIDER_INTERFACE.md

07_GITHUB_WORKFLOW.md

08_API_SPECIFICATION.md

09_DASHBOARD_SPECIFICATION.md

10_DOCKER_DEPLOYMENT.md

11_IMPLEMENTATION_ROADMAP.md

12_DEVELOPMENT_GUIDELINES.md

13_ACCEPTANCE_CRITERIA.md
```

---

# 14. Success Criteria

The project is considered successful when the platform can:

* Accept a complete project description.
* Generate a technical specification.
* Create a GitHub repository from the selected template.
* Produce an implementation backlog.
* Create GitHub issues.
* Execute multiple coding workers concurrently.
* Produce pull requests.
* Respond to review comments automatically.
* Merge validated pull requests automatically.
* Recover from crashes without losing execution state.
* Replace the coding provider without changing orchestration logic.

---

# 15. Out of Scope

The following capabilities are intentionally excluded from version 1:

* Automatic production deployment
* Multi-tenant SaaS support
* Distributed worker scheduling across clusters
* Cost optimization algorithms
* Fine-grained access control
* Self-improving prompts
* Automatic architecture refactoring

These may be introduced in future releases.

---

# 16. References

* 01_SYSTEM_ARCHITECTURE.md
* 02_TECH_STACK.md
* 03_DATABASE_DESIGN.md
* 04_LANGGRAPH_ARCHITECTURE.md
* 05_AGENT_SPECIFICATIONS.md

---

**End of Document**
