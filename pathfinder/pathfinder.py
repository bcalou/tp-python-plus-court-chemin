from pathfinder.graphs import *
from pathfinder.types import *


class PathFinder:
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
        self._reset_variables(start_city, end_city)

        while len(self._cities_to_visit) > 0:
            city_to_visit: City = self._get_next_city_to_visit()
            self._visit_city(city_to_visit)

        print(f'self._computed_distances_count : {self._computed_distances_count}')
        self._path = self._get_path()
        return self._path
    
    def _reset_variables(self, start_city: City, end_city: City):
        self._start_city = start_city
        self._end_city = end_city
        self._found_end_city = False
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
        next_city_weight: float = float("inf")

        for city in self._cities_to_visit:

            city_weight: float = self._get_city_weight(city)

            if city_weight < next_city_weight:
                next_city_to_visit = city
                next_city_weight = city_weight

        return next_city_to_visit
    
    def _get_city_weight(self, city: City) -> float:
        return self._cities_infos_dict[city]["distance_to_origin"]
    
    def _visit_city(self, city: City):
        # print(f'visiting {city.name}')

        if city == self._end_city:
            # print(f'{city.name} is the end city')
            self._found_end_city = True

        for connected_city in self._graph[city]:
            # print(f'checking connected city {connected_city.name}')

            if connected_city in self._visited_cities:
                # print(f'{connected_city.name} has already been visited, skipping')
                continue

            connected_city_weight: float = self._get_city_weight(connected_city)
            end_city_weight: float = self._get_city_weight(self._end_city)

            if connected_city not in self._cities_to_visit and (connected_city_weight <= end_city_weight):
                # print(f'will visit {connected_city.name} later')
                self._cities_to_visit.append(connected_city)
            
            new_weight: float = self._get_city_weight(city) + self._graph[city].get(connected_city)
            old_weight: float = connected_city_weight

            if new_weight < old_weight:
                self._cities_infos_dict[connected_city]["closest_city"] = city
                self._cities_infos_dict[connected_city]["distance_to_origin"] = (
                    self._cities_infos_dict[city]["distance_to_origin"] + self._graph[city].get(connected_city)
                )
                # print(f'new lower weight found for {connected_city.name} : {self._cities_infos_dict[connected_city]["distance_to_origin"]}')
                self._computed_distances_count += 1
        
        self._cities_to_visit.remove(city)
        self._visited_cities.append(city)
        # print(f'leaving {city.name}')


    def _get_path(self) -> Path:
        # print('_get_path function')
        path: Path = {
            "total": self._cities_infos_dict[self._end_city]["distance_to_origin"],
            "steps": [self._end_city]
        }
        next_step: City = self._end_city

        while not next_step == self._start_city:
            path["steps"].insert(0, self._cities_infos_dict[next_step]["closest_city"])
            next_step = self._cities_infos_dict[next_step]["closest_city"]

        return path

