from pathfinder.types import Path, CityInfo
from pathfinder.graphs import Graph
from pathfinder.city import City


class PathFinder:
    def __init__(self, graph: Graph):
        self.roads = graph

        self.cities_info: dict[City, CityInfo] = {}
        for city in self.roads.keys():
            self.cities_info[city] = {'distance': float('inf'), 'previous_city': None}

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Calculate the shortest path between two cities using Dijkstra's algorithm
        """

        self.cities_info[start] = {'distance': 0, 'previous_city': None}

        visited_cities = set()

        current_city = start
        while current_city != end:
            for neighbor, distance in self.roads[current_city].items():
                if distance + self.cities_info[current_city]['distance'] < self.cities_info[neighbor]['distance']:
                    self.cities_info[neighbor]['distance'] = distance + self.cities_info[current_city]['distance']
                    self.cities_info[neighbor]['previous_city'] = current_city

            visited_cities.add(current_city)
            unvisited_cities = {city for city in self.roads.keys() if city not in visited_cities}

            if not unvisited_cities:
                return {'total': float('inf'), 'steps': []}

            # Yes I dared to use a lambda :)
            current_city = min(unvisited_cities, key=lambda city: self.cities_info[city]['distance'])

        path = []

        while self.cities_info[current_city]['previous_city'] is not None:
            path.append(current_city)
            current_city = self.cities_info[current_city]['previous_city']

        path.append(start)

        return {'total': self.cities_info[end]['distance'], 'steps': list(reversed(path))}
