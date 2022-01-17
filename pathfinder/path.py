from pathfinder.city import City
from typing import TypedDict

class Path(TypedDict):
    total: float
    steps: list[City]