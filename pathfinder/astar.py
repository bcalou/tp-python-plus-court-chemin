from pathfinder.pathfinder import *


class AStar(PathFinder):
    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        super().__init__(graph)
        self._heuristics = heuristics

    def _get_city_weight(self, city: City) -> float:
        return self._cities_infos_dict[city]["distance_to_origin"] + self._heuristics[city]

    def get_shortest_path(self, start_city: City, end_city: City):
        self._reset_variables(start_city, end_city)

        while self._found_end_city == False:
            city_to_visit: City = self._get_next_city_to_visit()
            self._visit_city(city_to_visit)

        print(f'self._computed_distances_count : {self._computed_distances_count}')
        self._path = self._get_path()
        return self._path
