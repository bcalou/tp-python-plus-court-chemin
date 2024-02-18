from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path


class SPFA(Pathfinder):

    def search_end(self, Town: City, total: float, end: City):
        """We search end and the distance she has from start"""

        # While change now we check all path because
        # it is always possible to find a short length
        while self.get_all_number() != [] or end not in self.get_all_city():
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

                # if we already know this city we check if the length
                # by this "town" is under the length we save
                else:

                    # if it is under we remove the ancien length
                    # and replace by the new length
                    # A city can now return into the to_do tab
                    if (self.get_all_city()[neighbors]["Length"] >
                            self.get_graph()[Town][neighbors]+total):

                        # We add this condition because it is possible
                        # that a city isn't in tab anymore
                        # and we want to add again this
                        if (neighbors in self.get_all_name()):
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

        # We always return end because Town can be other city
        # and "end" is always treated
        return end
