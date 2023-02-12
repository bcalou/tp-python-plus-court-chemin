from pathfinder.pathfinder import PathFinder
from pathfinder.heuristics import HeuristicsType
from pathfinder.graphs import GraphType
from pathfinder.city import City


class AStar(PathFinder):
    def __init__(self, graph: GraphType, heuristics: HeuristicsType):
        PathFinder.__init__(self, graph)
        self._heuristics = heuristics

    def get_closest_city(self, list_city: list[City]):
        # Je prend en compte l'élément heuristic en plus de l'élément distance
        return (min(list_city, key=lambda x: self.get_heuristic(x) + self.get_distance(x)))

    def get_all_city_attributs(self, start: City):
        # Je rajoute l'élément heuristic dans le dictionnaire
        for city in self._graph:

            city_attribut = {
                "distance": 0 if city == start else float("inf"),
                "heuristic": self._heuristics[city]
            }
            self.list_city_distant[city] = city_attribut

    def get_heuristic(self, city: City):
        return self.list_city_distant[city]["heuristic"]

    def check_cities_to_visit(self, city: City, list_found_city: list[City],\
        list_visited_city: list[City], end: City):
        # Je modifie la fonction pour arreter la boucle si je trouve
        # la ville de d'arrivé
        super().check_cities_to_visit(city, list_found_city, list_visited_city, end)
        if end in list_found_city:
            list_found_city.clear()
            list_found_city.append(city)
