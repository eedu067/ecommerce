from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt

from core.config import config


class JWTManager:
    @staticmethod
    def encode(payload: Dict[str, Any]) -> str:
        payload["exp"] = datetime.now(timezone.utc) + timedelta(
            minutes=config.JWT_ACCESS_EXPIRE_MINUTES
        )

        return jwt.encode(
            payload,
            key=config.JWT_SECRET_KEY,
            algorithm=config.JWT_ALGORITHM,
        )

    @staticmethod
    def decode(token: str) -> Dict[str, Any]:
        return jwt.decode(
            token,
            key=config.JWT_SECRET_KEY,
            algorithms=[config.JWT_ALGORITHM],
        )
