from pathfinder.pathfinder import PathFinder
from pathfinder.heuristics import heuristics

class AStar(PathFinder):
    def __init__(self, graph, heuristics) -> None:
        super().__init__(graph)
        self.heuristics = heuristics
