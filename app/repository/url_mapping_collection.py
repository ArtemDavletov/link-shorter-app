import datetime

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.url_maping import UrlMapping
from app.modules.link_shorter.schemas import ShortenLinkSchema
from app.repository.history_collection import write_in_history
from app.utils.utils import create_random_string


def create_mapping(
        db: Session,
        shorten_link_schema: ShortenLinkSchema,
) -> str:
    short_link = create_random_string(shorten_link_schema.length_of_new_link)
    url_mapping = UrlMapping(short_link=short_link,
                             long_link=shorten_link_schema.long_link,
                             expiration_datetime=datetime.datetime.utcnow() + datetime.timedelta(
                                 days=shorten_link_schema.lifetime),
                             number_of_transitions=shorten_link_schema.number_of_transitions)
    db.add(url_mapping)
    db.commit()

    return short_link


async def redirect_to_long_link(
        db: Session,
        short_link
) -> str:
    url_mapping: UrlMapping = db.query(UrlMapping).filter(UrlMapping.short_link == short_link).first()
    if url_mapping.number_of_transitions == 0 or url_mapping.expiration_datetime < datetime.datetime.utcnow():
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE)

    db.query(UrlMapping).filter(UrlMapping.id == url_mapping.id) \
        .update({"number_of_transitions": url_mapping.number_of_transitions - 1})
    db.commit()

    await write_in_history(db, url_mapping)

    return url_mapping.long_link
