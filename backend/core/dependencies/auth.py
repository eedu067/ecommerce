from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class AuthenticationRequired:
    def __init__(
        self,
        token: Annotated[
            HTTPAuthorizationCredentials, Depends(HTTPBearer(auto_error=False))
        ],
    ) -> None:
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required",
            )
