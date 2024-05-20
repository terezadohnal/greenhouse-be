from sqlalchemy.orm import Session
from fastapi import APIRouter

import schemas
from database import SessionLocal
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from rgb.rgb_controller import RGB
import os
from fastapi.responses import FileResponse


rgb_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

rgb_output_folder = "./rgb/output/"

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


@rgb_router.get("/rgb-photos/{photo_filename}")
async def get_activity_photo(photo_filename: str):
    photo_path = str(rgb_output_folder) + str(photo_filename)

    if os.path.isfile(photo_path):
        return FileResponse(photo_path)
    else:
        raise HTTPException(status_code=404, detail="Photo not found")


@rgb_router.get("/rgb-photos/how-many/")
async def get_activity_photo():
    try:
        photos = os.listdir(rgb_output_folder)
        print(photos)
        return photos
    except:
        return 0

