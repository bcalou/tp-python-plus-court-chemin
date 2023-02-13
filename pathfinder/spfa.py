from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder


class SPFA(PathFinder):
    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)

    def _loop_condition(self):
        return False
