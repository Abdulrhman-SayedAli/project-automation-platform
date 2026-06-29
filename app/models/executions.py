from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import JSON, DateTime, Enum, Float, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, UUIDPrimaryKeyMixin
from app.models.enums import GraphExecutionStatus

if TYPE_CHECKING:
    from app.models.projects import Project
    from app.models.tasks import Task
    from app.models.workers import Worker


class TaskExecution(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "task_executions"
    __table_args__ = (
        Index("ix_task_executions_task_id", "task_id"),
        Index("ix_task_executions_worker_id", "worker_id"),
    )

    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"), nullable=False)
    worker_id: Mapped[UUID | None] = mapped_column(ForeignKey("workers.id"))
    provider: Mapped[str] = mapped_column(String(128), nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    result: Mapped[str | None] = mapped_column(Text)
    tokens: Mapped[int | None] = mapped_column(Integer)
    duration: Mapped[float | None] = mapped_column(Float)
    logs: Mapped[dict | None] = mapped_column(JSON)

    task: Mapped[Task] = relationship()
    worker: Mapped[Worker | None] = relationship()


class GraphExecution(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "graph_executions"

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    graph_name: Mapped[str] = mapped_column(String(128), nullable=False)
    current_node: Mapped[str] = mapped_column(String(128), nullable=False)
    state_snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)
    status: Mapped[GraphExecutionStatus] = mapped_column(
        Enum(GraphExecutionStatus, name="graph_execution_status"),
        default=GraphExecutionStatus.RUNNING,
        nullable=False,
    )
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    project: Mapped[Project] = relationship()
