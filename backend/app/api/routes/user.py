from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/")
def root():
    return {"message": "ELAN Backend Running"}


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
    name=user.name,
    email=user.email,
    skin_type=user.skin_type,
    concern=user.concern,
    favorite_category=user.favorite_category
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()