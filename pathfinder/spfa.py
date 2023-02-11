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

    def calculate_shortest_path(self) -> Path | None:
        """Calculate the path, we must go through each city to get total path"""

        city_to_check: City = self.start
        while bool(self.unchecked_cities):
            self.execute_checks(city_to_check)
            if bool(self.unchecked_cities):
                city_to_check = self.get_next_city()

        return self.compute_path(self.end)

    def can_be_added_to_queue(self, current_city: City, next_city: City, cost: float) -> bool:
        """Do the checks of the algorithm to see if the city can be added to the pile"""

        # Check if city is already seen and have a better path to it
        if next_city in self.checked_cities and self.checked_cities[next_city]['distance'] > cost:
            del (self.checked_cities[next_city])
            return True
        elif next_city in self.checked_cities:
            return False

        return super().can_be_added_to_queue(current_city, next_city, cost)
