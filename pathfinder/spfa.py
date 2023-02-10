from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder
from pathfinder.types import Path


class SPFA(PathFinder):
    def __init__(self, graph: Graph):
        super().__init__(graph)

    def get_next_city(self) -> City:
        """Returns first in queue"""

        return list(self.unchecked_cities.keys())[0]

    def calculate_shortest_path(self) -> Path|None :
        """Calculate the path"""

        city_to_check: City = self.start
        while bool(self.unchecked_cities):  # or city_to_check is not None:
            self.execute_checks(city_to_check)
            if bool(self.unchecked_cities):
                city_to_check = self.get_next_city()

        return self.compute_path(self.end)

    def can_be_added_to_queue(self, current_city: City, next_city: City, cost: float) -> bool:
        # check if current next city is not in checked city,
        # or is not the previous city
        if self.unchecked_cities[current_city]["previous_city"] == next_city:
            return False

        #Check if city is already seen and maybe have a better path to it
        if next_city in self.checked_cities and self.checked_cities[next_city]['distance'] > cost:
            del (self.checked_cities[next_city])
            return True
        elif next_city in self.checked_cities:
            return False

        # check if current next city is already known
        # and new distance is inferior to current distance
        if next_city in self.unchecked_cities \
                and self.unchecked_cities[next_city]['distance'] < cost:
            return False

        return True


