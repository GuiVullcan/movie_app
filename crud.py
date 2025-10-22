from sqlalchemy.orm import Session
from models import User, Movie, Rating, Watched
from schemas import UserCreate, UserLogin, MovieCreate, RatingCreate, WatchedCreate
from passlib.context import CryptContext
from fastapi import HTTPException
from jose import jwt
import datetime

SECRET_KEY = "chave_secreta_para_jwt"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    truncated = password[:72]  # corta no máximo 72 caracteres
    return pwd_context.hash(truncated)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(user_id: int):
    payload = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_user(db: Session, user: UserCreate):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuário criado com sucesso"}

def login(db: Session, user: UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_token(db_user.id)
    return {"access_token": token, "token_type": "bearer"}

def add_movie(db: Session, movie: MovieCreate):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {"message": "Filme adicionado", "movie": new_movie.title}

def add_rating(db: Session, rating: RatingCreate):
    new_rating = Rating(**rating.dict())
    db.add(new_rating)
    db.commit()
    return {"message": "Avaliação adicionada"}

def mark_watched(db: Session, w: WatchedCreate):
    new_watched = Watched(**w.dict())
    db.add(new_watched)
    db.commit()
    return {"message": "Filme marcado como assistido"}
