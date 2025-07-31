import random
from typing import Literal

from core.shared.value_randoms import random_float, random_integer, random_string

def random_point_coordinates() -> tuple[float, float]:
    """Generate random coordinates for a point."""
    return (random.uniform(-180, 180), random.uniform(-90, 90))


def random_properties_set(attributes: dict[str, Literal["string", "integer", "float"]]) -> dict[str, int | float | str]:
    """
    Generates a dictionary of random property values based on specified attribute types.

    Args:
        attributes (dict[str, Literal["string", "integer", "float"]]):
            A dictionary mapping attribute names to their expected types ("string", "integer", or "float").

    Returns:
        dict[str, int | float | str]:
            A dictionary where each key corresponds to an attribute name and each value is a randomly generated value
            of the specified type. If an unknown type is provided, the value will be set to "unknown".

    Example:
        >>> random_properties_set({"name": "string", "age": "integer", "height": "float"})
        {'name': 'abcde', 'age': 42, 'height': 1.23}
    """
    result: dict = {}
    for key, value in attributes.items():
        if value == "integer":
            result[key] = random_integer()
        elif value == "float":
            result[key] = random_float()
        elif value == "string":
            result[key] = random_string()
        else:
            result[key] = "unknown"
    return result


def random_properties_set_per_year(year_range: tuple[int, int], attributes: dict[str, Literal["string", "integer", "float"]]) -> dict[str, int | float | str]:
    """
    Generates a dictionary of random property values for each year in a given range.

    For each attribute specified in the `attributes` dictionary, this function creates a key for every year in the `year_range`, appending the year to the attribute name (e.g., "attribute_2020"). The value for each key is randomly generated based on the specified type: "integer", "float", or "string".

    Args:
        year_range (tuple[int, int]): A tuple specifying the start and end year (inclusive).
        attributes (dict[str, Literal["string", "integer", "float"]]): A dictionary mapping attribute names to their value types.

    Returns:
        dict[str, int | float | str]: A dictionary where keys are attribute names suffixed with the year, and values are randomly generated according to the specified type.
    """
    result: dict = {}
    for year in range(year_range[0], year_range[1] + 1):
        for key, value in attributes.items():
            year_key = f"{key}_{year}"
            if value == "integer":
                result[year_key] = random_integer()
            elif value == "float":
                result[year_key] = random_float()
            elif value == "string":
                result[year_key] = random_string()
            else:
                result[year_key] = "unknown"
    return result