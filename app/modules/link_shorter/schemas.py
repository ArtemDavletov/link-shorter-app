from pydantic import BaseModel, Field


class ShortenLinkSchema(BaseModel):
    long_link: str
    lifetime: int = Field(ge=10)
    number_of_transitions: int = Field(ge=5)
    length_of_new_link: int = Field(ge=8)
