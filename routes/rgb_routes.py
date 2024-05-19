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
import time


rgb_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_folders():
    # create folders if they do not exist
    if not os.path.exists("rgb"):
        os.makedirs("rgb")
    if not os.path.exists("rgb/output"):
        os.makedirs("rgb/output")

rbg_folder = "./rgb/"
# if rgb folder does not exist, create it
if not os.path.exists(rbg_folder):
    os.makedirs(rbg_folder)

rgb_output_folder = "./rgb/output/"
# if rgb output folder does not exist, create it
if not os.path.exists(rgb_output_folder):
    os.makedirs(rgb_output_folder)

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
    create_folders()
    photos_length = os.listdir(rgb_output_folder)
    response = RGB.captureFakeImage()
    new_photos_length = os.listdir(rgb_output_folder)
    if response and len(new_photos_length) > len(photos_length):
        try:
            photos = os.listdir(rgb_output_folder)
            return photos
        except:
            return 0
    else:
        # wait one two seconds and try again
        time.sleep(2)
        response = RGB.captureFakeImage()
        try:
            photos = os.listdir(rgb_output_folder)
            return photos
        except:
            return 0


@rgb_router.get("/rgb-photos/{photo_filename}")
async def get_activity_photo(photo_filename: str):
    create_folders()
    photo_path = str(rgb_output_folder) + str(photo_filename)

    if os.path.isfile(photo_path):
        return FileResponse(photo_path)
    else:
        raise HTTPException(status_code=404, detail="Photo not found")


@rgb_router.get("/rgb-photos/how-many/")
async def get_activity_photo():
    create_folders()
    try:
        photos = os.listdir(rgb_output_folder)
        return photos
    except:
        return 0