from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder


class AStar(PathFinder):

    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        PathFinder.__init__(self, graph)
        self._heuristics = heuristics
