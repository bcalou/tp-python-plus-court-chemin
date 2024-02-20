from pathfinder.graphs import Graph
from pathfinder.types import City, Path, ShortestPathInfo


class Pathfinder:
    """The main class is the parent Dijkstra's algorithm used to
    find the shortest path between two cities in a graph."""

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.start: City  # The start city
        self.end: City  # The end city
        self.path: Path  # The shortest path found
        self.finished: bool = False  # Whether the pathfinding process is finished
        self.city_info: dict[City, ShortestPathInfo] = {}  # Information about each city's shortest path
        self.visited_cities: list[City] = []  # The cities that have been visited
        self.unvisited_cities = {}  # The cities that haven't been visited

    def get_shortest_path(self, start: City, end: City) -> Path:
        """This method finds the shortest path between the start and end cities,
        it is the main method of the whole algorithm."""
        self.start = start
        self.end = end
        self.finished = False
        self.initialize_city_info()
        self.city_info[start]['distance'] = 0
        self.visited_cities.clear()
        current_city = start

        # Process cities until we reach the end city.
        while current_city != end:
            current_city = self.process_city(current_city)
            if self.finished:
                break

        # Reconstruct the shortest path when the main algorithm is done
        return self.reconstruct_path()

    def initialize_city_info(self) -> None:
        """This method initializes the city's distance to origin
        and the current closest city once the algorithm starts"""
        for city in self.graph:
            self.city_info[city] = {
                'closest_city': None,
                'distance': float('inf')  # float(inf) means infinity
            }

    def process_city(self, current_city: City) -> None:
        """This method processes a city by visiting it
        and then getting the next city to visit"""
        self.visit_city(current_city)
        if not self.finished:
            current_city = self.get_next_city()

        return current_city

    def get_next_city(self) -> City:
        """This method determines the next city to visit
        which is the unvisited city with the smallest distance"""
        self.unvisited_cities = {
            city: info['distance']
            for city, info in self.city_info.items()
            if city not in self.visited_cities
        }
        return min(self.unvisited_cities, key=self.unvisited_cities.get)

    def visit_city(self, current_city: City) -> None:
        self.visited_cities.append(current_city)
        self.process_neighbors(current_city)
        if current_city == self.end:
            self.finished = True

    def process_neighbors(self, current_city: City) -> None:
        for neighbor, weight in self.graph[current_city].items():
            if neighbor not in self.visited_cities:
                self.update_neighbor(neighbor, current_city, weight)

    def update_neighbor(self, neighbor: City, current_city: City, weight: float) -> None:
        """This method updates a neighbor's shortest path information"""
        current_distance = self.city_info[current_city]['distance']
        total_distance = current_distance + weight

        if total_distance < self.city_info[neighbor]['distance']:
            self.city_info[neighbor]['closest_city'] = current_city
            self.city_info[neighbor]['distance'] = total_distance

    def reconstruct_path(self) -> Path:
        """This method reconstructs the shortest path from the start city to the end city"""
        shortest_path: Path = {
            "total": self.city_info[self.end]['distance'],
            "steps": []
        }
        current_city = self.end

        while current_city != self.start:
            shortest_path['steps'].insert(0, current_city)
            current_city = self.city_info[current_city]['closest_city']

        shortest_path['steps'].insert(0, self.start)
        return shortest_path
