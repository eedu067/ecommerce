from fastapi import APIRouter

from .auth import auth
from .health import health

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
