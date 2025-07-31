
import random

def random_float(negative: bool = False) -> float:
    """Generate a random float, optionally negative."""
    min = -100.0 if negative else 0.0
    value = random.uniform(min, 100.0)
    return -value if negative else value

def random_integer(negative: bool = False) -> int:
    """Generate a random integer, optionally negative."""
    min = -100 if negative else 0
    value = random.randint(min, 100)
    return -value if negative else value

def random_string() -> str:
    """Generate a random string from a predefined set."""
    return random.choice(["low", "medium", "high", "very high"])