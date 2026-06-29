from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Column, Enum, ForeignKey, Index, Integer, String, Table, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin, UUIDPrimaryKeyMixin
from app.models.enums import TaskStatus

if TYPE_CHECKING:
    from app.models.projects import Project
    from app.models.tasks import Task

task_dependencies = Table(
    "task_dependencies",
    Base.metadata,
    Column("task_id", Uuid(as_uuid=True), ForeignKey("tasks.id"), primary_key=True),
    Column(
        "depends_on_task_id",
        Uuid(as_uuid=True),
        ForeignKey("tasks.id"),
        primary_key=True,
    ),
)


class Task(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "tasks"
    __table_args__ = (
        Index("ix_tasks_status", "status"),
        Index("ix_tasks_project_id", "project_id"),
        Index("ix_tasks_assigned_worker_id", "assigned_worker_id"),
    )

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    github_issue_number: Mapped[int | None] = mapped_column(Integer)
    parent_task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    acceptance_criteria: Mapped[str] = mapped_column(Text, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status"),
        default=TaskStatus.PLANNED,
        nullable=False,
    )
    retry_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    estimated_tokens: Mapped[int | None] = mapped_column(Integer)
    assigned_worker_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("workers.id", use_alter=True, name="fk_tasks_assigned_worker_id_workers")
    )

    project: Mapped[Project] = relationship()
    parent_task: Mapped[Task | None] = relationship(remote_side="Task.id")
