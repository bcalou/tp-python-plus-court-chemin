from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path


class AStar(Pathfinder):

    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        """We define also heuristics in this class"""
        self.__heuristics: dict[City, float] = heuristics
        super().__init__(graph)

    def search_end(self, Town: City, total: float, end: City):
        """We search end and the distance she has from start"""

        # We look all city near to the start until the end we define
        while Town != end:
            # We get the length to go at this city from the start
            total = self.get_all_city()[Town]["Length"]

            # We increment counter for each City we visit
            self.set_counter(self.get_counter()+1)

            # for each neighbors of the city
            for neighbors in self.get_graph()[Town]:
                # We begun by ask if we known this city
                # and we add it for later if its isn't
                if (neighbors not in self.get_all_city()):
                    self.set_all_city(self.add_city_to_do(
                        neighbors, self.get_length(Town, neighbors)+total,
                        Town), neighbors)

                    # little difference when we find end we stop the search
                    if (neighbors == end):
                        Town = neighbors
                        break

                # if we already know this city we check if the length
                # by this "town" is under the length we save
                else:

                    # if it is under we remove the ancien length
                    # and replace by the new length
                    if (self.get_all_city()[neighbors]["Length"] >
                            self.get_graph()[Town][neighbors]+total
                            and neighbors in self.get_all_name()):
                        self.remove_city_to_do(
                            self.get_all_name().index(neighbors))
                        self.set_all_city(self.add_city_to_do(
                            neighbors, self.get_length(Town, neighbors)+total,
                            Town), neighbors)
            # After Check all neighbor of a City we find the minimum length
            # of all City not look
            Town = self.remove_city_to_do(
                self.get_index_minimum(self.get_all_number()))

        # We increment counter for end City we visit
        self.set_counter(self.get_counter()+1)
        return Town

    def get_length(self, town, neighbor):
        """We return the length between City in graph with heuristics"""
        return super().get_length(town, neighbor)*self.get_heuristics(neighbor)

    def reverse_path_from_end(self, town: City):
        """When we find end City we make all reverse way
        for find shortest path"""
        total: float = 0
        steps: list[City] = []
        # until we return to start we add City on "steps" and we add the length
        while town is not None:
            steps.insert(0, town)
            if self.get_all_city()[town]["Previous_city"] is not None:
                total += super().get_length(
                    town, self.get_all_city()[town]["Previous_city"])
            town = self.get_all_city()[town]["Previous_city"]
        return Path(total=total, steps=steps)

    def get_heuristics(self, town: City):
        return self.__heuristics[town]
