from typing import Any, AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from core.server import server


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI, Any, None]:
    app = server()
    yield app


@pytest_asyncio.fixture(scope="function")
async def client(
    app: FastAPI, db_session: AsyncSession
) -> AsyncGenerator[AsyncClient, None]:
    async def _get_session():
        return db_session

    app.dependency_overrides[get_session] = _get_session

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
