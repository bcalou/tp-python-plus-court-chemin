from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path


class AStar(Pathfinder):
    __heuristics: dict[City, float]

    def __init__(self, graph: Graph, heuristics: dict[City, float]) -> None:
        super().__init__(graph)
        self.__heuristics = heuristics

    def _optimal_path(self):
        """Returns A*'s definition of the optimal path"""
        optimal_path: Path = self._paths[0]

        for path in self._paths:
            if path["steps"][-1] == self._end:
                return path
            
            if self._weighted_total(path) < self._weighted_total(optimal_path):
                optimal_path = path

        return optimal_path
    
    def _weighted_total(self, path: Path) -> float:
        return path["total"] + self.__heuristics[path["steps"][-1]]