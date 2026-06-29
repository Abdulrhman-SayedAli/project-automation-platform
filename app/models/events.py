from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import JSON, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, CreatedAtMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.projects import Project
    from app.models.tasks import Task


class Event(UUIDPrimaryKeyMixin, CreatedAtMixin, Base):
    __tablename__ = "events"
    __table_args__ = (
        Index("ix_events_project_id", "project_id"),
        Index("ix_events_created_at", "created_at"),
    )

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id"))
    event_type: Mapped[str] = mapped_column(String(128), nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    project: Mapped[Project] = relationship()
    task: Mapped[Task | None] = relationship()
