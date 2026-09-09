from fastapi import APIRouter

from .auth import auth
from .health import health
from .user import user

router = APIRouter()

router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)


router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

router.include_router(
    user.router,
    prefix="/users",
    tags=["User Management"],
)
