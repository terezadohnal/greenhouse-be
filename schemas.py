# PYDANTIC SCHEMAS (MODELS)
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    fullname: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True