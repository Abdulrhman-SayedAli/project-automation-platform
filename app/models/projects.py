from __future__ import annotations

from uuid import UUID

from sqlalchemy import Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, CreatedAtMixin, TimestampMixin, UUIDPrimaryKeyMixin
from app.models.enums import ProjectStatus


class Project(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "projects"
    __table_args__ = (Index("ix_projects_status", "status"),)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    github_repository: Mapped[str | None] = mapped_column(String(512))
    template: Mapped[str | None] = mapped_column(String(128))
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, name="project_status"),
        default=ProjectStatus.CREATED,
        nullable=False,
    )

    documents: Mapped[list[ProjectDocument]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )


class ProjectDocument(UUIDPrimaryKeyMixin, CreatedAtMixin, Base):
    __tablename__ = "project_documents"

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    type: Mapped[str] = mapped_column(String(128), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    project: Mapped[Project] = relationship(back_populates="documents")
