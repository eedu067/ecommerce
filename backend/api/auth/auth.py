from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.controllers import AuthController
from app.schemas.auth import CreateUser, LoginUser
from core.dependencies.controller import get_auth_controller

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    data: CreateUser,
    auth_controller: Annotated[AuthController, Depends(get_auth_controller)],
):

    new_user = await auth_controller.create_user(data)
    return {"message": "User registered successfully.", "user_id": new_user.id}


@router.post("/login")
async def login_user(
    data: LoginUser,
    auth_controller: Annotated[AuthController, Depends(get_auth_controller)],
):
    user = await auth_controller.login_user(data)
    return {"message": "User logged in successfully.", "user_id": user.id}
