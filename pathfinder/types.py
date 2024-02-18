from typing import TypedDict
from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class Step(TypedDict):
    city: City
    origin: 'Step | None'
    bestCost: float


Graph = dict[City, dict[City, float]]

Heuristic = dict[City, float]
