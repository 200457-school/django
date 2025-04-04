TRANSPORTATION_CO2_PER_KM = 0.21  # grams of CO2 per km
ENERGY_CO2_PER_KWH = 0.233  # grams of CO2 per kWh
WASTE_CO2_PER_KG = 0.5  # grams of CO2 per kg of waste

def calculate_co2_emissions(transportation_km, energy_kWh, waste_kg):
    transportation_emissions = transportation_km * TRANSPORTATION_CO2_PER_KM
    energy_emissions = energy_kWh * ENERGY_CO2_PER_KWH
    waste_emissions = waste_kg * WASTE_CO2_PER_KG
    total_emissions = transportation_emissions + energy_emissions + waste_emissions
    return total_emissions
