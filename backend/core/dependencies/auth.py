from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.security.jwt import JWTManager


async def auth_required(
    request: Request,
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(HTTPBearer(auto_error=False))
    ],
):
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    payload = JWTManager.decode(credentials.credentials)
    user_id = payload.get("user_id", None)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Invalid JWT Token",
        )
    # TODO: Add the user_id in the request
