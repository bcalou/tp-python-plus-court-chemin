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

    def early_break(self, current_city: City, end: City) -> bool:
        # La version de Dijkstra est toujours vrai pour A*
        if super().early_break(current_city, end):
            return True

        # Mais on peut aller un peu plus loin, si la ville actuelle voit
        # la ville d'arrivé, alors on peut directement ignorer tout les
        # autres chemins
        neighbours: list[City] = list(self.graph.get(current_city).keys())
        if end in neighbours:
            self.previous_cities[end] = current_city
            return True

        return False

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
