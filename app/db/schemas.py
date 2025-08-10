# db/schemas.py
from pydantic import BaseModel

class VideoBase(BaseModel):
    title: str
    description: str | None = None

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
