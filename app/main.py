from fastapi import FastAPI

from routers import comics, ratings


app = FastAPI()

app.include_router(comics.router, prefix="/api/comics")
app.include_router(ratings.router, prefix="/api/ratings")

@app.get("/")
def root():
    return {"test": "ok"}
