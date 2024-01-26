from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path

class SPFA(Pathfinder):
    def __init__(self, graph):
        super().__init__(graph)
    
    def get_shortest_path(self, start, end):
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
                city: shortest_paths[city]
                for city in shortest_paths if city not in visited}
            
            current_city = self._get_next_city(next_destinations)

        path, cost = self._build_path_and_cost(end, shortest_paths)
        return Path(total=cost, steps=path)