from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.utils import hash

router = APIRouter(tags=["User"])

@router.post("/create_user")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    userCreate = User(name = user.name, password = hash(user.password))
    db.add(userCreate)
    db.commit()
    db.refresh(userCreate)
    return userCreate

@router.delete("/delete_user/{id}")
async def delete_user(id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    db.delete(user)
    db.commit()
    return "Deleted Successfully"