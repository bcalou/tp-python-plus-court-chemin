"""
Pathfinder class
"""

from pathfinder.city import City
from pathfinder.types import Cities, Graph, Path


class Pathfinder:
    """Dijkstra pathfinder"""

    def __init__(self, graph: Graph):
        self._graph = graph
        self._start: City
        self._end: City
        self._cities: Cities
        self._cities_to_visit: list[City]

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Get the shortest path between 2 cities"""
        self._start: City = start
        self._end: City = end

        self._cities: Cities = self._get_initial_cities()

        # At the start, we can only visit the city from which we start
        self._cities_to_visit: list[City] = [start]

        self._explore_paths()

        return self._get_formatted_path()

    def _get_initial_cities(self) -> Cities:
        """Get an object retaining cities info as we go along"""
        cities: Cities = {}

        # The start city has a distance of zero (we're already there)
        cities[self._start] = {
            "distance_from_start": 0
        }

        # The end city distance if infinite (we don't know the path yet)
        cities[self._end] = {
            "distance_from_start": float("inf")
        }

        return cities

    def _explore_paths(self):
        """Explore the paths connected to the cities to visit"""
        while not self._is_finished():
            # Visit the closest city available
            next_city_to_visit: City = self._get_next_city_to_visit()

            self._visit_city(next_city_to_visit)

            # Remove the city from the visit list
            self._cities_to_visit.remove(next_city_to_visit)

    def _is_finished(self) -> bool:
        """Return True if the algorithm has finished it's job"""

        # When the next city to visit is the end city, it means there is
        # no way to improve the end city score, so stop
        return self._get_next_city_to_visit() == self._end

    def _get_next_city_to_visit(self) -> City:
        """Get the closest city, which is the most interesting to visit"""
        return min(
            self._cities_to_visit,
            key=self._get_city_distance_evaluation
        )

    def _get_city_distance_evaluation(self, city: City) -> float:
        """Get the city distance"""

        return self._cities[city]["distance_from_start"]

    def _visit_city(self, city: City) -> None:
        """Try the routes connected to this city"""
        print("___\nNow visiting:", city.name)

        # Try each city connected to the current one and unvisited
        for connected_city in self._graph[city]:

            # Create a new city info if we don't know about it yet
            if connected_city not in self._cities:
                self._cities[connected_city] = {
                    "distance_from_start": float("inf")
                }

            self._test_route(city, connected_city)

    def _test_route(self, current_city: City, connected_city: City) -> None:
        """Test the route between two cities"""

        # The distance to the connected city is the distance of the current
        # city + the cost for this connection
        distance: float = (
            self._cities[current_city]["distance_from_start"]
            + self._graph[current_city][connected_city]
        )

        # If the distance is better than the current distance for this city
        if distance < self._cities[connected_city]["distance_from_start"]:
            self._save_path(current_city, connected_city, distance)

    def _save_path(self, from_city: City, to_city: City, distance: float):
        """Save a new interesting path"""
        print("New path to", to_city, "found")
        print(distance, "coming_from", from_city)
        self._cities[to_city]["distance_from_start"] = distance

        # Remember where we come from
        self._cities[to_city]["coming_from"] = from_city

        # Add connected city to the list of cities to visit
        if to_city not in self._cities_to_visit:
            print("Add city to visit:", to_city.name)
            self._cities_to_visit.append(to_city)

    def _get_formatted_path(self) -> Path:
        """Convert the cities object to a formatted path answer"""

        path: Path = {
            "total": self._cities[self._end]["distance_from_start"],
            "steps": [self._end]  # We only know the last step at the moment
        }

        previous_step = self._cities[self._end]

        # While we come from somewhere...
        while "coming_from" in previous_step:

            # Insert where we come from at the beginning of the steps array
            path["steps"].insert(0, previous_step['coming_from'])

            # Rewind the steps
            previous_step = self._cities[previous_step["coming_from"]]

        return path
