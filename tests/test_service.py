from app.services import calculate_production_plan

def test_production_plan():
    payload = {
        "load": 480,
        "fuels": {"gas(euro/MWh)": 13.4, "kerosine(euro/MWh)": 50.8, "co2(euro/ton)": 20, "wind(%)": 60},
        "powerplants": [
            {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
            {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 150}
        ]
    }
    result = calculate_production_plan(payload)
    assert sum(p["p"] for p in result) == 480  # Verificar que la carga se cumple
    