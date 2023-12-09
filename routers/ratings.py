from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def read_ratings():
    return {"ratings test": "ok"}
