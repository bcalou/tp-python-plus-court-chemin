from typing import NotRequired, TypedDict
from pathfinder.city import City

class Path(TypedDict):
    total: float
    steps: list[City]

class Step(TypedDict):
    city: City
    origin: 'Step | None'
    bestCost : float
