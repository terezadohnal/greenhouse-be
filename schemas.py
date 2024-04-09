# PYDANTIC SCHEMAS (MODELS)
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True