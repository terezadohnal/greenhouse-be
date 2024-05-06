from sqlalchemy.orm import Session
from fastapi import APIRouter

import schemas
from database import SessionLocal
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from rgb.rgb_controller import RGB

rgb_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rgb_router.post("/rgb/available")
def Connect():
    return RGB.isCameraAvailable()

@rgb_router.post("/rgb/capture")
def Connect():
    return RGB.captureImage()

@rgb_router.post("/rgb/capturefake")
def Connect():
    return RGB.captureFakeImage()