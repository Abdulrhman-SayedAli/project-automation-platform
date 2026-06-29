from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.events import Event


class EventRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def append(
        self,
        *,
        project_id: UUID,
        event_type: str,
        payload: dict,
        task_id: UUID | None = None,
    ) -> Event:
        event = Event(
            project_id=project_id,
            task_id=task_id,
            event_type=event_type,
            payload=payload,
        )
        self._session.add(event)
        await self._session.flush()
        return event

    async def list_for_project(self, project_id: UUID) -> Sequence[Event]:
        result = await self._session.scalars(
            select(Event)
            .where(Event.project_id == project_id)
            .order_by(Event.created_at.asc())
        )
        return result.all()

