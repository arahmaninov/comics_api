from fastapi import APIRouter

from models import core
from models.database import engine, db
from controllers.comics import get_all_comics, get_rating

router = APIRouter()

@router.get("/")
def read_root():
    #return db.query(core.Comic).all()
    comics = get_all_comics()

    return comics

@router.get("/{comic_id}/rating/")
def read_rating(comic_id: int):
    #return {"comic_id": comic_id}

    #selected_comic = db.get(core.Comic, comic_id)
    #return selected_comic
    selected_comic = get_rating(comic_id)
    return selected_comic
