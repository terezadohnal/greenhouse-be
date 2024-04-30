from sqlalchemy.orm import Session
import os

from schemas import Role, UserCreate
from models.user_model import User, TokenData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

from fastapi.encoders import jsonable_encoder


def get_user(db: Session, user_id: int):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    return jsonable_encoder(user) if user else None


def get_user_by_email(db: Session, email: str):
    user = db.query(user_model.User).filter(user_model.User.email == email).first()
    return jsonable_encoder(user) if user else None


def get_user_by_username(db: Session, username: str):
    user = db.query(user_model.User).filter(user_model.User.username == username).first()
    return jsonable_encoder(user) if user else None



def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(user_model.User).offset(skip).limit(limit).all()
    return [jsonable_encoder(user) for user in users]


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        role=Role.user.value
    )
    print(db_user.hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jsonable_encoder(db_user)


def edit_user(user_id: int, user: schemas.UserCreate, db: Session):
    # Retrieve the user from the database
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()

    # Check if the user exists
    if db_user:
        # Update the user's properties with the new data
        db_user.email = user.email
        db_user.username = user.username
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name

        # If a new password is provided, hash it and update the hashed password
        if user.password:
            hashed_password = get_password_hash(user.password)
            db_user.hashed_password = hashed_password

        # Commit the changes to the database
        db.commit()

        # Refresh the db_user to reflect the changes made in the database
        db.refresh(db_user)

        updated_user = {
            "id": db_user.id,
            "email": db_user.email,
            "username": db_user.username,
            "first_name": db_user.first_name,
            "last_name": db_user.last_name
        }

        print(updated_user)

        # Return the updated user as a dictionary
        return updated_user
    else:
        # Handle the case where the user with the given ID does not exist
        return None


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user