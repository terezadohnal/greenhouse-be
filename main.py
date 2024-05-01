import uvicorn

from fastapi import FastAPI, __version__
from fastapi.middleware.cors import CORSMiddleware
from models import user_model
from database import  engine
from routes.user_routes import user_api_router
from routes.camera_routes import camera_api_router
from fastapi.responses import HTMLResponse
from time import time

user_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_api_router)
app.include_router(camera_api_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
