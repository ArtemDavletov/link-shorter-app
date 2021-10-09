from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.modules.link_shorter.schemas import ShortenLinkSchema
from app.repository.url_mapping_collection import create_mapping, redirect_to_long_link
from app.settings.database import get_db
from app.settings.settings import settings

short_router = APIRouter()

__all__ = (
    short_router,
)


@short_router.post('/')
async def short_link(
        shorten_link_schema: ShortenLinkSchema,
        db: Session = Depends(get_db)
) -> str:
    return settings.APP_HOST + ":" + str(settings.APP_PORT) + "/short/redirect/" + create_mapping(db, shorten_link_schema)


@short_router.get('/redirect/{short_link}')
async def get_link(
        short_link: str,
        db: Session = Depends(get_db)
):
    return RedirectResponse(await redirect_to_long_link(db, short_link))
