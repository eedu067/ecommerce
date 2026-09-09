from typing import Tuple

from jwt import PyJWTError
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection

from app.schemas.user import CurrentUserRead
from core.security.jwt import JWTManager


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, CurrentUserRead | None]:  # type: ignore
        current_user = CurrentUserRead()

        authorization: str | None = conn.headers.get("Authorization")

        if not authorization:
            return False, current_user

        try:
            scheme, token = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
        except ValueError:
            return False, current_user

        if not token:
            return False, current_user

        try:
            payload = JWTManager.decode(token)
            user_id = payload["user_id"]
        except PyJWTError:
            return False, current_user

        current_user.id = user_id

        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
