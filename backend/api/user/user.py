from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import User
from core.dependencies.auth import AuthenticationRequired
from core.dependencies.get_current_user import get_current_user

router = APIRouter()


@router.get("/me", dependencies=[Depends(AuthenticationRequired)])
async def get_user_profile(current_user: Annotated[User, Depends(get_current_user)]):
    return {"message": "Authenticated user", "user": current_user}
