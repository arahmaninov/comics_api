from fastapi import FastAPI

from models import core
from models.database import engine, db
from routers import comics, ratings


core.Base.metadata.create_all(bind=engine)

all_comics = db.query(core.Comic).all()
for comic in all_comics:
    print(f"{comic.id} - {comic.title} - {comic.author} - {comic.rating}")

app = FastAPI()

app.include_router(comics.router, prefix="/api/comics")
app.include_router(ratings.router, prefix="/api/ratings")

@app.get("/")
def root():
    return {"test": "ok"}
