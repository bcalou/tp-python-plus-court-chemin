from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.heuristics import Heuristics
from pathfinder.pathfinder import Pathfinder
from pathfinder.node import Node
from pathfinder.types import Path


class AStar(Pathfinder):

    def __init__(self, graph: Graph, heuristics: Heuristics) -> None:

        super().__init__(graph)
        self.__inner_heuristics: Heuristics = heuristics

    def get_shortest_path(self, start: City, end: City) -> Path:
        super().__reset()

        self.__cities_to_travel.append(start)

        super().__get_node(start).set_distance(0)

        i = 0

        while i < len(self.__cities_to_travel):

            city_to_travel: City = self.__cities_to_travel[i]

            self.__travel_city(city_to_travel)
            self.__travelled_cities.append(city_to_travel)
            i += 1

        return self.__reconstitute_path(start, end)

    def __travel_city(self, city_to_travel: City) -> None:

        closest_node: Node = self.__get_node(city_to_travel)
        city_distance: int = closest_node.get_distance()

        closest_distance: int = 0
        real_distance: int = 0

        print("ah")

        # for each city neighbours from the city to travel
        for neighbour in self.__inner_graph[city_to_travel].keys():

            vertex_dist: int = self.__inner_graph[city_to_travel][neighbour]
            heuristic_dist: int = self.__inner_heuristics[neighbour]

            # calculate distance based on heuristics
            new_distance: int = vertex_dist + heuristic_dist

            # and update closest city (and his real distance)
            if closest_distance == 0 or closest_distance > new_distance:

                closest_node = self.__get_node(neighbour)
                closest_distance = new_distance
                real_distance = city_distance + vertex_dist

        # update node properties
        closest_node.set_distance(real_distance)
        closest_node.set_previous_node(self.__get_node(city_to_travel))
        self.__cities_to_travel.append(closest_node.get_city())
