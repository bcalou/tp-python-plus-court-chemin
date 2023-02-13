from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder
from pathfinder.types import Path


class SPFA(PathFinder):
    def __init__(self, graph: Graph):
        PathFinder.__init__(self, graph)
        self.is_city_in_list: dict[City, bool] = {}

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Calculate the shortest path between two cities using spfa algorithm
        """
        distances = {city: float('inf') for city in self.roads.keys()}

        distances[start] = 0
        previous = {city: None for city in self.roads.keys()}
        queue = [start]
        self.is_city_in_list[start] = True

        while queue:
            current = queue.pop(0)
            self.is_city_in_list[current] = False
            for neighbor, weight in self.roads[current].items():
                if distances[neighbor] > distances[current] + weight:
                    distances[neighbor] = distances[current] + weight
                    previous[neighbor] = current
                    if not self.is_city_in_list[neighbor]:
                        queue.append(neighbor)
                        self.is_city_in_list[neighbor] = True

        path = []
        current = end
        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()

        return {"total": distances[end], "steps": path}

