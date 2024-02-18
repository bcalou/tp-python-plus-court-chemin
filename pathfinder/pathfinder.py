from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.graphs import Graph
from pathfinder.node import Node


class Pathfinder:

    def __init__(self, graph: Graph) -> None:

        self._path: Path = {
            "total": 0,
            "steps": []
        }

        self._inner_graph: Graph = graph

        self._nodes: list[Node] = []

        for i in graph.keys():
            self._nodes.append(Node(i))

        self._travelled_cities: list[City] = []
        self._cities_to_travel: list[City] = []

    def _get_node(self, city: City) -> Node:
        """
            Return the desired node from the graph based on the city
        """

        for i in self._nodes:
            if i.get_city() == city:
                return i

    def _reset(self) -> None:
        """
            Reset the instance parameters to compute a new path
        """

        self._path = {
            "total": 0,
            "steps": []
        }

        self._travelled_cities = []
        self._cities_to_travel = []

        for node in self._nodes:
            node.set_distance(float("inf"))
            node.set_previous_city(node.get_city())

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Calculate the shortest path from start to the end based on the
            graph of the instance.
        """

        self._reset()

        self._cities_to_travel.append(start)

        self._get_node(start).set_distance(0)

        i = 0

        while i < len(self._cities_to_travel):

            city_to_travel: City = self._cities_to_travel[i]

            self._travel_city(city_to_travel)
            self._travelled_cities.append(city_to_travel)
            i += 1

        return self._reconstitute_path(start, end)

    def _travel_city(self, city_to_travel: City) -> None:
        """
            Check each vertex of the city given and update his neighbours
        """

        nodes_to_sort: list[Node] = []
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

            nodes_to_sort.append(neighbour_node)

        # Update array of next nodes to compute
        self.__update_cities_to_travel(nodes_to_sort)

    def __update_cities_to_travel(self, neighbours: list[Node]) -> None:
        """
            Sort neighbours based on distance and schedule the cities
            to travel next if not already planned
        """
        
        sorted_neighbours: list[Node] = self.__sort(neighbours)

        for neighbour in sorted_neighbours:

            neighbour_city: City = neighbour.get_city()

            if neighbour_city not in self.__travelled_cities:
                self.__cities_to_travel.append(neighbour_city)

    def __sort(self, nodes: list[Node]) -> list[Node]:
        """
            Used in travel_city() to tell the entire programm
            wich city to check next (fusion sort)
        """

        if len(nodes) <= 1:
            return nodes
        else:
            half = len(nodes) // 2
            return self.__merge(self.__sort(nodes[:half]),
                                self.__sort(nodes[half:]))

    def __merge(self, array: list[Node], array_2: list[Node]) -> list[Node]:
        """
            Used for fusion sort
        """

        sorted_array = []

        array_index = 0
        array_2_index = 0

        while len(sorted_array) != len(array) + len(array_2):

            # Avoid list out of range
            if array_index >= len(array):

                sorted_array.append(array_2[array_2_index])
                array_2_index += 1

            elif array_2_index >= len(array_2):

                sorted_array.append(array[array_index])
                array_index += 1

            # or check wich value is the smallest

            elif (array_2[array_2_index].get_distance() <
                  array[array_index].get_distance()):

                sorted_array.append(array_2[array_2_index])
                array_2_index += 1

            else:
                sorted_array.append(array[array_index])
                array_index += 1

        return sorted_array

    def _reconstitute_path(self, start: City, end: City) -> Path:
        """
            Create an array of steps of the shortest path to take
        """

        step: City = end
        steps: list[City] = []

        while step != start:
            steps.append(step)
            step = self._get_node(step).get_previous_city()

        steps.append(start)
        steps.reverse()

        self._path["steps"] = steps

        self._path["total"] = self._get_node(end).get_distance()

        return self._path
