from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder
from pathfinder.types import Path


class SPFA(PathFinder):

    def __init__(self, graph: Graph):
        PathFinder.__init__(self, graph)
        self.is_city_in_list: dict[City, bool] = {}

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Returns the shortest path to the end city"""

        self._init_cities_dict(start)

        # List of our cities to visit
        current_cities: list[City] = [start]

        self._init_verification_dict(start)

        while len(current_cities) > 0:

            # Visit the first city of the list
            city_to_visit = current_cities.pop(0)
            self.is_city_in_list[city_to_visit] = False

            # Check every neighbour of the visited city
            for neighbour in self._graph[city_to_visit]:

                # The distance for the visited city to the neighbour city
                distance = self._graph[city_to_visit][neighbour]

                if self._cities[neighbour]['distance'] > \
                        self._cities[city_to_visit]['distance'] + distance:

                    self._update_city_infos(neighbour, city_to_visit,
                                            self._cities[city_to_visit][
                                                'distance'] + distance)

                    # Check if the neighbour city is in the list of cities
                    # to visit, if not, add it
                    if not self.is_city_in_list[neighbour]:
                        current_cities.append(neighbour)
                        self.is_city_in_list[neighbour] = True

        return self._get_path(end)

    def _init_verification_dict(self, start_city: City):
        """Initialises the is_city_in_list dict"""
        self.is_city_in_list.clear()

        # Fill the dict using the graph and set every city to false
        for city in self._graph.keys():
            self.is_city_in_list[city] = False

        # The starting city is the only city in our list for now
        self.is_city_in_list[start_city] = True
