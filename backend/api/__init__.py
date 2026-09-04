from fastapi import APIRouter

from .health import health

router = APIRouter()

router.include_router(
    health.router,
)
