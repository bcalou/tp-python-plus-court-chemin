from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder


class AStar(Pathfinder):
    heuristics: dict[City, float]

    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        super().__init__(graph)
        self.heuristics = heuristics

    def get_next_city(self) -> City:
        """Return next city if present in unchecked cities,
        else nearest city"""

        if self.end in self.unchecked_cities:
            return self.end
        else:
            return super().get_next_city()

    def get_cost(self, city: City):
        """Override of get cost to take in heuristics"""
        return super().get_cost(city) + self.heuristics[city]
