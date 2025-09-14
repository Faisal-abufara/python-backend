from fastapi import FastAPI
import uvicorn

APP = FastAPI()
@APP.get("/")
async def root():
    return {"message": "Hello World"}