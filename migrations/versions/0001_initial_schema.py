"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-06-29
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_initial_schema"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("github_repository", sa.String(length=512), nullable=True),
        sa.Column("template", sa.String(length=128), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "CREATED",
                "PLANNING",
                "IMPLEMENTING",
                "REVIEWING",
                "COMPLETED",
                "BLOCKED",
                "FAILED",
                name="project_status",
            ),
            nullable=False,
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_projects")),
    )
    op.create_index("ix_projects_status", "projects", ["status"])

    op.create_table(
        "settings",
        sa.Column("key", sa.String(length=128), nullable=False),
        sa.Column("value", sa.JSON(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_settings")),
    )
    op.create_index("ix_settings_key", "settings", ["key"], unique=True)

    op.create_table(
        "graph_executions",
        sa.Column("project_id", sa.Uuid(), nullable=False),
        sa.Column("graph_name", sa.String(length=128), nullable=False),
        sa.Column("current_node", sa.String(length=128), nullable=False),
        sa.Column("state_snapshot", sa.JSON(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("RUNNING", "COMPLETED", "BLOCKED", "FAILED", name="graph_execution_status"),
            nullable=False,
        ),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], name=op.f("fk_graph_executions_project_id_projects")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_graph_executions")),
    )

    op.create_table(
        "project_documents",
        sa.Column("project_id", sa.Uuid(), nullable=False),
        sa.Column("type", sa.String(length=128), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], name=op.f("fk_project_documents_project_id_projects")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_project_documents")),
    )

    op.create_table(
        "tasks",
        sa.Column("project_id", sa.Uuid(), nullable=False),
        sa.Column("github_issue_number", sa.Integer(), nullable=True),
        sa.Column("parent_task_id", sa.Uuid(), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("acceptance_criteria", sa.Text(), nullable=False),
        sa.Column("priority", sa.Integer(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "PLANNED",
                "READY",
                "ASSIGNED",
                "WORKING",
                "PR_OPEN",
                "IN_REVIEW",
                "REWORK",
                "MERGED",
                "DONE",
                "BLOCKED",
                "FAILED",
                name="task_status",
            ),
            nullable=False,
        ),
        sa.Column("retry_count", sa.Integer(), nullable=False),
        sa.Column("estimated_tokens", sa.Integer(), nullable=True),
        sa.Column("assigned_worker_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["parent_task_id"], ["tasks.id"], name=op.f("fk_tasks_parent_task_id_tasks")),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], name=op.f("fk_tasks_project_id_projects")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tasks")),
    )
    op.create_index("ix_tasks_assigned_worker_id", "tasks", ["assigned_worker_id"])
    op.create_index("ix_tasks_project_id", "tasks", ["project_id"])
    op.create_index("ix_tasks_status", "tasks", ["status"])

    op.create_table(
        "workers",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("provider", sa.String(length=128), nullable=False),
        sa.Column("status", sa.Enum("IDLE", "RUNNING", "FAILED", "OFFLINE", name="worker_status"), nullable=False),
        sa.Column("current_task_id", sa.Uuid(), nullable=True),
        sa.Column("heartbeat", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["current_task_id"], ["tasks.id"], name=op.f("fk_workers_current_task_id_tasks")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_workers")),
    )
    op.create_index("ix_workers_status", "workers", ["status"])

    op.create_foreign_key(
        op.f("fk_tasks_assigned_worker_id_workers"),
        "tasks",
        "workers",
        ["assigned_worker_id"],
        ["id"],
    )

    op.create_table(
        "events",
        sa.Column("project_id", sa.Uuid(), nullable=False),
        sa.Column("task_id", sa.Uuid(), nullable=True),
        sa.Column("event_type", sa.String(length=128), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], name=op.f("fk_events_project_id_projects")),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"], name=op.f("fk_events_task_id_tasks")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_events")),
    )
    op.create_index("ix_events_created_at", "events", ["created_at"])
    op.create_index("ix_events_project_id", "events", ["project_id"])

    op.create_table(
        "pull_requests",
        sa.Column("task_id", sa.Uuid(), nullable=False),
        sa.Column("github_pr", sa.Integer(), nullable=False),
        sa.Column("branch", sa.String(length=255), nullable=False),
        sa.Column(
            "status",
            sa.Enum("OPEN", "REVIEW", "CHANGES_REQUESTED", "READY", "MERGED", "CLOSED", name="pull_request_status"),
            nullable=False,
        ),
        sa.Column("ci_status", sa.String(length=128), nullable=True),
        sa.Column("merged_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"], name=op.f("fk_pull_requests_task_id_tasks")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_pull_requests")),
    )

    op.create_table(
        "task_dependencies",
        sa.Column("task_id", sa.Uuid(), nullable=False),
        sa.Column("depends_on_task_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["depends_on_task_id"], ["tasks.id"], name=op.f("fk_task_dependencies_depends_on_task_id_tasks")),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"], name=op.f("fk_task_dependencies_task_id_tasks")),
        sa.PrimaryKeyConstraint("task_id", "depends_on_task_id", name=op.f("pk_task_dependencies")),
    )

    op.create_table(
        "task_executions",
        sa.Column("task_id", sa.Uuid(), nullable=False),
        sa.Column("worker_id", sa.Uuid(), nullable=True),
        sa.Column("provider", sa.String(length=128), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("result", sa.Text(), nullable=True),
        sa.Column("tokens", sa.Integer(), nullable=True),
        sa.Column("duration", sa.Float(), nullable=True),
        sa.Column("logs", sa.JSON(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"], name=op.f("fk_task_executions_task_id_tasks")),
        sa.ForeignKeyConstraint(["worker_id"], ["workers.id"], name=op.f("fk_task_executions_worker_id_workers")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_task_executions")),
    )
    op.create_index("ix_task_executions_task_id", "task_executions", ["task_id"])
    op.create_index("ix_task_executions_worker_id", "task_executions", ["worker_id"])

    op.create_table(
        "reviews",
        sa.Column("pr_id", sa.Uuid(), nullable=False),
        sa.Column("reviewer", sa.String(length=128), nullable=False),
        sa.Column("decision", sa.Enum("PASS", "FAIL", "BLOCK", "HUMAN_REQUIRED", name="review_decision"), nullable=False),
        sa.Column("comments", sa.Text(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["pr_id"], ["pull_requests.id"], name=op.f("fk_reviews_pr_id_pull_requests")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_reviews")),
    )


def downgrade() -> None:
    op.drop_table("reviews")
    op.drop_index("ix_task_executions_worker_id", table_name="task_executions")
    op.drop_index("ix_task_executions_task_id", table_name="task_executions")
    op.drop_table("task_executions")
    op.drop_table("task_dependencies")
    op.drop_table("pull_requests")
    op.drop_index("ix_events_project_id", table_name="events")
    op.drop_index("ix_events_created_at", table_name="events")
    op.drop_table("events")
    op.drop_constraint(op.f("fk_tasks_assigned_worker_id_workers"), "tasks", type_="foreignkey")
    op.drop_index("ix_workers_status", table_name="workers")
    op.drop_table("workers")
    op.drop_index("ix_tasks_status", table_name="tasks")
    op.drop_index("ix_tasks_project_id", table_name="tasks")
    op.drop_index("ix_tasks_assigned_worker_id", table_name="tasks")
    op.drop_table("tasks")
    op.drop_table("project_documents")
    op.drop_table("graph_executions")
    op.drop_index("ix_settings_key", table_name="settings")
    op.drop_table("settings")
    op.drop_index("ix_projects_status", table_name="projects")
    op.drop_table("projects")
    op.execute("DROP TYPE IF EXISTS review_decision")
    op.execute("DROP TYPE IF EXISTS pull_request_status")
    op.execute("DROP TYPE IF EXISTS worker_status")
    op.execute("DROP TYPE IF EXISTS task_status")
    op.execute("DROP TYPE IF EXISTS graph_execution_status")
    op.execute("DROP TYPE IF EXISTS project_status")
