# PYDANTIC SCHEMAS (MODELS)
from enum import Enum

from pydantic import BaseModel


class Role(Enum):
    user = 'user'
    admin = 'admin'


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    role: Role

    class Config:
        from_attributes = True