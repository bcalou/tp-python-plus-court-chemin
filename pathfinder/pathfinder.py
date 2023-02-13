from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path
from pathfinder.types import CityOrigin


class PathFinder:
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.cities_to_visit: list[City] = []
        self.cities_origins: dict[City, CityOrigin] = {}
        self.is_end_found: bool = False
        self.end_city: City

    def __setup_cities_origin(self):

        for city in self.graph.keys():
            self.cities_origins[city] = {
                'origin': city, 'total_distance': float("inf")}

    def get_shortest_path(self, start: City, end: City) -> Path:

        self.__setup_cities_origin()

        self.end_city = end
        self.is_end_found = False

        # Setup start city at 0 distance
        self.cities_origins[start]['total_distance'] = 0
        self.cities_to_visit.append(start)
        while self.should_continue_search():
            current_city: City = self.__get_nearest_city()

            self.__compute_nearest_city_neighbourgs(current_city)

        path_cities: list[City] = [end]

        while path_cities[-1] != start:
            path_cities.append(self.cities_origins[path_cities[-1]]['origin'])

        path_cities.reverse()
        shortest_path: Path = {
            'total': self.cities_origins[end]['total_distance'], 'steps': path_cities}

        return shortest_path

    def should_continue_search(self):
        return len(self.cities_to_visit) > 0

    def __get_nearest_city(self) -> City:

        if len(self.cities_to_visit) == 1:
            return self.cities_to_visit[0]

        nearest_distance = float("inf")
        nearest_city: City = self.cities_to_visit[0]

        for city in self.cities_to_visit:
            city_distance: float = self.cities_origins[city]['total_distance']
            if city_distance < nearest_distance:
                nearest_distance = city_distance
                nearest_city = city

        return nearest_city

    def __compute_nearest_city_neighbourgs(self, nearest_city: City):

        for neighbour in self.graph[nearest_city]:

            self.compute_neighbourg_distance(nearest_city, neighbour)
        self.cities_to_visit.remove(nearest_city)

    def check_add_to_city_to_visit(self, neighbour):

        if not neighbour in self.cities_to_visit:
            self.cities_to_visit.append(neighbour)

    def compute_neighbourg_distance(self, nearest_city, neighbour):
        distance_from_nearest_city = self.get_distance_from_nearest_city(
            nearest_city, neighbour)
        weighted_distance_from_nearest_city = self.get_weighted_distance_from_nearest_city(
            nearest_city, neighbour)
        distance_from_current_origin = self.cities_origins[neighbour]['total_distance']
        if weighted_distance_from_nearest_city < distance_from_current_origin:
            self.check_add_to_city_to_visit(neighbour)
            self.cities_origins[neighbour] = {
                'origin': nearest_city,
                'total_distance': distance_from_nearest_city
            }
            if neighbour == self.end_city:
                self.is_end_found = True

    def get_weighted_distance_from_nearest_city(self, nearest_city, neighbour):
        return self.get_distance_from_nearest_city(nearest_city, neighbour)

    def get_distance_from_nearest_city(self, nearest_city, neighbour):
        return self.graph[nearest_city][neighbour] + \
            self.cities_origins[nearest_city]['total_distance']
