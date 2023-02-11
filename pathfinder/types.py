from typing import TypedDict
from pathfinder.city import City
from typing_extensions import NotRequired

class Path(TypedDict):
    total: float
    steps: list[City]

class CityInfo(TypedDict):
    distance: float
    come_from: NotRequired[City]