from pathfinder.pathfinder import Pathfinder
from pathfinder.types import City
from pathfinder.types import Graph
from pathfinder.types import Path
from pathfinder.types import Step


class SPFA(Pathfinder):

    def __init__(self, graph: Graph):
        Pathfinder.__init__(self, graph)

    def _lowest_cost_in_discoverd_cities(self) -> Step:
        """Here we don't want the cheapest, but the first not processed city"""
        if len(self._discovered_steps) > 0:
            return self._discovered_steps[0]
        return self._processed_steps[0]
    # The funtion works but is apparently not the only thing to change

    def _can_continue_research(self) -> bool:
        """Express the condition to continue explore new cities.
        Here, the end city must not be processed"""
        for city in self._graph:
            if city not in self._processed_cities:
                return True
        return False
