from fastapi import HTTPException

from models.database import db
from models import core


def add_rating(comic_id: int, user_id: int, value: int):

    comic_exists = db.query(core.Comic).filter(core.Comic.id == comic_id).first()

    if value >= 1 and value <= 5 and comic_exists:

        user_already_rated_this_comic = db.query(core.Rating).filter(core.Rating.comic_id == comic_id, core.Rating.user_id == user_id).first()
        if user_already_rated_this_comic:
            # Updating existing rating
            user_already_rated_this_comic.value = value
            db.commit()
        else:
            # Make a new rating
            rating = core.Rating(comic_id=comic_id, user_id=user_id, value=value)
            db.add(rating)
            db.commit()
        
        # Calculating the average rating for the comic
        all_comic_ratings = db.query(core.Rating).filter(core.Rating.comic_id == comic_id).all()
        all_ratings = 0
        counter = 0
        for rating in all_comic_ratings:
            all_ratings += rating.value
            counter += 1
        average = int(all_ratings / counter)

        comic_to_change = db.query(core.Comic).filter(core.Comic.id == comic_id).first()
        comic_to_change.rating = average

        db.commit()

        return {"addition": "ok"}
    else:
        raise HTTPException(status_code=400)

