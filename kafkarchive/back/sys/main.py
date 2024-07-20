from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
from annotated_types import Len

#numbers for debugging

class number(BaseModel):
    num1: float | None = None
    num2: float | None = None

#fr

class Character(BaseModel):
    id: int
    name: str
    level: int
    ascension: int

class Light_cone(BaseModel):
    id: int
    name: str
    level: int
    ascension: int
    equipped: bool

class Each_substats(BaseModel):
    id: int
    cnt: int
    step: int

class Each_relic(BaseModel):
    setid: int
    setname: str
    level: int
    type: str
    rarity: str
    mainstat: int
    actualtype: str
    substats: Annotated[list[Each_substats], Len(min_length=1, max_length=4)]

class Relics(BaseModel):
    Head: Each_relic | None = None
    Hands: Each_relic | None = None
    Body: Each_relic | None = None
    Feet: Each_relic | None = None
    Planar_Sphere: Each_relic | None = None
    Link_Rope: Each_relic | None = None

class Build_data(BaseModel):
    Character: Character
    Light_cone: Light_cone
    Traces_list: list[int] = []
    Relics: Relics


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

@app.post("/test")
async def test(builddata: Build_data):
    builddict = builddata.model_dump()
    result = builddict["Character"]["name"]
    return result