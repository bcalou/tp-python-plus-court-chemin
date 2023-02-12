from pathfinder.pathfinderClass import PathFinder
from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path


class SPFA(PathFinder):
    
    def __init__(self, graph: Graph):
        PathFinder.__init__(self, graph)

    def get_shortest_path(self, start: City, end: City) -> Path:
        # Initialize the weight dictionary
        self.init_weight(start)
        # Set the starting city as the first city to be evaluated
        self.current_cities = [start]
        self.next_cities_to_visit = [start]
        # Start with an empty list of visited cities
        self.visited_cities = []
        # Keep evaluating cities until there are no more cities to be evaluated
        while len(self.current_cities) > 0:
            # Set the current cities to be evaluated in the next iteration
            self.current_cities = self.next_cities_to_visit.copy()
            # Clear the list of cities to be evaluated in the next iteration
            self.next_cities_to_visit.clear()
            # Check the distance to each neighboring city
            self.check_distance()
            # Add the evaluated cities to the list of visited cities
            self.visited_cities.extend(self.current_cities)
        # Return the shortest path from the starting city to the end city
        return self.get_path(end)




    def check_distance(self):
        # Check the distances of the nearest cities of the city we are
        # visiting
        for current_city in self.current_cities:
            neighbour_cities: dict[City, float] = self.get_neighbours_by_distances(current_city)


            for neighbour_city, distance in neighbour_cities.items():

                # The distance to the city is the distance to that
                # city + the distance to get to the city we are visiting
                city_distance = distance + self.weight[current_city]['distance']

                # Update city info only if the distance is smaller
                if self.weight[neighbour_city]['distance'] > city_distance:
                    self.update_weight_dict(neighbour_city, current_city, city_distance)

                # Only visit this city if it hasn't been visited before
                if neighbour_city not in self.visited_cities:
                    self.next_cities_to_visit.append(neighbour_city)