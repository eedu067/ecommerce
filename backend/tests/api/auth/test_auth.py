import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient) -> None:
    fake_user = {
        "username": "john_doe",
        "email": "john_doe@example.com",
        "password": "Secure@123",
    }

    response = await client.post("/auth/register", json=fake_user)

    assert response.status_code == 201
