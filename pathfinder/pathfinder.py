from pathfinder.graphs import *
from pathfinder.types import *


class PathFinder:
    """Class implementing the Dijkstra's algorithm to find the shortest path
    between 2 points of a graph"""

    def __init__(self, graph: Graph):
        self._graph: Graph = graph
        self._start_city: City
        self._end_city: City
        self._path: Path
        self._found_end_city: bool = False
        self._cities_infos_dict: CitiesInfosDict
        self._cities_to_visit: list[City] = []
        self._visited_cities: list[City] = []
        self._computed_distances_count: int = 0

    def get_shortest_path(self, start_city: City, end_city: City):
        """The only public method, the one to call. May vary depending on the
        algorithm used"""

        self._reset_variables(start_city, end_city)

        while len(self._cities_to_visit) > 0:
            city_to_visit: City = self._get_next_city_to_visit()
            self._visit_city(city_to_visit)

        # print(f'self._computed_distances_count : {self._computed_distances_count}')
        self._path = self._get_path()
        return self._path

    def _reset_variables(self, start_city: City, end_city: City):
        """Method reseting all the variables to get a fresh start when
        computing a new path"""

        self._start_city = start_city
        self._end_city = end_city
        self._found_end_city = False
        self._cities_infos_dict = self._init_cities_infos_dict()
        self._cities_to_visit = [start_city]
        self._visited_cities = []
        self._computed_distances_count = 0

    def _init_cities_infos_dict(self) -> CitiesInfosDict:
        """Method creating a blank dictionnary containing each city's info
        (the total distance to origin and the city to come from to get the
        shortest path)"""

        cities_info_dict: CitiesInfosDict = {}

        for city in City:
            if city == self._start_city:
                cities_info_dict[city] = {
                    "closest_city": city,
                    "distance_to_origin": 0
                }
            else:
                cities_info_dict[city] = {
                    "closest_city": city,
                    "distance_to_origin": float("inf")
                }

        return cities_info_dict

    def _get_next_city_to_visit(self) -> City:
        """Method identifying the next city to be visited by the algorithm
        amont the cities in the list"""

        next_city_to_visit: City
        next_city_weight: float = float("inf")

        for city in self._cities_to_visit:
            city_weight: float = self._get_city_weight(city)

            if city_weight < next_city_weight:
                next_city_to_visit = city
                next_city_weight = city_weight

        return next_city_to_visit

    def _get_city_weight(self, city: City) -> float:
        """Method computing the weight of a city. May vary depending on the
        algorithm used"""

        return self._cities_infos_dict[city]["distance_to_origin"]

    def _visit_city(self, city: City):
        """Method visiting a city : checking if connected cities are relevant
        to be visited"""

        if city == self._end_city:
            self._found_end_city = True

        for connected_city in self._graph[city]:

            if self._should_skip_city(connected_city):
                continue

            if self._should_visit_city_when_met(connected_city):
                self._cities_to_visit.append(connected_city)
            
            self._update_city_weight(connected_city, city)

        self._cities_to_visit.remove(city)
        self._visited_cities.append(city)

    def _should_skip_city(self, city: City) -> bool:
        """Determine wether there is no need to visit a city. May vary
        depending on the algorithm used"""

        return True if city in self._visited_cities else False

    def _should_visit_city_when_met(self, city: City) -> bool:
        """Determine whether the algorithm should visit a city when it meets
        one. May vary depending on the algorithm used"""

        if city not in self._cities_to_visit and (self._get_city_weight(city) <= self._get_city_weight(self._end_city)):
            return True
        else:
            return False
    
    def _update_city_weight(self, connected_city: City, parent_city: City):
        """Method to update the weight of a city if needed"""

        new_weight: float = self._get_city_weight(parent_city) + self._graph[parent_city].get(connected_city)
        old_weight: float = self._get_city_weight(connected_city)

        if new_weight < old_weight:
            self._cities_infos_dict[connected_city]["closest_city"] = parent_city
            self._cities_infos_dict[connected_city]["distance_to_origin"] = (
                self._cities_infos_dict[parent_city]["distance_to_origin"] + self._graph[parent_city].get(connected_city)
            )
            self._computed_distances_count += 1

            if self._should_visit_city_when_weight_changed(connected_city):
                self._cities_to_visit.append(connected_city)

    def _should_visit_city_when_weight_changed(self, city) -> bool:
        """Determine whether the algorithm should visit a city when its weight
        was updated. May vary depending on the algorithm used"""
        return False

    def _get_path(self) -> Path:
        """Method to compute the path when to graph has finished being
        explorated"""

        path: Path = {
            "total": self._cities_infos_dict[self._end_city]["distance_to_origin"],
            "steps": [self._end_city]
        }
        next_step: City = self._end_city

        while not next_step == self._start_city:
            path["steps"].insert(0, self._cities_infos_dict[next_step]["closest_city"])
            next_step = self._cities_infos_dict[next_step]["closest_city"]

        return path
