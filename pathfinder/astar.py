from pathfinder.graphs import graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.types import Path


class AStar(Pathfinder):
    def __init__(self, graph, heuristics):
        super().__init__(graph)
        self.heuristics = heuristics

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Returns the shortest path between two cities and the total cost of the
        path.
        """
        shortest_paths = {start: (None, 0)}
        current_city = start
        visited = set()

        while current_city != end:
            visited.add(current_city)
            destinations = self.graph[current_city]
            cost_to_current_city = shortest_paths[current_city][1]

            for next_city in destinations:
                self._update_shortest_paths(next_city, current_city,
                                            cost_to_current_city,
                                            shortest_paths)

            next_destinations = {
                city: (shortest_paths[city][1] + self.heuristics[city], city)
                for city in shortest_paths if city not in visited}

            current_city = min(next_destinations,
                               key=lambda city: next_destinations[city][0])

        path, cost = self._build_path_and_cost(end, shortest_paths)
        return Path(total=cost, steps=path)
