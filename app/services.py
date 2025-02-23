def calculate_production_plan(payload):
    load = payload.load
    fuels = payload.fuels
    powerplants = payload.powerplants

    # 1️⃣ Calcular costos considerando eficiencia y CO₂
    for plant in powerplants:
        if plant.type == "windturbine":
            plant.cost = 0
        elif plant.type == "gasfired":
            plant.cost = (fuels.gas / plant.efficiency) + (fuels.co2 * 0.3)
        elif plant.type == "turbojet":
            plant.cost = (fuels.kerosine / plant.efficiency)

    # 2️⃣ Ordenar plantas por menor costo
    sorted_plants = sorted(powerplants, key=lambda p: p.cost)

    # 3️⃣ Asignar carga respetando pmin y pmax
    production_plan = []
    remaining_load = load

    for plant in sorted_plants:
        if remaining_load <= 0:
            break

        if plant.type == "windturbine":
            production = min(plant.pmax * fuels.wind / 100, remaining_load)
        else:
            production = max(plant.pmin, min(plant.pmax, remaining_load))

        production = round(production, 1)
        production_plan.append({"name": plant.name, "p": production})
        remaining_load -= production

    # Verificación final: asegurar que la suma de producción debe ser igual o mayor que la carga solicitada
    total_generated = sum(p["p"] for p in production_plan)
    if round(total_generated, 1) < round(load, 1):
         raise ValueError(f"Error en la asignación de carga: esperado {load}, obtenido {total_generated}")

    return production_plan
