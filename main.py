import uvicorn

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import user_model
from database import  engine
from routes.user_routes import user_api_router
from routes.camera_routes import camera_api_router
from routes.rgb_routes import rgb_router

user_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_api_router)
app.include_router(camera_api_router)
app.include_router(rgb_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
