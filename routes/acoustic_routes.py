from sqlalchemy.orm import Session
from fastapi import APIRouter
from acoustic.ZedoRPC import ZedoRPC

import schemas
from database import SessionLocal
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from routes.acoustic_crud import create_acoustic_measurement, get_acoustic_measurements

acoustic_router = APIRouter()
ZedoClient = ZedoRPC()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@acoustic_router.post("/acoustic/connect")
def Connect(token: Annotated[str, Depends(oauth2_scheme)]):
    return ZedoClient.Connect()

@acoustic_router.post("/acoustic/disconnect")
def Disconnect(token: Annotated[str, Depends(oauth2_scheme)]):
    return ZedoClient.Disconnect()

@acoustic_router.post("/acoustic/start_rec")
def Start_recording(token: Annotated[str, Depends(oauth2_scheme)], sensor_name: str, record_history_secs: int, measurement_id: int, buffer_size: int):
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.StartRecording(sensor_name, record_history_secs)

@acoustic_router.post("/acoustic/pause_rec")
def Pause_recording(token: Annotated[str, Depends(oauth2_scheme)], measurement_id: int, buffer_size: int):
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.PauseRecording()

@acoustic_router.post("/acoustic/stop_rec")
def Stop_recording(token: Annotated[str, Depends(oauth2_scheme)], measurement_id: int, buffer_size: int):
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.StopRecording()

@acoustic_router.post("/acoustic/export_data")
def Export_data(token: Annotated[str, Depends(oauth2_scheme)]):
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.ExportData("2024-04-27")

@acoustic_router.post("/acoustic/test_save_data",
                      description="Testing endpoint for adding dummy data to measurements table.")
def Test_save_data(body: schemas.MeasurementBase, db: Session = Depends(get_db)):
    return create_acoustic_measurement(db, body)

@acoustic_router.get("/acoustic/get_data",
                     description="Get all acoustic measurements from DB")
def Get_data(db: Session = Depends(get_db)):
    return get_acoustic_measurements(db, skip=0, limit=100)

