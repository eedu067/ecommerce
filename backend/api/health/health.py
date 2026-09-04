from typing import Annotated, TypedDict

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session

router = APIRouter()


class Status(TypedDict):
    db_connection: bool


@router.get("/")
async def health_check(session: Annotated[AsyncSession, Depends(get_session)]):
    status: Status = Status(db_connection=False)
    try:
        await session.execute(text("SELECT 1"))
        status["db_connection"] = True

    except Exception:
        pass

    return {"DB_Connection": status["db_connection"]}
