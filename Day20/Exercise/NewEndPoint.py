from fastapi import FastAPI
import uvicorn
UserName=input("Enter your name: ")
APP = FastAPI()
@APP.get("/")
def read_root():
    return {f"Hello": {UserName}}