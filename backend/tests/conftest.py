from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models import Base
from core.config import config
from core.database.session import AsyncSessionLocal

engine: AsyncEngine = create_async_engine(config.TEST_DATABASE_URL, pool_pre_ping=True)
SessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSessionLocal
)


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()
