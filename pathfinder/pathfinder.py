
from pathfinder.types import Path
from pathfinder.city import City
from pathfinder.graphs import Graph


class Pathfinder:

    def __init__(self, graph: Graph):
        """We initiate all tab and counter """
        self.__graph: Graph = graph
        self.__tab_number_city_to_do: list[float] = []
        self.__tab_name_city_to_do: list[City] = []
        self.__tab_all_city: dict[City, dict] = {}
        self.__counter = 0

    def get_shortest_path(self, start: City, end: City) -> Path:
        """We decide a start and an end of the Path and
        it will find the shortest path"""

        # We set all tab we use in this method
        # We create a city and a length we can modify to add at these tabs
        self.set_all_tab({start: {"Previous_city": None, "Length": 0}}, [], [])
        Town: City = start
        total: float = 0

        # We search the end
        Town = self.search_end(Town, total, end)

        # We use the end to make reverse path
        return self.reverse_path_from_end(Town)

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

    def get_index_minimum(self, tab: list[float]):
        """We take minimum of list"""
        return tab.index(min(tab))

    def get_length(self, town, neighbor):
        """We return the length between City in graph"""
        return self.get_graph()[town][neighbor]

    def reverse_path_from_end(self, town: City):
        """When we find end City we make all reverse way
        for find shortest path"""
        total: float = self.get_all_city()[town]["Length"]
        steps: list[City] = []
        # until we return to start we add City on "steps"
        while town is not None:
            steps.insert(0, town)
            town = self.get_all_city()[town]["Previous_city"]
        return Path(total=total, steps=steps)

    def remove_city_to_do(self, index: int):
        """When we treat a city we remove it from the tab"""
        neighbor = self.get_all_name()[index]
        self.set_all_number(self.get_all_number().pop(index))
        self.set_all_name(self.get_all_name().pop(index))
        return neighbor

    def add_city_to_do(self, neighbors: City, length: float, town: City):
        """We add the name of a city and the length in tab
        until we treat them later"""
        self.set_all_number(self.get_all_number().append(length))
        self.set_all_name(self.get_all_name().append(neighbors))
        return {"Previous_city": town, "Length": length}

    def set_all_tab(self, all_city: dict[City, dict], all_name: list[City],
                    all_number: list[float]):
        """We set all tab we need for find shortest path"""
        self.set_all_city(all_city)
        self.set_all_name(all_name)
        self.set_all_number(all_number)

    def set_all_city(self, all_city, neighbors=None):
        """set all city on the graph"""
        if neighbors is None:
            self.__tab_all_city: dict[City, dict] = all_city
        else:
            self.__tab_all_city[neighbors] = all_city

    def get_all_city(self):
        """get all city on the graph"""
        return self.__tab_all_city

    def set_all_name(self, name):
        """set all name of city on the graph we haven't treat yet"""
        self.tab_name_city_to_do = name

    def get_all_name(self):
        """get all name of city on the graph we haven't treat yet"""
        return self.__tab_name_city_to_do

    def set_all_number(self, number):
        """set all length between this city and the start
        on the graph we haven't treat yet"""
        self.tab_number_city_to_do = number

    def get_all_number(self):
        """get all length between this city and the start
        on the graph we haven't treat yet"""
        return self.__tab_number_city_to_do

    def set_graph(self, new_graph: Graph):
        self.__graph: Graph = new_graph

    def get_graph(self) -> Graph:
        return self.__graph

    def set_counter(self, number: int):
        self.__counter = number

    def get_counter(self) -> int:
        return self.__counter
