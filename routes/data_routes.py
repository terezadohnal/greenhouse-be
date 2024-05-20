from sqlalchemy.orm import Session
from fastapi import APIRouter
from acoustic.ZedoRPC import ZedoRPC
from typing import Annotated

import schemas
from database import SessionLocal
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from routes.acoustic_crud import create_acoustic_measurement, get_acoustic_measurements

data_router = APIRouter()
ZedoClient = ZedoRPC()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@data_router.post("/data/getDefaultPath")
def Connect(token: Annotated[str, Depends(oauth2_scheme)]):
    return ZedoClient.DEFAULT_DIR_PATH

@data_router.get("/data/get_data", description="Get all acoustic measurements")
def Get_data(token: Annotated[str, Depends(oauth2_scheme)], dir=ZedoClient.DEFAULT_DIR_PATH):
    return ZedoClient.GetAllMeasurement(dir)

@data_router.get("/data/download_data_FileResponse", description="Download one measurement")
def Download_data(token: Annotated[str, Depends(oauth2_scheme)],  measurement: str, dir=ZedoClient.DEFAULT_DIR_PATH):
    return ZedoClient.DownloadMeasurementFileResponse(measurement, dir)

@data_router.get("/data/download_data_DataStreaming", description="Download one measurement")
def Download_data(token: Annotated[str, Depends(oauth2_scheme)],  measurement: str, dir=ZedoClient.DEFAULT_DIR_PATH):
    return ZedoClient.DownloadMeasurementDataStreaming(measurement, dir)

