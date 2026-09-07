from uuid import UUID

from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas.auth import CreateUser, LoginResponse, LoginUser
from app.schemas.token import TokenResponse
from app.schemas.user import UserResponse
from core.security.jwt import JWTManager
from core.security.password import PasswordHasher

"""
    TODO: Return a JWT token upon successful login and registration. 
    This will allow the user to authenticate subsequent requests using the token.

    # TODO: The user should be able to log in with either their email or username.
    Update the login schema to accept either email or username, 
    and modify the login_user method to handle both cases.

    # TODO: Implement a password reset functionality.
    # TODO: Implement email verification upon registration.
    # TODO: Implement rate limiting for login attempts to 
        prevent brute force attacks.
    # TODO: Implement a logout functionality that invalidates
        the user's session or token.
    # TODO: Implement a refresh token mechanism to allow users
        to obtain a new access token without re-authenticating.

"""


class AuthController:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_by_email(self, email: EmailStr) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def get_by_id(self, user_id: UUID) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def create_user(self, data: CreateUser) -> LoginResponse:

        if await self.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email already exists."
            )

        if await self.get_by_username(data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username already exists."
            )

        hashed_password = PasswordHasher.hash_password(data.password)
        data.password = hashed_password

        user = User(**data.model_dump())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        token = self.generate_jwt_token(user)

        return LoginResponse(
            token=TokenResponse(token=token),
            user=UserResponse.model_validate(user),
        )

    async def login_user(self, data: LoginUser):
        user = await self.get_by_email(data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials."
            )

        if not PasswordHasher.verify_password(data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials."
            )

        token = self.generate_jwt_token(user)

        return LoginResponse(
            token=TokenResponse(token=token),
            user=UserResponse.model_validate(user),
        )

    def generate_jwt_token(self, user: User) -> str:

        payload = {
            "user_id": str(user.id),
            "email": user.email,
            "username": user.username,
        }
        token = JWTManager.encode(payload)
        return token
