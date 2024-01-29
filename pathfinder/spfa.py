from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder


class SPFA(Pathfinder):

    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)