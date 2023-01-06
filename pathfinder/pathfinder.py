import math
from pathfinder.graphs import Graph
from pathfinder.types import Path, Ville
from pathfinder.city import City

# Il s'agit d'une implémentation de l'algorithme de Dijkstra
class PathFinder:
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.villes: dict[City, Ville] = {}
        self.min_to_end: float = math.inf

    def get_shortest_path(self, start: City, end: City) -> Path:

        self.analyse_next_city(start, end)
        return self.get_path(start, end)

    def analyse_next_city(self, city: City, end: City, current_sum: float = 0) -> None:
        for neighbour in self.graph[city]:
            
            if current_sum > self.min_to_end:
                return
            
            total_cost = current_sum + self.graph[city][neighbour]

            if (
                neighbour not in self.villes or
                self.villes[neighbour]["cout"] > total_cost
            ):
                self.villes[neighbour] = {"previous": city, "cout": total_cost}

            if neighbour == end:
                if total_cost < self.min_to_end:
                    self.min_to_end = total_cost
                return
            
            self.analyse_next_city(neighbour, end, total_cost)

    def get_path(self, start: City, end: City) -> Path:
        to_ret: Path = {"total": 0, "steps": []}
        current_city: City = end
        while current_city != start and self.villes[current_city]["previous"]:
            to_ret["steps"].insert(0, current_city)
            current_city = self.villes[current_city]["previous"] # type: ignore
            # (le linter ne voit pas la condition du while...)
        to_ret["steps"].insert(0, start)
        return to_ret
