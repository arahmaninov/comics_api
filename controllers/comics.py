from models.database import db
from models import core

def get_all_comics():
    return db.query(core.Comic).all()

def get_rating(comic_id: int):
    return db.get(core.Comic, comic_id)
    
