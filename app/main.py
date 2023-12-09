from fastapi import FastAPI

from models import core
from models.database import engine
from routers import comics, ratings

core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(comics.router, prefix="/api/comics")
app.include_router(ratings.router, prefix="/api/ratings")

@app.get("/")
def root():
    return {"test": "ok"}
