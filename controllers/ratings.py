from models.database import db
from models import core

def add_rating(comic_id: int, user_id: int, value: int):
    rating = core.Rating(comic_id=comic_id, user_id=user_id, value=value)
    db.add(rating)
    db.commit()
    
    all_comic_ratings = db.query(core.Rating).filter(core.Rating.comic_id == comic_id).all()
    all_ratings = 0
    counter = 0
    for rating in all_comic_ratings:
        print(f"ID: {rating.id} Comic id: {rating.comic_id} User id: {rating.user_id} Value: {rating.value}")
        all_ratings += rating.value
        counter += 1
    average = int(all_ratings / counter)
    print(f"Average rating for that comic is {average}")

    comic_to_change = db.query(core.Comic).filter(core.Comic.id == comic_id).first()
    comic_to_change.rating = average

    db.commit()

    return {"addition": "ok"}
    #return {"comic_id": comic_id, "user_id": user_id, "value": value}
