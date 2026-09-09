from fastapi import APIRouter, Depends

from core.dependencies.auth import auth_required

router = APIRouter()


@router.get("/me", dependencies=[Depends(auth_required)])
async def get_user_profile():
    return {"message": "Authenticated user."}
