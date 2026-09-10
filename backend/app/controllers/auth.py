from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas.auth import CreateUser, LoginResponse, LoginUser
from app.schemas.token import TokenResponse
from app.schemas.user import UserResponse
from core.exceptions import ConflictException, UnauthorizedException
from core.security.jwt import JWTManager
from core.security.password import PasswordHasher


class AuthController:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def _get_by_email(self, email: EmailStr) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def _get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def _get_by_id(self, user_id: UUID) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def create_user(self, data: CreateUser) -> LoginResponse:

        if await self._get_by_email(data.email):
            raise ConflictException("Email already exists")

        if await self._get_by_username(data.username):
            raise ConflictException("Username already exists")

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
        user = await self._get_by_email(data.email)

        if not user:
            raise UnauthorizedException("Invalid credentials")

        if not PasswordHasher.verify_password(data.password, user.password):
            raise UnauthorizedException("Invalid credentials")

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
