from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.type import Path


class AStar(Pathfinder):
    __heuristics: dict[City, float]

    def __init__(self, graph: Graph, heuristics: dict[City, float]) -> None:
        super().__init__(graph)
        self.__heuristics = heuristics

    def find_next_city(self, current_city: City, paths: dict[City, Path],
                       visited_cities: list[City]):
        # Find the next city to visit
        min_distance = float('inf')
        for city, path in paths.items():
            if (city not in visited_cities and
                    min_distance > path["total"] + self.__heuristics[city]):
                min_distance = path["total"] + self.__heuristics[city]
                current_city = city
        return current_city

    def is_loop_ended(self, current_city, end, paths: dict[City, Path]):
        return paths.__contains__(end)