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
        self.to_visit: list[City] = []

    def get_shortest_path(self, start: City, end: City) -> Path:

        self.to_visit.append(start)
        self.villes[start] = {"previous": None, "cout": 0}

        self.pathfind(start, end)
        result: Path = self.get_path(start, end)
        self.reset()

        return result

    # def analyse_next_city(self, city: City, end: City, current_sum: float = 0) -> None:
    #     for neighbour in self.graph[city]:
            
    #         if current_sum > self.min_to_end:
    #             return
            
    #         total_cost = current_sum + self.graph[city][neighbour]

    #         if neighbour == end:
    #             if total_cost < self.min_to_end:
    #                 self.min_to_end = total_cost
    #                 self.villes[neighbour] = {"previous": city, "cout": total_cost}
    #             return

    #         if (
    #             neighbour not in self.villes or
    #             self.villes[neighbour]["cout"] > total_cost
    #         ):
    #             self.villes[neighbour] = {"previous": city, "cout": total_cost}
    #             self.analyse_next_city(neighbour, end, total_cost)

    def pathfind(self, city: City, end: City) -> None:
        """Fonction principale de l'algo"""
        while self.to_visit and not self.finished():
            self.sort_visits()
            city = self.to_visit.pop(0)
            
            for neighbour in self.graph[city]:
                total_cost = self.villes[city]["cout"] + self.graph[city][neighbour]

                if total_cost > self.min_to_end:
                    continue

                if neighbour == end:
                    if total_cost < self.min_to_end:
                        self.min_to_end = total_cost
                        self.villes[neighbour] = {"previous": city, "cout": total_cost}
                    continue
                
                if (
                    neighbour not in self.villes or
                    self.villes[neighbour]["cout"] > total_cost
                ):
                    self.villes[neighbour] = {"previous": city, "cout": total_cost}
                    if neighbour not in self.to_visit:
                        self.to_visit.append(neighbour)

    def sort_visits(self) -> None:
        """Algo de tri des villes à visiter, à modifier en fonction de l'algo"""
        self.to_visit.sort(key=lambda city: self.villes[city]["cout"])

    def finished(self) -> bool:
        """Condition de fin de l'algo, à modifier en fonction de l'algo"""
        return len(self.to_visit) == 0

    def get_path(self, start: City, end: City) -> Path:
        """Lis le résultat de l'algo en partant de la fin"""
        to_ret: Path = {"total": 0, "steps": []}
        current_city: City = end
        
        while current_city != start and self.villes[current_city]["previous"]:
            to_ret["steps"].insert(0, current_city)
            current_city = self.villes[current_city]["previous"] # type: ignore
            # (le linter ne voit pas la condition du while...)
        
        to_ret["steps"].insert(0, start)
        to_ret["total"] = self.villes[end]["cout"]

        return to_ret


    def reset(self) -> None:
        self.villes = {}
        self.min_to_end = math.inf