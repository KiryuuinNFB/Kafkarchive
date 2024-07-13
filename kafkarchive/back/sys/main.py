from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class number(BaseModel):
    num1: float | None = None
    num2: float | None = None

app = FastAPI()

allowed = ["http://26.140.165.255:5173/",
           "http://localhost:5173/",
           "http://127.0.0.1:8000/calc"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {"msg": "lmao"}

@app.post("/calc")
async def calc(number: number):
    num_dict = number.model_dump()
    result = num_dict["num1"] + num_dict["num2"]
    result_dict = dict(result = result)
    return result_dict