import datetime

from sqlalchemy import Column, Integer, DateTime, String

from app.settings.database import Base


class UrlMapping(Base):
    __tablename__ = 'url_mapping'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    short_link = Column(String, unique=True, index=True)
    long_link = Column(String)
    creation_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    expiration_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    number_of_transitions = Column(Integer, default=10_000)
