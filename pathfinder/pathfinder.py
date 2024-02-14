from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.type import Path


class Pathfinder:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    """Returns the shortest path between two cities using Dijkstra's algorithm"""
    def get_shortest_path(self, start: City, end: City) -> Path:
        paths: dict[City, Path] = {start: {"total": 0, "steps": [start]}}
        visited: list[City] = []
        current_city: City = start

        while current_city != end:
            for city, distance in self.graph[current_city].items():
                if city in visited:
                    continue

                path_distance: float = paths[current_city]["total"] + distance

                if city not in paths or path_distance < paths[city]["total"]:
                    steps: list[City] = paths[current_city]["steps"] + [city]
                    paths[city] = {"total": path_distance, "steps": steps}

            visited.append(current_city)
            min_distance = float('inf')
            for city, path in paths.items():
                if city not in visited and path["total"] < min_distance:
                    min_distance = path["total"]
                    current_city = city

        return paths[end]
