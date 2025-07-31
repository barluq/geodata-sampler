import random


_random_urban_spatial_attributes: dict[str, str | int | float] = {
    "population_density": "integer",
    "land_use": "string",
    "building_height": "float",
    "green_space_ratio": "float",
    "transportation_accessibility": "string",
    "urban_infrastructure_quality": "string",
    "socioeconomic_status": "string",
    "crime_rate": "float",
    "public_services_availability": "string",
    "cultural_attractions": "string",
    "environmental_quality": "string",
    "urban_heat_island_effect": "float",
    "walkability_score": "float",
    "bicycle_infrastructure": "string",
    "public_transportation_quality": "string",
    "urban_greening_initiatives": "string", 
}

_year_range: tuple[int, int] = (2000, 2023)


def random_point_coordinates() -> tuple[float, float]:
    """Generate random coordinates for a point."""
    return (random.uniform(-180, 180), random.uniform(-90, 90))


def random_properties_set(year_range: tuple[int, int]) -> dict[str, int | float | str]:
    result: dict = {}
    for year in range(year_range[0], year_range[1] + 1):
        for key, value in _random_urban_spatial_attributes.items():
            year_key = f"{key}_{year}"
            if value == "integer":
                result[year_key] = random.randint(1, 100)
            elif value == "float":
                result[year_key] = random.uniform(0.0, 100.0)
            elif value == "string":
                result[year_key] = random.choice(["low", "medium", "high", "very high"])
            else:
                result[year_key] = "unknown"
    return result