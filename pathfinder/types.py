from typing import TypedDict

from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class DataToCity(TypedDict):
    previous_city: City | None
    distance: float


CitiesData = dict[City, DataToCity]
# class PathToCity(TypedDict):
#     city: City
#     cost: float
#     lastCity: City
#
