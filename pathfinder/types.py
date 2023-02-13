from typing import TypedDict

from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class CityInfo(TypedDict):
    """Type used to have information on the current city in the pathfinder
    algorithm"""
    distance: float
    previous_city: City
