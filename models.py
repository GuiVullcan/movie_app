from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    ratings = relationship("Rating", back_populates="user")
    watched = relationship("Watched", back_populates="user")

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    genre = Column(String)
    year = Column(Integer)
    ratings = relationship("Rating", back_populates="movie")
    watched = relationship("Watched", back_populates="movie")

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    score = Column(Float)
    comment = Column(String, nullable=True)
    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")

class Watched(Base):
    __tablename__ = "watched"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    watched_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="watched")
    movie = relationship("Movie", back_populates="watched")
