"""
Common types declaration
"""

from typing import TypedDict

from typing_extensions import NotRequired

from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class CityInfo(TypedDict):
    distance_from_start: float
    coming_from: NotRequired[City]


Cities = dict[City, CityInfo]

Graph = dict[City, dict[City, float]]
Heuristics = dict[City, float]
