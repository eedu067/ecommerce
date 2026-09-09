from typing import Annotated

from fastapi import Depends, Request

from app.controllers import UserController
from app.models import User
from core.dependencies.controller import get_user_controller


async def get_current_user(
    request: Request,
    controller: Annotated[UserController, Depends(get_user_controller)],
) -> User:
    return await controller.get_by_id(request.user.id)
