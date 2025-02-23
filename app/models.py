#Para asegurarnos de que los datos recibidos por la API son correctos antes de procesarlos.
from pydantic import BaseModel, Field
from typing import List

class Fuel(BaseModel):
    gas: float = Field(gt=0, description="Precio del gas en €/MWh")
    kerosine: float = Field(gt=0, description="Precio del kerosene en €/MWh")
    co2: float = Field(gt=0, description="Costo de CO2 en €/ton")
    wind: float = Field(ge=0, le=100, description="Porcentaje de viento disponible")

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float = Field(gt=0, le=1, description="Eficiencia en el rango (0,1]")
    pmin: float = Field(ge=0, description="Producción mínima de la planta")
    pmax: float = Field(gt=0, description="Producción máxima de la planta")
    cost: float = 0  # Se agrega este campo opcional

class Payload(BaseModel):
    load: float = Field(gt=0, description="Carga total que debe generarse")
    fuels: Fuel
    powerplants: List[PowerPlant]
