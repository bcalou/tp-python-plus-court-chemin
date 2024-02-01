from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.graphs import Graph


class Pathfinder:

    def __init__(self, graph: Graph) -> None:

        self.__path: Path = {
            "total": 0,
            "steps": []
        }

        self.__inner_graph: Graph = graph

        self.__travelled_cities: list[City] = []

    def get_shortest_path(self, start: City, end: City) -> Path:

        self.__travelled_cities = [start]

        self.__path["steps"].append(start)

        last_step: City = start

        while last_step != end:

            self.__find_nearest_city(last_step)
            last_step = self.__path["steps"][len(self.__path["steps"]) - 1]

            self.__travelled_cities.append(last_step)

        return self.__path

    def __find_nearest_city(self, start_city: City) -> None:

        node: list[dict[City, float]] = self.__inner_graph[start_city]
        new_step: City = list(node.keys())[0]
        distance: int = node[new_step]

        for i in node:
            new_distance: int = node[i]

            if not self.__has_been_travelled(i):

                if (self.__has_been_travelled(new_step) or
                        not self.__has_been_travelled(new_step) and
                        new_distance < distance):

                    distance = new_distance
                    new_step = i

        self.__path["total"] += distance
        self.__path["steps"].append(new_step)

    def __has_been_travelled(self, city: City):

        for i in self.__travelled_cities:
            if i == city:
                return True

        return False
