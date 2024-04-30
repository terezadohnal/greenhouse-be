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


class UserUpdate(UserBase):
    role: Role


class User(UserBase):
    id: int
    role: Role

    class Config:
        from_attributes = True


class UserPasswordReset(BaseModel):
    new_password: str


class CameraBase(BaseModel):
    camera_name: str
    sampling_frequency: int
    images_count: int
    camera_activation: int
    measurement_duration: int

class Camera(CameraBase):
    id: int

    class Config:
        from_attributes = True