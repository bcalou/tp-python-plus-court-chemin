from typing import TypedDict, List
from pathfinder.city import City

class Path(TypedDict):
    total: float
    steps: List[City]

class ShortestPathInfo(TypedDict):
    closest_city: City
    distance: float
