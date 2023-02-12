from pathfinder.pathfinderClass import PathFinder
from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path


class Astar(PathFinder):
    def __init__(self, graph: Graph, given_heuristics: dict[City, float]):
        self.heuristics = given_heuristics
        PathFinder.__init__(self, graph)
        self.neighbours_with_new_distances: dict[City, float] = {}
        self.is_finished: bool


    def get_shortest_path(self, start: City, end: City) -> Path:


        super().init_weight(start)

        self.neighbours_with_new_distances: dict[City, float] = {}
        self.is_finished: bool = False

        current_city: City = start
        next_city_to_visit: City = start
        


        while not self.is_finished:

            current_city = next_city_to_visit
    

            self.check_distance(end, current_city)

            next_city_to_visit = min( self.neighbours_with_new_distances, key = self.neighbours_with_new_distances.get)
            if next_city_to_visit == end:
                self.is_finished = True


        return self.get_path(end)


    def check_distance(self, end: City, current_city: City):
        super().check_distance()
        # Check the distances of the nearest cities of the city we are
        # visiting

        neighbour_cities: dict[City, float] = self.get_neighbours_by_distances(current_city)


        for neighbour_city, distance in neighbour_cities.items():

            city_heuristics_distance = distance + self.heuristics[neighbour_city]

            # The distance to the city is the distance to that
            # city + the distance to get to the city we are visiting
            city_distance = distance + self.weight[current_city]['distance']

            # Update city info only if the distance is smaller
            if self.weight[neighbour_city]['distance'] > city_distance:
                super().update_weight_dict(neighbour_city, current_city, city_distance)
                self.neighbours_with_new_distances[neighbour_city] = city_heuristics_distance

            if end == neighbour_city:
                self.is_finished = True
                break
