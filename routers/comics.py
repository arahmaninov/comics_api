from fastapi import APIRouter

from models import core
from models.database import engine, db
from controllers.comics import get_all_comics, get_rating


router = APIRouter()

@router.get("/")
def read_root():
    comics = get_all_comics()

    return comics

@router.get("/{comic_id}/rating/")
def read_rating(comic_id: int):
    rating = get_rating(comic_id)

    return rating
