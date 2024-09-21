from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Annotated
from annotated_types import Len
from build_calculator import *
from build_calculator.fetchdata import fetch

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
    step: int | None = None

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

class UserID(BaseModel):
    UssrID: int

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

@app.post("/build_calc")
async def build_calc(builddata: Build_data):
    builddict = builddata.model_dump()
    result = await build_calculation(builddict, "True")
    return result

@app.post("/fetch_raw")
async def fetch_raw(uid: UserID):
    packed = {}
    uiddict = uid.model_dump()
    data = await fetch(uiddict["UssrID"])
    for chars in data:
        response = await build_calculation(data[str(chars)], "raw")
        packed.update({chars : response})
    
    return packed

@app.post("/fetch_numdata")
async def fetch_numdata(uid: UserID):
    packed = {}
    uiddict = uid.model_dump()
    data = await fetch(uiddict["UssrID"])
    for chars in data:
        response = await build_calculation(data[str(chars)], "numdata")
        packed.update({chars : response})
    
    return packed

@app.post("/fetch_cooked")
async def fetch_cooked(uid: UserID):
    packed = {}
    uiddict = uid.model_dump()
    data = await fetch(uiddict["UssrID"])
    for chars in data:
        response = await build_calculation(data[str(chars)], "True")
        packed.update({chars : response})
    
    return packed
    

get_char_data_types = "datatypes : name, description, stats, icon, shortIcon, drawIcon, rarity, element, skills, promos, avatarType, promotion, treePromotion, maxPromo, exp, tree, ranks, statsArray, promoarrays, advancement, va, id"

@app.get("/data/chars/{datatype}", description=get_char_data_types)
async def get_chars_data(datatype: str):
    return await forward_amogus_get_chars_data(datatype)

get_relic_data_types = "datatypes : name, setID, two, twopc, four, fourpc, params, props, setIcon, planarSet"

@app.get("/data/relics/{datatype}", description=get_relic_data_types)
async def get_relic_data(datatype: str):
    return await forward_amogus_get_relic_data(datatype)

get_lightcone_data_types = "datatypes : name, icon, shortIcon, rarity, weaponType, refinements, maxHP, maxATK, maxDEF, promotion, promo, params, passives, id"

@app.get("/data/lightcones/{datatype}", description=get_lightcone_data_types)
async def get_lightcone_data(datatype: str):
    return await forward_amogus_get_lc_data(datatype)

img_path = R"build_calculator\amogus\jsonsdata\img"

@app.get("/img/char/{id}")
async def get_char_img(id):
    return FileResponse(Rf"{img_path}\chars\{id}.png")

@app.get("/img/charbig/{id}")
async def get_char_img(id):
    return FileResponse(Rf"{img_path}\charbig\{id}.png")

@app.get("/img/lightcones/{id}")
async def get_char_img(id):
    return FileResponse(Rf"{img_path}\lightcones\{id}.png")

@app.get("/img/relics/{id}/{relictype}")
async def get_char_img(id, relictype):
    return FileResponse(Rf"{img_path}\relics\IconRelic_{id}_{relictype}.png")