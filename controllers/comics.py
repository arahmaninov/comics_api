from fastapi import HTTPException

from models.database import db
from models import core


def get_all_comics():
    return db.query(core.Comic).all()

def get_rating(comic_id: int):
    selected_comic = db.get(core.Comic, comic_id)
    if selected_comic:
        return selected_comic.rating
    else:
        raise HTTPException(status_code=400)
