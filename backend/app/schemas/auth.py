import re

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.schemas.token import TokenResponse

from .user import UserResponse

"""
    TODO: Add comprehensive validation for username and password
"""

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]+$")


class CreateUser(BaseModel):
    email: EmailStr = Field(..., examples=["john_doe@example.com"])
    username: str = Field(..., min_length=3, max_length=30, examples=["john_doe"])
    password: str = Field(
        ..., min_length=8, max_length=128, examples=["MySecurePassword@123"]
    )

    @field_validator("username")
    @classmethod
    def _validate_username(cls, v: str) -> str:
        if not USERNAME_RE.match(v):
            raise ValueError(
                "Username may only contain letters, numbers, and underscores"
            )

        if not v[0].isalpha():
            raise ValueError("Username must start with a letter")
        if v[-1] == "_":
            raise ValueError("Username cannot end with underscore")
        if "__" in v:
            raise ValueError("Username cannot contain consecutive underscores")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        missing = []

        if not re.search(r"[A-Z]", v):
            missing.append("'one uppercase letter'")
        if not re.search(r"[a-z]", v):
            missing.append("'one lowercase letter'")
        if not re.search(r"\d", v):
            missing.append("'one digit'")
        if not re.search(r"[^\w\s]", v):
            missing.append("'one special character'")
        if missing:
            raise ValueError(f"Password must contain at least {', '.join(missing)}")

        return v


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: TokenResponse
    user: UserResponse

    model_config = ConfigDict(from_attributes=True)
