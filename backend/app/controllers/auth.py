from uuid import UUID

from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.models.auth import CreateUser
from core.security.password import PasswordHasher


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

    async def create_user(self, data: CreateUser) -> User:

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
        return user
