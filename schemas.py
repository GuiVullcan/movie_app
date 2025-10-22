from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class MovieBase(BaseModel):
    title: str
    description: str
    genre: str
    year: int

class MovieCreate(MovieBase):
    pass

class RatingCreate(BaseModel):
    movie_id: int
    score: float
    comment: Optional[str] = None

class WatchedCreate(BaseModel):
    movie_id: int
