from pathfinder.pathfinder import PathFinder
from typing import Dict, TypedDict
from pathfinder.city import City
from pathfinder.path import Path

class AStar(PathFinder):
    heuristics: dict[City, int]

    def __init__(self, graph: dict[City, dict[City, int]], heuristics: dict[City, int]):
        self.graph = graph
        self.heuristics = heuristics
