from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.type import Path


class Pathfinder:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Returns the shortest path between two cities using Dijkstra's algorithm"""
        paths: dict[City, Path] = {start: {"total": 0, "steps": [start]}}
        visited: list[City] = []
        current_city: City = start

        while not self.is_loop_ended(current_city, end, paths):
            for city, distance in self.graph[current_city].items():
                if city in visited:
                    continue

                path_distance: float = paths[current_city]["total"] + distance

                # If the city is not in the paths or the new path is shorter
                if city not in paths or path_distance < paths[city]["total"]:
                    steps: list[City] = paths[current_city]["steps"] + [city]
                    paths[city] = {"total": path_distance, "steps": steps}

            visited.append(current_city)

            current_city = self.find_next_city(current_city, paths, visited)

        return paths[end]

    def is_loop_ended(self, current_city, end, paths: dict[City, Path]):
        """Check if the loop should be ended"""
        return current_city == end

    def find_next_city(self, current_city, paths: dict[City, Path], visited):
        """Find the next city to visit
        (the one with the shortest path from the start city)"""
        # Find the next city to visit
        min_distance = float('inf')
        for city, path in paths.items():
            if city not in visited and path["total"] < min_distance:
                min_distance = path["total"]
                current_city = city
        return current_city
