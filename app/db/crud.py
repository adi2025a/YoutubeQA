# db/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_videos(db: Session):
    return db.query(models.Video).all()

def get_video(db: Session, video_id: int):
    return db.query(models.Video).filter(models.Video.id == video_id).first()

def create_video(db: Session, video: schemas.VideoCreate):
    db_video = models.Video(title=video.title, description=video.description)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video
