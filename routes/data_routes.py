from sqlalchemy.orm import Session
from fastapi import APIRouter
from acoustic.ZedoRPC import ZedoRPC

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

@data_router.get("/data/get_data",
                     description="Get all acoustic measurements from DB")
def Get_data(token: Annotated[str, Depends(oauth2_scheme)], dir):
    return ZedoClient.GetAllMeasurement(dir)


