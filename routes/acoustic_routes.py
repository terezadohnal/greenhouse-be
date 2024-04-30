from sqlalchemy.orm import Session
from fastapi import APIRouter
from acoustic.ZedoRPC import ZedoRPC

import schemas
from database import SessionLocal
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


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
def Connect():
    return ZedoClient.Connect()

@acoustic_router.post("/acoustic/disconnect")
def Disconnect():
    return ZedoClient.Disconnect()

@acoustic_router.post("/acoustic/start_rec")
def Start_recording():
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.StartRecording("test")

@acoustic_router.post("/acoustic/pause_rec")
def Pause_recording():
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.PauseRecording()

@acoustic_router.post("/acoustic/stop_rec")
def Stop_recording():
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.StopRecording()

@acoustic_router.post("/acoustic/export_data")
def Export_data():
    if not ZedoClient.Is_connected():
        ZedoClient.Connect()
    return ZedoClient.ExportData("2024-04-27")