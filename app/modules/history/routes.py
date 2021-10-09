from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.history import History
from app.repository.history_collection import get_history_for_link
from app.settings.database import get_db

history_router = APIRouter()

__all__ = (
    history_router,
)


@history_router.post('/all')
async def short_link(
        short_link: str,
        db: Session = Depends(get_db)
) -> List[History]:
    return await get_history_for_link(db, short_link)
