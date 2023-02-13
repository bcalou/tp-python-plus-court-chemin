from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder


class AStar(PathFinder):
    def __init__(self, graph: Graph, heuristics: dict[City, float]) -> None:
        super().__init__(graph)
        self._heuristics: dict[City, float] = heuristics

    def get_weighted_distance_from_nearest_city(self, nearest_city, neighbour):
        return super().get_weighted_distance_from_nearest_city(nearest_city, neighbour) + self._heuristics[neighbour]

    def should_continue_search(self):
        return super().should_continue_search() and not self.is_end_found
