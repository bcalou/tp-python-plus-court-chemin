from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path, CityInfo


class PathFinder:

    def __init__(self, graph: Graph):
        self._graph = graph
        self._cities: dict[City, CityInfo] = {}

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Returns the shortest path to the end city"""

        self._init_cities_dict(start)

        current_cities: list[City] = [start]
        next_cities_to_visit: list[City] = [start]
        visited_cities: list[City] = []

        while len(current_cities) > 0:

            current_cities = next_cities_to_visit.copy()
            next_cities_to_visit.clear()

            for current_city in current_cities:
                neighbour_cities: dict[
                    City, float] = self._get_neighbours_cities_with_distances(
                    current_city)

                # Check the distances of the nearest cities of the city we are
                # visiting
                for neighbour_city, distance in neighbour_cities.items():

                    # The distance to the city is the distance to that
                    # city + the distance to get to the city we are visiting
                    city_distance = distance + self._cities[current_city][
                        'distance']

                    # Update city info only if the distance is smaller
                    if self._cities[neighbour_city]['distance'] > city_distance:
                        self._update_city_infos(neighbour_city, current_city,
                                                city_distance)

                    # Only visit this city if it hasn't been visited before
                    if neighbour_city not in visited_cities:
                        next_cities_to_visit.append(neighbour_city)

            # Add visited cities in the list
            visited_cities.extend(current_cities)

        return self._get_path(end)

    def _init_cities_dict(self, start_city: City):
        """Initializes the cities dict with default values"""
        self._cities.clear()

        # Fill cities list with graph
        for city in self._graph.keys():
            self._cities[city] = {
                'previous_city': None,
                'distance': float('inf')}

        # Set the starting city distance to 0
        self._cities[start_city]['distance'] = 0

    def _get_path(self, end_city: City) -> Path:
        """Returns the path object containing the shortest path to the
        end city"""
        path_to_end: list[City] = [end_city]
        previous_city: City = self._cities[end_city]['previous_city']

        # Rewind each previous city from the end, until our start
        while previous_city is not None:
            path_to_end.insert(0, previous_city)
            previous_city = self._cities[path_to_end[0]]['previous_city']

        path: Path = {
            'total': self._cities[end_city]['distance'],
            'steps': path_to_end
        }

        return path

    def _update_city_infos(self, city: City, previous_city: City,
                           distance: float):
        """Updates a city info in the cities dictionary"""
        self._cities[city] = {'previous_city': previous_city,
                              'distance': distance}

    def _get_neighbours_cities(self, city: City) -> list[City]:
        """Returns the list of neighbours cities from a given city"""
        neighbours: list[City] = []
        for neighbour in self._graph[city]:
            neighbours.append(neighbour)

        return neighbours

    def _get_neighbours_cities_with_distances(self, city: City) -> dict[
        City, float]:
        """Returns the list of neighbours cities from a given city and the
        distance to them"""
        neighbours: dict[City, float] = {}
        for neighbour, distance in self._graph[city].items():
            neighbours[neighbour] = distance

        return neighbours
