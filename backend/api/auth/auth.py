from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.controllers import AuthController
from app.schemas.auth import CreateUser, LoginResponse, LoginUser
from core.dependencies.controller import get_auth_controller

router = APIRouter()


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=LoginResponse
)
async def register_user(
    data: CreateUser,
    auth_controller: Annotated[AuthController, Depends(get_auth_controller)],
):

    return await auth_controller.create_user(data)


@router.post("/login", response_model=LoginResponse)
async def login_user(
    data: LoginUser,
    auth_controller: Annotated[AuthController, Depends(get_auth_controller)],
):
    return await auth_controller.login_user(data)
