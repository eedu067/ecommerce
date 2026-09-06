from typing import Annotated

from fastapi import APIRouter, Depends

from app.controllers import AuthController
from app.models.auth import CreateUser
from core.dependencies.controller import get_auth_controller

router = APIRouter()


@router.post("/register")
async def register_user(
    data: CreateUser,
    auth_controller: Annotated[AuthController, Depends(get_auth_controller)],
):
    existing_user = await auth_controller.get_by_email(data.email)
    if existing_user:
        return {"error": "User with this email already exists."}

    new_user = await auth_controller.create_user(data)
    return {"message": "User registered successfully.", "user_id": new_user.id}
