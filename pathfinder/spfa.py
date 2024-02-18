from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path


class SPFA(Pathfinder):
    def __init__(self, graph):
        """
        Create a new SPFA pathfinder with the given graph.
        """
        super().__init__(graph)

    def _update_shortest_paths(self, next_city, current_city,
                               cost_to_current_city, shortest_paths) -> bool:
        """
        Update the shortest paths if a shorter path is found.
        """
        cost = self.graph[current_city][next_city] + cost_to_current_city
        if next_city not in shortest_paths or cost < shortest_paths[next_city][
                1]:
            shortest_paths[next_city] = (current_city, cost)
            return True
        return False

    def _get_next_city(self, queue):
        return queue.pop(0)

    def get_shortest_path(self, start, end) -> Path:
        """
        Get the shortest path from start to end using the SPFA algorithm.
        """
        shortest_paths = {start: (None, 0)}
        queue = [start]

        while queue:
            current_city = self._get_next_city(queue)
            destinations = self.graph[current_city]
            cost_to_current_city = shortest_paths[current_city][1]

            for next_city in destinations:
                if self._update_shortest_paths(next_city, current_city,
                                               cost_to_current_city,
                                               shortest_paths):
                    queue.append(next_city)

        path, cost = self._build_path_and_cost(end, shortest_paths)
        return Path(total=cost, steps=path)
