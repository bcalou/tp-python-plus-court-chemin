from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder
from pathfinder.types import Path


class AStar(PathFinder):
    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        PathFinder.__init__(self, graph)
        self.heuristics = heuristics

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Calculate the shortest path between two cities using the A* algorithm
        """
        distances = {city: float('inf') for city in self.roads.keys()}
        distances[start] = 0
        previous_city = {city: None for city in self.roads.keys()}
        visited_cities = set()

        current_city = start
        while current_city != end:
            for neighbor, distance in self.roads[current_city].items():
                if distance + distances[current_city] + self.heuristics[neighbor] - self.heuristics[current_city] < distances[neighbor]:
                    distances[neighbor] = distance + distances[current_city] + self.heuristics[neighbor] - self.heuristics[current_city]
                    previous_city[neighbor] = current_city

            visited_cities.add(current_city)
            unvisited_cities = {city for city in self.roads.keys() if city not in visited_cities}

            if not unvisited_cities:
                return {'total': float('inf'), 'steps': []}

            current_city = min(unvisited_cities, key=lambda city: distances[city] + self.heuristics[city])

        path = []

        while previous_city[current_city] is not None:
            path.append(current_city)
            current_city = previous_city[current_city]

        path.append(start)

        return {'total': distances[end], 'steps': list(reversed(path))}
