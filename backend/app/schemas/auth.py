from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas.token import TokenResponse

from .user import UserResponse

"""
    TODO: Add comprehensive validation for username and password
"""


class CreateUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: TokenResponse
    user: UserResponse

    model_config = ConfigDict(from_attributes=True)
