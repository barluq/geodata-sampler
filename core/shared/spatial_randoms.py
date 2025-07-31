import random
from typing import Literal

from shared.value_randoms import _random_float, _random_integer, _random_string

def random_point_coordinates() -> tuple[float, float]:
    """Generate random coordinates for a point."""
    return (random.uniform(-180, 180), random.uniform(-90, 90))


def random_properties_set(attributes: dict[str, Literal["string", "integer", "float"]]) -> dict[str, int | float | str]:
    result: dict = {}
    for key, value in attributes.items():
        if value == "integer":
            result[key] = _random_integer()
        elif value == "float":
            result[key] = _random_float()
        elif value == "string":
            result[key] = _random_string()
        else:
            result[key] = "unknown"
    return result


def random_properties_set_per_year(year_range: tuple[int, int], attributes: dict[str, Literal["string", "integer", "float"]]) -> dict[str, int | float | str]:
    result: dict = {}
    for year in range(year_range[0], year_range[1] + 1):
        for key, value in attributes.items():
            year_key = f"{key}_{year}"
            if value == "integer":
                result[year_key] = _random_integer()
            elif value == "float":
                result[year_key] = _random_float()
            elif value == "string":
                result[year_key] = _random_string()
            else:
                result[year_key] = "unknown"
    return result