from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

router = APIRouter()

@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()  # get all users from database
    return users  # return the list of users