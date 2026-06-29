from enum import StrEnum


class ProjectStatus(StrEnum):
    CREATED = "CREATED"
    PLANNING = "PLANNING"
    IMPLEMENTING = "IMPLEMENTING"
    REVIEWING = "REVIEWING"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"


class TaskStatus(StrEnum):
    PLANNED = "PLANNED"
    READY = "READY"
    ASSIGNED = "ASSIGNED"
    WORKING = "WORKING"
    PR_OPEN = "PR_OPEN"
    IN_REVIEW = "IN_REVIEW"
    REWORK = "REWORK"
    MERGED = "MERGED"
    DONE = "DONE"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"


class WorkerStatus(StrEnum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    OFFLINE = "OFFLINE"


class PullRequestStatus(StrEnum):
    OPEN = "OPEN"
    REVIEW = "REVIEW"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    READY = "READY"
    MERGED = "MERGED"
    CLOSED = "CLOSED"


class ReviewDecision(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    BLOCK = "BLOCK"
    HUMAN_REQUIRED = "HUMAN_REQUIRED"


class GraphExecutionStatus(StrEnum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"

