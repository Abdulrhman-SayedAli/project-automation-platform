from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, CreatedAtMixin, UUIDPrimaryKeyMixin
from app.models.enums import PullRequestStatus, ReviewDecision

if TYPE_CHECKING:
    from app.models.tasks import Task


class PullRequest(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "pull_requests"

    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"), nullable=False)
    github_pr: Mapped[int] = mapped_column(Integer, nullable=False)
    branch: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[PullRequestStatus] = mapped_column(
        Enum(PullRequestStatus, name="pull_request_status"),
        default=PullRequestStatus.OPEN,
        nullable=False,
    )
    ci_status: Mapped[str | None] = mapped_column(String(128))
    merged_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    task: Mapped[Task] = relationship()
    reviews: Mapped[list[Review]] = relationship(back_populates="pull_request")


class Review(UUIDPrimaryKeyMixin, CreatedAtMixin, Base):
    __tablename__ = "reviews"

    pr_id: Mapped[UUID] = mapped_column(ForeignKey("pull_requests.id"), nullable=False)
    reviewer: Mapped[str] = mapped_column(String(128), nullable=False)
    decision: Mapped[ReviewDecision] = mapped_column(
        Enum(ReviewDecision, name="review_decision"),
        nullable=False,
    )
    comments: Mapped[str | None] = mapped_column(Text)

    pull_request: Mapped[PullRequest] = relationship(back_populates="reviews")
