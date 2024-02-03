from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.graphs import Graph
from pathfinder.node import Node


class Pathfinder:

    def __init__(self, graph: Graph) -> None:

        self.__path: Path = {
            "total": 0,
            "steps": []
        }

        self.__inner_graph: Graph = graph

        self.__nodes: list[Node] = []

        for i in graph.keys():
            self.__nodes.append(Node(i.value))

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
