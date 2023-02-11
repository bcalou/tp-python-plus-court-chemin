from typing import TypedDict
from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class CityInfo(TypedDict):
    closest_city: City
    distance_to_origin: float


CitiesInfosDict = dict[City, CityInfo]
