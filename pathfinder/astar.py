"""
Astar pathfinder
"""

from pathfinder.city import City
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Graph, Heuristics


class AStar(Pathfinder):
    """A* algorithm"""

    def __init__(self, graph: Graph, heuristics: Heuristics):
        super().__init__(graph)
        self._heuristics = heuristics

    def _is_finished(self) -> bool:
        """Return True if the algorithm has finished it's job"""

        # Algorithm has finished as soon as a solution has been found
        return self._cities[self._end]["distance_from_start"] != float('inf')

    def _get_city_distance_evaluation(self, city: City) -> float:
        """Add the heuristic to the distance for better evaluation"""

        return (
            super()._get_city_distance_evaluation(city)
            + self._heuristics[city]
        )
