from pathfinder.graphs import Graph
from pathfinder.city import City
from pathfinder.types import Path


class Pathfinder:
    def __init__(self, graph: Graph):
        self.graph = graph

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

            next_destinations = {city: shortest_paths[city] for city in
                                 shortest_paths if city not in visited}
            # if not next_destinations:
            #    return "Route Not Possible"
            current_city = self._get_next_city(next_destinations)

        path, cost = self._build_path_and_cost(end, shortest_paths)
        return Path(total=cost, steps=path)

    def _update_shortest_paths(self, next_city: City, current_city: City,
                               cost_to_current_city: float,
                               shortest_paths: dict) -> None:
        """
        Updates the shortest path if a shorter path is found.
        """
        cost = self.graph[current_city][next_city] + cost_to_current_city
        if next_city not in shortest_paths:
            shortest_paths[next_city] = (current_city, cost)
        else:
            current_lowest_cost = shortest_paths[next_city][1]
            if current_lowest_cost > cost:
                shortest_paths[next_city] = (current_city, cost)

    def _get_next_city(self, next_destinations: dict):
        """
        Returns the next city to visit.
        """
        return min(next_destinations, key=lambda k: next_destinations[k][1])

    def _build_path_and_cost(self, end: City, shortest_paths: dict) -> tuple[
            list[City], float]:
        """
        Returns the path and total cost of the path.
        """
        path = []
        total_cost = 0
        current_city = end
        while current_city is not None:
            path.append(current_city)
            next_city, cost = shortest_paths[current_city]
            if next_city is not None:  # Prevent adding cost for the start city
                total_cost += self.graph[next_city][current_city]
            current_city = next_city
        return path[::-1], total_cost  # Return reversed path and total cost
