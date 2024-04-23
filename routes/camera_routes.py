from sqlalchemy.orm import Session
from fastapi import APIRouter

import schemas
from routes import camera_crud
from database import SessionLocal
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


camera_api_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@camera_api_router.get("/cameras/", response_model=list[schemas.Camera])
def read_cameras(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    cameras = camera_crud.get_cameras(db)
    if cameras is None:
        raise HTTPException(status_code=404, detail="No cameras found")
    return cameras


@camera_api_router.get("/cameras/{camera_id}", response_model=schemas.Camera)
def read_camera(token: Annotated[str, Depends(oauth2_scheme)], camera_id: int, db: Session = Depends(get_db)):
    db_camera = camera_crud.get_camera(db, camera_id=camera_id)
    if db_camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return db_camera

@camera_api_router.post("/cameras/", response_model=schemas.Camera)
def create_camera(token: Annotated[str, Depends(oauth2_scheme)], camera: schemas.CameraBase, db: Session = Depends(get_db)):
    return camera_crud.create_camera(db=db, camera=camera)

@camera_api_router.put("/cameras/{camera_id}", response_model=schemas.Camera)
def update_camera(token: Annotated[str, Depends(oauth2_scheme)], camera_id: int, camera: schemas.CameraBase, db: Session = Depends(get_db)):
    db_camera = camera_crud.get_camera(db, camera_id=camera_id)
    if db_camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera_crud.update_camera(db=db, camera_id=camera_id, camera=camera)

@camera_api_router.delete("/cameras/{camera_id}", response_model=schemas.Camera)
def delete_camera(token: Annotated[str, Depends(oauth2_scheme)], camera_id: int, db: Session = Depends(get_db)):
    return camera_crud.delete_camera(db=db, camera_id=camera_id)