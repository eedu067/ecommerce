from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import AuthController, UserController
from core.database import get_session


async def get_auth_controller(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> AuthController:
    return AuthController(session)


async def get_user_controller(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> UserController:
    return UserController(session)
