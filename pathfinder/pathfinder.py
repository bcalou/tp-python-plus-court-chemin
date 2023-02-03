from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import CitiesData, Path, DataToCity


class PathFinder:
    graph: Graph
    unchecked_cities: CitiesData
    checked_cities: CitiesData

    def __init__(self, graph: Graph):
        self.graph = graph
        self.unchecked_cities = {}
        self.checked_cities = {}
        print("Class PathFinder Initialised")

    def get_shortest_path(self, start: City, end: City) -> Path|None:
        city_to_check: City = start
        self.unchecked_cities.update({
            start: {
                "previous_city": start,
                "distance": 0
            }
        })
        while city_to_check != end: # or city_to_check is not None:
            self.check_city(city_to_check)
            self.checked_cities.update({city_to_check: self.unchecked_cities[city_to_check]})
            del self.unchecked_cities[city_to_check]
            city_to_check = self.get_nearest_unchecked_city()

        if city_to_check is not None :
            self.checked_cities.update({city_to_check: self.unchecked_cities[city_to_check]})

            path: Path = {
                "total": self.checked_cities[city_to_check]["distance"],
                "steps": self.get_path_from_city(city_to_check)
            }
            return path

        return None

    def get_nearest_unchecked_city(self) -> City|None:
        """Returns the city with minimum distance"""
        # if len(self.unchecked_cities) == 0:
        #     return None
        return min(self.unchecked_cities, key=self.get_total_from_path)

    def get_total_from_path(self, city: City) -> float:
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
        """Checks if city got a path to any new city,
        or if it's quicker to get to a already known city """

        path_current_total: float = self.get_total_from_path(city)
        for next_city, cost_to_next_city in self.graph[city].items():
            total_cost_to_city: float = path_current_total + cost_to_next_city

            # check if city is not in checked city, or is not the previous city
            if next_city in self.checked_cities or \
                    self.unchecked_cities[city]["previous_city"] == next_city:
                continue

            # check if city is already known
            # and compare current distance to possible distance
            if next_city in self.unchecked_cities \
                    and self.unchecked_cities[next_city]['distance'] < total_cost_to_city:
                continue

            # adds or update the city in the unchecked list
            self.unchecked_cities.update({
                next_city: {
                    'distance': total_cost_to_city,
                    "previous_city": city
                }
            })
