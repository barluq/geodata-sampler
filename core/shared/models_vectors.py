from typing import NamedTuple

class VectorEntityFeature(NamedTuple):
    geometry: dict
    properties: dict

class VectorEntity(NamedTuple):
    crs: str
    features: list[VectorEntityFeature]