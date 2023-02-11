from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder
from pathfinder.types import Path


class AStar(PathFinder):

    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        PathFinder.__init__(self, graph)
        self._heuristics = heuristics

    def get_shortest_path(self, start: City, end: City) -> Path:
        super()._init_cities_dict(start)

        current_city: City = start
        neighbours_with_new_distances: dict[City, float] = {}
        next_city_to_visit: City = start
        end_has_been_reached: bool = False

        while not end_has_been_reached:

            current_city = next_city_to_visit

            neighbour_cities: dict[
                City, float] = self._get_neighbours_cities_with_distances(
                current_city)

            # Check the distances of the nearest cities of the city we are
            # visiting
            for neighbour_city, distance in neighbour_cities.items():

                # The distance to the city is the distance to that
                # city + the heuristic of the neighbour city
                city_distance_with_heuristics = distance + self._heuristics[
                    neighbour_city]

                # Keep the original distance (without heuristics) for the
                # total distance
                city_distance = distance + self._cities[current_city][
                    'distance']

                # Update city info only if the distance is smaller
                if self._cities[neighbour_city]['distance'] > city_distance:
                    super()._update_city_infos(neighbour_city, current_city,
                                               city_distance)

                    # Fill the list of our updated neighbours
                    neighbours_with_new_distances[
                        neighbour_city] = city_distance_with_heuristics

                if end == neighbour_city:
                    end_has_been_reached = True
                    break

            # The next city we are visiting is the one with the
            # smallest distance
            next_city_to_visit = min(neighbours_with_new_distances,
                                     key=neighbours_with_new_distances.get)

            # If the city is the destination, we stop searching
            if next_city_to_visit == end:
                end_has_been_reached = True

        return self._get_path(end)
