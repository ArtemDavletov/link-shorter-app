import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from app.settings.database import Base


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    transition_datetime = Column(DateTime, default=datetime.datetime.utcnow)

    url_mapping_id = Column(Integer, ForeignKey('url_mapping.id'))
