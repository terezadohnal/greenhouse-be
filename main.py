import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from models import user_model
from database import SessionLocal, engine
from routes.user_routes import user_api_router

user_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)