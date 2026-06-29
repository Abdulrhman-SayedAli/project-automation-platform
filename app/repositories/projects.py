from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.enums import ProjectStatus
from app.models.projects import Project


class ProjectRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self,
        *,
        name: str,
        description: str,
        github_repository: str | None,
        template: str | None,
        status: ProjectStatus = ProjectStatus.CREATED,
    ) -> Project:
        project = Project(
            name=name,
            description=description,
            github_repository=github_repository,
            template=template,
            status=status,
        )
        self._session.add(project)
        await self._session.flush()
        return project

    async def get(self, project_id: UUID) -> Project | None:
        return await self._session.get(Project, project_id)

    async def list(self) -> Sequence[Project]:
        result = await self._session.scalars(select(Project).order_by(Project.created_at.desc()))
        return result.all()

