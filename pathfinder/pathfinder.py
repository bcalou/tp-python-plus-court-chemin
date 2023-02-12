from pathfinder.graphs import GraphType
from pathfinder.city import City
from pathfinder.types import Path

class PathFinder():
    def __init__(self, graph: GraphType):
        self._graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        list_found_city: list[City] = [start]
        self.list_city_distant = {}
        list_visited_city = []
        current_city = end
        final_path: Path = {
            "total": 0,
            "steps": []
        }
        
        self.get_all_city_attributs(start)

        while len(list_found_city) > 0:

                city = self.get_closest_city(list_found_city)
                
                self.check_cities_to_visit(city, list_found_city, list_visited_city, end)

                list_visited_city.append(city)
                list_found_city.remove(city)

        
        final_path["total"] = self.list_city_distant[end]["distance"]
        while current_city != start:

            final_path["steps"].insert(0, current_city)
            current_city = self.list_city_distant[current_city]["from"]

        final_path["steps"].insert(0, start)
        return final_path
            
    def get_distance(self, city: City):
        return self.list_city_distant[city]["distance"]


    def get_closest_city(self, list_city: list[City]):
            return (min(list_city, key = self.get_distance))

    def get_all_city_attributs(self, start: City):
        for city in self._graph:

            city_attribut = {
                "distance" : 0 if city == start else float("inf")
            }
            self.list_city_distant[city] = city_attribut


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
