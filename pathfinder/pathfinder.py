from pathfinder.graphs import *
from pathfinder.types import *


class PathFinder:
    def __init__(self, graph: Graph):
        self._graph: Graph = graph
        self._start_city: City
        self._end_city: City
        self._cities_infos_dict: CitiesInfosDict
        self._cities_to_visit: list[City] = []
        self._visited_cities: list[City] = []
        self._computed_distances_count: int = 0
    
    def get_shortest_path(self, start_city: City, end_city: City):
        self._reset_variables(start_city, end_city)

        while len(self._cities_to_visit) > 0:
            city_to_visit: City = self._get_next_city_to_visit()
            self._visit_city(city_to_visit)

        print(f'self._computed_distances_count : {self._computed_distances_count}')
        return self._get_path()
    
    def _reset_variables(self, start_city: City, end_city: City):
        self._start_city = start_city
        self._end_city = end_city
        self._cities_infos_dict = self._init_cities_infos_dict()
        self._cities_to_visit = [start_city]
        self._visited_cities = []
        self._computed_distances_count = 0

    def _init_cities_infos_dict(self) -> CitiesInfosDict:
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
        next_city_to_visit: City
        next_city_distance_to_origin: float = float("inf")

        for city in self._cities_to_visit:
            if self._cities_infos_dict[city]["distance_to_origin"] < next_city_distance_to_origin:
                next_city_to_visit = city
                next_city_distance_to_origin = self._cities_infos_dict[city]["distance_to_origin"]

        return next_city_to_visit
    
    def _visit_city(self, city: City):

        for connected_city in self._graph[city]:

            if connected_city in self._visited_cities:
                continue

            if connected_city not in self._cities_to_visit and (self._cities_infos_dict[connected_city]["distance_to_origin"] <= self._cities_infos_dict[self._end_city]["distance_to_origin"]):
            # if connected_city not in self._cities_to_visit:
                self._cities_to_visit.append(connected_city)
            
            new_distance: float = self._cities_infos_dict[city]["distance_to_origin"] + self._graph[city].get(connected_city)
            old_distance: float = self._cities_infos_dict[connected_city]["distance_to_origin"]

            if new_distance < old_distance:
                self._cities_infos_dict[connected_city]["closest_city"] = city
                self._cities_infos_dict[connected_city]["distance_to_origin"] = new_distance
                self._computed_distances_count += 1
        
        self._cities_to_visit.remove(city)
        self._visited_cities.append(city)

    def _get_path(self) -> Path:
        path: Path = {
            "total": self._cities_infos_dict[self._end_city]["distance_to_origin"],
            "steps": [self._end_city]
        }
        next_step: City = self._end_city

        while not next_step == self._start_city:
            path["steps"].insert(0, self._cities_infos_dict[next_step]["closest_city"])
            next_step = self._cities_infos_dict[next_step]["closest_city"]

        return path

