import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.repositories.events import EventRepository
from app.repositories.projects import ProjectRepository


@pytest.fixture
async def session_factory() -> async_sessionmaker:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    try:
        yield async_sessionmaker(engine, expire_on_commit=False)
    finally:
        await engine.dispose()


async def test_project_repository_creates_and_reads_project(
    session_factory: async_sessionmaker,
) -> None:
    async with session_factory() as session:
        repository = ProjectRepository(session)

        project = await repository.create(
            name="Factory",
            description="Autonomous delivery platform",
            github_repository="owner/repo",
            template="backend",
        )
        await session.commit()

        stored_project = await repository.get(project.id)
        projects = await repository.list()

    assert stored_project is not None
    assert stored_project.name == "Factory"
    assert len(projects) == 1


async def test_event_repository_appends_events(session_factory: async_sessionmaker) -> None:
    async with session_factory() as session:
        projects = ProjectRepository(session)
        events = EventRepository(session)
        project = await projects.create(
            name="Factory",
            description="Autonomous delivery platform",
            github_repository=None,
            template=None,
        )

        event = await events.append(
            project_id=project.id,
            event_type="PROJECT_CREATED",
            payload={"source": "test"},
        )
        await session.commit()

        stored_events = await events.list_for_project(project.id)

    assert event.id is not None
    assert [stored_event.event_type for stored_event in stored_events] == ["PROJECT_CREATED"]
