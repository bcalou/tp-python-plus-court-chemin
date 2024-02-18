from pathfinder.pathfinder import Pathfinder
from pathfinder.types import City
from pathfinder.types import Graph
from pathfinder.types import Path
from pathfinder.types import Step


class SPFA(Pathfinder):

    def __init__(self, graph: Graph):
        Pathfinder.__init__(self, graph)

    def _can_continue_research(self) -> bool:
        """Express the condition to continue explore new cities.
        Here, the end city must not be processed"""
        for city in self._graph:
            if city not in self._processed_cities:
                return True
        return False
