from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.controllers import UserController
from app.models import User
from app.schemas.user import UserResponse
from core.dependencies.auth import AuthenticationRequired
from core.dependencies.controller import get_user_controller
from core.dependencies.get_current_user import get_current_user
from core.exceptions import BadRequestException

router = APIRouter(dependencies=[Depends(AuthenticationRequired)])


@router.get("/u", response_model=UserResponse)
async def get_user(
    controller: Annotated[UserController, Depends(get_user_controller)],
    id: UUID | None = None,
    username: str | None = None,
    email: EmailStr | None = None,
):
    if email is None and id is None and username is None:
        raise BadRequestException(
            "At least one query parameter (id, email, username) is required"
        )

    if id:
        return await controller.get_by_id(id)
    if username:
        return await controller.get_by_username(username)
    if email:
        return await controller.get_by_email(email)


@router.get("/me")
async def get_user_profile(current_user: Annotated[User, Depends(get_current_user)]):
    return {"message": "Authenticated user", "user": current_user}


@router.put("/")
async def update_user_profile(
    current_user: Annotated[User, Depends(get_current_user)],
): ...
