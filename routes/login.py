from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from schemas.token import Token
from core.config import settings
from auth.token import create_access_token
from auth.password import verify_password, get_password_hash
from auth.dependencies import get_current_active_user
from datetime import timedelta
from db.config import get_db
from sqlalchemy.orm import Session
from models.admins import Admins
from schemas.admins import AdminsSchema


admin_router = APIRouter()

@admin_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)]
) -> Token:
    user = db.query(Admins).filter(Admins.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    hash_password: str = str(user.hash_pwd)
    if not verify_password(form_data.password, hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username, "id": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@admin_router.post("/create")
async def create_admin(admin: AdminsSchema, db: Annotated[Session, Depends(get_db)]):
    hash_passowrd = get_password_hash(admin.password)
    new_admin = Admins(firstname= admin.firstname, lastname= admin.lastname, email=admin.email, hash_pwd = hash_passowrd, is_active = True, is_admin = True)

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return {"admin": new_admin}

@admin_router.get("/user/me")
async def read_users_me(admin: Annotated[AdminsSchema, Depends(get_current_active_user)]):
    return admin