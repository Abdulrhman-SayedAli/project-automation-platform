from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, CreatedAtMixin, UUIDPrimaryKeyMixin
from app.models.enums import WorkerStatus

if TYPE_CHECKING:
    from app.models.tasks import Task


class Worker(UUIDPrimaryKeyMixin, CreatedAtMixin, Base):
    __tablename__ = "workers"
    __table_args__ = (Index("ix_workers_status", "status"),)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    provider: Mapped[str] = mapped_column(String(128), nullable=False)
    status: Mapped[WorkerStatus] = mapped_column(
        Enum(WorkerStatus, name="worker_status"),
        default=WorkerStatus.IDLE,
        nullable=False,
    )
    current_task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id"))
    heartbeat: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    current_task: Mapped[Task | None] = relationship(foreign_keys=[current_task_id])
