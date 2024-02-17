from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City


class AStar (Pathfinder):
    """
    La classe AStar implémente l'algorithme du même nom
    (https://fr.wikipedia.org/wiki/Algorithme_A*)
    """

    # Stocke les valeurs d'heuristics de chaque villes
    heuristics: dict[City, float]

    def __init__(
        self,
        graph: dict[City, dict[City, float]],
        heuristic: dict[City, float]
         ) -> None:
        super().__init__(graph)
        self.heuristics = heuristic

    def find_distance_to_city(self, city: City, previous: City) -> float:
        """
        Permet de connaître la distance d'une ville par rapport au départ
        du chemin.

        `city` est la ville qui va être ajouté.

        `previous` est la ville par laquelle on est arrivé à `city`
        """
        distance_to_previous: float = self.distance_to_cities[previous]
        distance: float = distance_to_previous + self.graph[previous][city]
        distance += self.heuristics[city]
        return distance
