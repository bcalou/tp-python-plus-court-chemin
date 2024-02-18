from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City
from pathfinder.types import Path


class SPFA (Pathfinder):
    """
    La classe AStar implémente l'algorithme du même nom
    (https://fr.wikipedia.org/wiki/Algorithme_A*)
    """

    def explore_city(self, city: City, end: City, history: list[City]) -> list[list[City]] | None:
        results = []

        for destination, _ in self.graph[city].items():
            if destination in history:
                continue

            copy = self.copy_history(history)
            copy.append(city)

            if destination == end:
                copy.append(end)
                results.append(copy)
                continue

            result = self.explore_city(destination, end, copy)

            if result is not None:
                for route in result:
                    results.append(route)

        return results

    def count_cost(self, route: list[City]) -> float:
        sum = 0
        for index, city in enumerate(route):
            if index < len(route) - 1:
                sum += self.graph[city][route[index+1]]
        return sum

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Applique l'algorithme de SPFA

        La fonction considère que la ville d'arrivé est présente et accéssible
        dans le `graph` passé à la création de l'objet Pathfinder.
        """

        results = self.explore_city(start, end, [])
        results = sorted(
            results,
            key=self.count_cost
        )

        return Path(total=self.count_cost(results[0]), steps=results[0])

    def copy_history(self, history: list[City]) -> list[City]:
        if len(history) == 0:
            return []

        return history.copy()
