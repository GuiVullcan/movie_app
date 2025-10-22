from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models, schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.login(db, user)

@app.post("/movies/")
def add_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.add_movie(db, movie)

@app.post("/ratings/")
def rate_movie(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.add_rating(db, rating)

@app.post("/watched/")
def mark_watched(w: schemas.WatchedCreate, db: Session = Depends(get_db)):
    return crud.mark_watched(db, w)
