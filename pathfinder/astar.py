from pathfinder.pathfinder import PathFinder
from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.heuristics import heuristics
import math

class AStar(PathFinder):
    def __init__(self, graph: Graph, heuristics: dict[City, float]) -> None:
        super().__init__(graph)
        self.heuristics: dict[City, float] = heuristics

    def sort_visits(self) -> None:
        """Algo de tri des villes à visiter, à modifier en fonction de l'algo"""
        self.to_visit.sort(
            key=lambda city: self.villes[city]["cout"] + self.heuristics[city]
        )

    def finished(self) -> bool:
        """Condition de fin de l'algo, à modifier en fonction de l'algo"""
        return self.min_to_end < math.inf