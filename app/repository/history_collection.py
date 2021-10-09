from typing import List

from sqlalchemy.orm import Session

from app.models.history import History
from app.models.url_maping import UrlMapping


async def write_in_history(
        db: Session,
        url_mapping
) -> History:
    history: History = History(url_mapping_id=url_mapping.id)
    db.add(history)
    db.commit()

    return history


async def get_history_for_link(
        db: Session,
        short_link: str
) -> List[History]:
    url_mapping = db.query(UrlMapping).filter(UrlMapping.short_link == short_link).first()
    return db.query(History).filter(History.url_mapping_id == url_mapping.id).all()
