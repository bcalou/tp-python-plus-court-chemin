from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import CitiesData, Path, DataToCity


class Pathfinder:
    graph: Graph
    unchecked_cities: CitiesData
    checked_cities: CitiesData
    end: City
    start: City

    def __init__(self, graph: Graph):
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path | None:
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

    def calculate_shortest_path(self) -> Path | None:
        current_city: City = self.start
        while current_city != self.end:
            self.execute_checks(current_city)
            current_city = self.get_next_city()

        self.checked_cities.update(
            {current_city: self.unchecked_cities[current_city]}
        )
        return self.compute_path(current_city)

    def execute_checks(self, city: City) -> None:
        self.check_city(city)
        self.checked_cities.update({city: self.unchecked_cities[city]})
        del self.unchecked_cities[city]

    def compute_path(self, last_city: City) -> Path | None:
        if last_city is not None:
            path: Path = {
                "total": self.checked_cities[last_city]["distance"],
                "steps": self.get_path_from_city(last_city)
            }
            return path
        return None

    def get_next_city(self) -> City:
        return self.get_nearest_unchecked_city()

    def get_nearest_unchecked_city(self) -> City:
        return min(self.unchecked_cities, key=self.get_cost)

    def get_cost(self, city: City) -> float:
        return self.get_path_distance(city)

    def get_path_distance(self, city: City) -> float:
        return self.unchecked_cities[city]["distance"]

    def get_path_from_city(self, city: City) -> list[City]:
        path: list[City] = [city]
        while self.checked_cities[city]["previous_city"] != city:
            city = self.checked_cities[city]['previous_city']
            path.append(city)
        path.reverse()
        return path

    def check_city(self, city: City) -> None:
        path_current_total: float = self.get_path_distance(city)
        for next_city, cost_to_next_city in self.graph[city].items():
            total_cost_to_city: float = path_current_total + cost_to_next_city
            if not self.can_be_added_to_queue(
                city, next_city, total_cost_to_city
            ):
                continue
            self.unchecked_cities.update({
                next_city: {
                    'distance': total_cost_to_city,
                    "previous_city": city
                }
            })

    def can_be_added_to_queue(
        self, current_city: City, next_city: City, cost: float
    ) -> bool:
        if (
            next_city in self.checked_cities or
            self.unchecked_cities[current_city]["previous_city"] == next_city
        ):
            return False
        if (
            next_city in self.unchecked_cities and
            self.unchecked_cities[next_city]['distance'] < cost
        ):
            return False
        return True
