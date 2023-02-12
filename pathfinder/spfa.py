from pathfinder.pathfinder import PathFinder
from pathfinder.graphs import GraphType
from pathfinder.city import City
from pathfinder.types import Path


class SPFA(PathFinder):
    def __init__(self, graph: GraphType):
        PathFinder.__init__(self, graph)

    def check_cities_to_visit(self, city: City, list_found_city: list[City], list_visited_city: list[City], end: City):
        for city_to_visit in self._graph[city]:
            if city_to_visit not in list_found_city and \
                city_to_visit not in list_visited_city:

                list_found_city.append(city_to_visit)

            distance_from_start = self.list_city_distant[city]["distance"]\
                + self._graph[city][city_to_visit]
            if distance_from_start < self.list_city_distant[city_to_visit]["distance"]:
                
                self.list_city_distant[city_to_visit]["distance"] = distance_from_start
                self.list_city_distant[city_to_visit]["from"] = city
                list_found_city.append(city_to_visit)