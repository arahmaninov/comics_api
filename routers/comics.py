from fastapi import APIRouter


router = APIRouter()


@router.get("/{comic_id}/rating/")
def read_rating(comic_id: int):
    return {"comic_id": comic_id}
