# SQL ALCHEMY MODELS
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Annotated, Union


from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Token(BaseModel):
    __tablename__ = "user_token"
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None