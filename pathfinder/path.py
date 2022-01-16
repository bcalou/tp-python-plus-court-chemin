from importlib.machinery import PathFinder
from typing import TypedDict


from pathfinder.city import City


class path(TypedDict):
    total : float
    steps : list[City]