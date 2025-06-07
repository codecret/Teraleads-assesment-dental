from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin, User, Token
from app.services.auth import create_user, login_user
from app.core.security import get_current_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    return create_user(db=db, user=user)

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Login user and return JWT token.
    """
    return login_user(db=db, user_data=user_data)

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    """
    Get current user information.
    """
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "name": current_user.name
    } 