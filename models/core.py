from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Comic(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    rating = Column(Integer, default=0)

    comic_ratings = relationship("Rating", back_populates="comic")


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    comic_id = Column(Integer, ForeignKey("comics.id"))
    user_id = Column(Integer)
    value = Column(Integer) 

    comic = relationship("Comic", back_populates="comic_ratings")
