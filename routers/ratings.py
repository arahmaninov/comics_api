from fastapi import APIRouter

from controllers.ratings import add_rating


router = APIRouter()

@router.post("/")
def _rating(comic_id: int, user_id: int, value: int):
    data = add_rating(comic_id, user_id, value)
    return data
