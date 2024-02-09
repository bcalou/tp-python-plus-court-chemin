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
            self.__nodes.append(Node(i))

        self.__travelled_cities: list[City] = []
        self.__cities_to_travel: list[City] = []

    def __get_node(self, city: City) -> Node:

        for i in self.__nodes:
            if i.get_city() == city:
                return i
            
    def __reset(self) -> None:

        self.__path = {
            "total": 0,
            "steps": []
        }

        self.__travelled_cities = []
        self.__cities_to_travel = []

    def get_shortest_path(self, start: City, end: City) -> Path:

        self.__reset()

        self.__cities_to_travel.append(start)

        self.__get_node(start).set_distance(0)

        i = 0

        while i < len(self.__cities_to_travel):

            self.__travel_city(self.__cities_to_travel[i])
            i += 1

        return self.__reconstitute_path(start, end)

    def __travel_city(self, city_to_travel: City) -> None:

        nodes_to_sort: list[Node] = []
        city_node: Node = self.__get_node(city_to_travel)

        for i in self.__inner_graph[city_to_travel].keys():

            next_city_node = self.__get_node(i)

            new_distance: float = (city_node.get_distance() + 
                                   self.__inner_graph[city_to_travel][i])

            if next_city_node.get_distance() > new_distance:

                next_city_node.set_distance(new_distance)
                next_city_node.set_previous_node(city_to_travel)
                
            nodes_to_sort.append(next_city_node)
        
        sorted_nodes: list[Node] = self.__sort(nodes_to_sort)

        for i in sorted_nodes:
            
            city: City = i.get_city()

            if city not in self.__travelled_cities:
                self.__travelled_cities.append(city)

    
    def __sort(self, nodes: list[Node]) -> list[Node]:

        if len(nodes) <= 1:
            return nodes
        else:
            half = len(nodes) // 2
            return self.__merge(self.__sort(nodes[:half]), 
                                self.__sort(nodes[half:]))

    def __merge(self, array: list[Node], array_2: list[Node]) -> list[Node] :

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
    
    def __reconstitute_path(self, start:City, end: City) -> Path:

        step: City = end

        while step != start:

            self.__path["steps"].append(step)
            step = self.__get_node(step).get_previous_node()

        self.__path["total"] = self.__get_node(end).get_distance()

        return self.__path