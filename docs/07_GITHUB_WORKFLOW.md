# 07_GITHUB_WORKFLOW.md

# AI Software Factory
## GitHub Workflow Specification

Version: 1.0

Status: Approved

Dependencies

- 04_LANGGRAPH_ARCHITECTURE.md
- 05_AGENT_SPECIFICATIONS.md
- 06_CODING_PROVIDER_INTERFACE.md

---

# Purpose

GitHub is the collaboration platform for the AI Software Factory.

Every implementation task must flow through GitHub.

GitHub is the source of truth for:

- Repository
- Branches
- Issues
- Pull Requests
- Reviews
- CI
- Merge History

The internal database stores synchronization state only.

---

# Repository Lifecycle

Project Created

↓

Repository Selected

↓

Template Cloned

↓

Labels Created

↓

Issues Created

↓

Workers Start

---

# Repository Structure

Expected repository

```
.github/
docs/
backend/
frontend/
flutter/
```

The automation platform never creates project structure.

Templates provide the initial structure.

---

# Labels

Required labels

```
ai-ready

ai-working

ai-review

ai-rework

ai-blocked

needs-human

security

documentation
```

Labels are managed automatically.

Humans should rarely modify labels.

---

# Milestones

Optional.

Planner Agent may create milestones.

Example

```
Authentication

Dashboard

Notifications

Deployment
```

---

# GitHub Issue

Every task equals one issue.

One issue

↓

One branch

↓

One PR

Never combine multiple tasks into one PR.

---

# Issue Template

Each generated issue contains

- Summary
- Description
- Acceptance Criteria
- Dependencies
- Labels

Example

```
Title

Create Project API

Description

Implement REST endpoint...

Acceptance

- endpoint exists
- validation
- tests
```

---

# Branch Strategy

Branch format

```
ai/project-{project_id}/task-{task_id}
```

Examples

```
ai/project-1/task-18

ai/project-2/task-43
```

Never commit directly to main.

---

# Branch Ownership

One worker owns one branch.

Branches are never shared between workers.

---

# Pull Request Lifecycle

```
Branch Created

↓

Commit

↓

Push

↓

Open PR

↓

Review

↓

CI

↓

Merge
```

---

# Pull Request Template

Every PR contains

```
Summary

Issue Reference

Files Changed

Acceptance Criteria

Tests

Risks
```

Generated automatically.

---

# Review Workflow

Reviewer Agent executes first.

Possible outcomes

```
PASS

FAIL

BLOCK
```

PASS

↓

Wait CI

FAIL

↓

Rework

BLOCK

↓

Human

---

# Review Comments

When review fails

Reviewer produces

- Explanation
- Required changes
- Priority

Coding Provider receives these comments during rework.

---

# Rework Workflow

```
Review Failed

↓

Rework Task

↓

Same Branch

↓

New Commit

↓

Update PR

↓

Review Again
```

Never create another PR.

---

# CI Workflow

Every PR triggers

```
Lint

↓

Formatting

↓

Type Check

↓

Unit Tests

↓

Integration Tests
```

If configured

↓

Security Scan

---

# Merge Rules

Auto merge allowed only when

- Review passed
- Security passed
- CI passed
- No conflicts
- Branch up to date

Otherwise

↓

Block merge

---

# Auto Merge

Merge Agent performs merge.

Workers never merge.

Providers never merge.

---

# Protected Branches

Protected

```
main

develop (optional)
```

Workers cannot push directly.

---

# GitHub Webhooks

Platform listens to

```
issues

issue_comment

pull_request

pull_request_review

push

check_suite

check_run
```

Every webhook updates internal state.

---

# Synchronization Rules

GitHub

↓

Database

Never

Database

↓

GitHub

unless executing an action.

GitHub is authoritative.

---

# Retry Rules

Retry automatically

- push failed
- webhook timeout
- temporary API failure

Never retry

- permission denied
- invalid repository
- deleted branch

---

# Merge Conflicts

If merge conflict

↓

Mark task

```
BLOCKED
```

↓

Escalation Agent

Workers never resolve complex merge conflicts automatically in V1.

---

# Commit Standards

Commit format

```
feat(api): ...

fix(worker): ...

docs(graph): ...

test(project): ...
```

One logical change per commit.

---

# GitHub Services

Only GitHubService may access GitHub.

Forbidden

```
Graph

↓

GitHub API
```

Allowed

```
Graph

↓

GitHubService

↓

GitHub API
```

---

# Required GitHub Permissions

Minimum

- Issues
- Pull Requests
- Contents
- Metadata
- Checks

Future

- Projects
- Discussions

---

# AI Agent Notes

Owner

GitHub Team

Allowed

- Labels
- Issues
- PRs
- Branches
- Webhooks

Forbidden

- Database schema
- Graph routing
- Provider implementation

---

# Acceptance Criteria

✓ One issue per task

✓ One branch per issue

✓ One PR per issue

✓ Protected main branch

✓ Automatic labels

✓ Automatic reviews

✓ Automatic rework

✓ Automatic merge

✓ GitHub remains source of truth

---

# Related Documents

04_LANGGRAPH_ARCHITECTURE.md

05_AGENT_SPECIFICATIONS.md

06_CODING_PROVIDER_INTERFACE.md

08_API_SPECIFICATION.md

---

End of Document