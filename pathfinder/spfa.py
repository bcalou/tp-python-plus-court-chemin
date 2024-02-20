from collections import deque
from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path

class SPFA(Pathfinder):

    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)
        self.queue = deque()