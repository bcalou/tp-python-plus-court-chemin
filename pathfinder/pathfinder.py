from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import CitiesData, Path, DataToCity


class PathFinder:
    graph: Graph
    unchecked_cities: CitiesData
    checked_cities: CitiesData
    end: City
    start: City


    def __init__(self, graph: Graph):
        self.graph = graph
        print("Class PathFinder Initialised")

    def get_shortest_path(self, start: City, end: City) -> Path|None:
        self.start = start
        self.end = end
        self.checked_cities = {}
        self.unchecked_cities = {
            start: {
                "previous_city": start,
                "distance": 0
            }
        }
        return self.calculate_shortest_path()


    def calculate_shortest_path(self) -> Path|None :
        """Calculate the path"""

        city_to_check: City = self.start
        while city_to_check != self.end:  # or city_to_check is not None:
            self.execute_checks(city_to_check)
            city_to_check = self.get_next_city()

        self.checked_cities.update({city_to_check: self.unchecked_cities[city_to_check]})
        return self.compute_path(city_to_check)


    def execute_checks(self, city_to_check: City) -> City:
        self.check_city(city_to_check)
        self.checked_cities.update({city_to_check: self.unchecked_cities[city_to_check]})
        del self.unchecked_cities[city_to_check]

    def compute_path(self, last_city: City) -> Path|None:
        """Compute path from given city"""

        if last_city is not None:
            path: Path = {
                "total": self.checked_cities[last_city]["distance"],
                "steps": self.get_path_from_city(last_city)
            }
            return path
        return None

    def get_next_city(self) -> City:
        """Returns next city"""

        return self.get_nearest_unchecked_city()
    def get_nearest_unchecked_city(self) -> City:
        """Returns the city with minimum distance"""

        return min(self.unchecked_cities, key=self.get_cost)

    def get_cost(self, city: City) -> float:
        return self.get_path_distance(city)

    def get_path_distance(self, city: City) -> float:
        """Return distance to get to a city"""

        return self.unchecked_cities[city]["distance"]

    def get_path_from_city(self, city: City) -> list[City]:
        """Get the path to a given city, from the start city"""

        path: list[City] = [city]
        while self.checked_cities[city]["previous_city"] != city:
            city = self.checked_cities[city]['previous_city']
            path.append(city)
        path.reverse()
        return path

    def check_city(self, city: City) -> None:
        """Checks if selected city got a path to any new city,
        or if it's quicker to get to a already known city """

        path_current_total: float = self.get_path_distance(city)
        for next_city, cost_to_next_city in self.graph[city].items():

            total_cost_to_city: float = path_current_total + cost_to_next_city

            if not self.can_be_added_to_queue(city, next_city, total_cost_to_city):
               continue

            # adds or update the city in the unchecked list
            self.unchecked_cities.update({
                next_city: {
                    'distance': total_cost_to_city,
                    "previous_city": city
                }
            })

    def can_be_added_to_queue(self, current_city: City ,next_city: City, cost: float) -> bool:
        # check if current next city is not in checked city,
        # or is not the previous city
        if next_city in self.checked_cities or \
                self.unchecked_cities[current_city]["previous_city"] == next_city:
            return False

        # check if current next city is already known
        # and new distance is inferior to current distance
        if next_city in self.unchecked_cities \
                and self.unchecked_cities[next_city]['distance'] < cost:
            return False

        return True