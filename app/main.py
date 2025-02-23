from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.services import calculate_production_plan

app = FastAPI()

class Fuel(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float
    cost: float = 0  # Se agrega este campo opcional

class Payload(BaseModel):
    load: float
    fuels: Fuel
    powerplants: List[PowerPlant]

@app.post("/productionplan")
async def production_plan(payload: Payload):
    return calculate_production_plan(payload)
