from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path
from pathfinder.node import Node

class SPFA(Pathfinder):

    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)

    def get_shortest_path(self, start: City, end: City) -> Path:

        self._reset()

        self._cities_to_travel.append(start)

        self._get_node(start).set_distance(0)

        i = 0

        while i < len(self._cities_to_travel):

            city_to_travel: City = self._cities_to_travel[i]

            self._travel_city(city_to_travel)
            i += 1

        return self._reconstitute_path(start, end)
    
    def _travel_city(self, city_to_travel: City) -> None:

        city_distance: int = self._get_node(city_to_travel).get_distance()

        # for each city neighbours from the city to travel
        for neighbour in self._inner_graph[city_to_travel].keys():

            neighbour_node: Node = self._get_node(neighbour)
            vertex_dist: int = self._inner_graph[city_to_travel][neighbour]

            new_distance: int = city_distance + vertex_dist

            # Replace distance if it's smaller than the stored one
            if neighbour_node.get_distance() > new_distance:
                neighbour_node.set_distance(new_distance)
                neighbour_node.set_previous_city(city_to_travel)
                self._cities_to_travel.append(neighbour)