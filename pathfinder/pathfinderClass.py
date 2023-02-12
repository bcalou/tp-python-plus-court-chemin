#TO DO:
# Set the starting city's weight to 0

#In the one that remains to be visited, we start with the one with the smallest distance (-> Toulouse), we delete Toulouse
# of the list of cities to visit.

# As soon as we discover a city, we add it to the list of cities to visit

# If we already have a weight by the city of arrival and if the weight of a city is greater than this weight then there is no point in
# continue towards this town.

# We stop the script when the list of the city to visit is null.

from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.graphs import Graph
from pathfinder.types import CityInfo

class PathFinder:
    def __init__(self, given_graph: Graph):
        self.graph = given_graph
        self.weight : dict[City, CityInfo] = {}
        self.visited_cities: list[City] = []
        self.next_cities_to_visit: list[City] = []
        self.current_cities: list[City] = []


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


    def init_weight(self, start_city: City):
        """Initializes the weight dict with default values"""
        self.weight.clear()


        for city in self.graph.keys():
            self.weight[city] = {
                'distance': float('inf'),
                'come_from': None}


        self.weight[start_city]['distance'] = 0


    def check_distance(self):
        # Evaluate each city in the current cities list
        for current_city in self.current_cities:
            # Get the distances to each neighboring city
            neighbour_cities: dict[City, float] = self.get_neighbours_by_distances(current_city)
            # Evaluate each neighboring city
            for neighbour_city, distance in neighbour_cities.items():
                # Calculate the total distance to the neighboring city
                city_distance = distance + self.weight[current_city]['distance']
                # If the total distance is smaller than the previous distance, update the distance
                if self.weight[neighbour_city]['distance'] > city_distance:
                    self.update_weight_dict(neighbour_city, current_city, city_distance)


                if neighbour_city not in self.visited_cities:
                    self.next_cities_to_visit.append(neighbour_city)


    def get_path(self, end_city: City) -> Path:
        """Return the path object containing the shortest path"""
        path_to_end: list[City] = [end_city]
        previous_city: City = self.weight[end_city]['come_from']


        while previous_city is not None:
            path_to_end.insert(0, previous_city)
            previous_city = self.weight[path_to_end[0]]['come_from']

        path: Path = {
            'total': self.weight[end_city]['distance'],
            'steps': path_to_end
        }

        return path


    def update_weight_dict(self, city: City, previous_city: City,
                           distance: float):

        self.weight[city] = {'come_from': previous_city,
                              'distance': distance}



    def get_neighbours_by_distances(self, city: City) -> dict[
        City, float]:
        neighbours: dict[City, float] = {}
        for neighbour, distance in self.graph[city].items():
            neighbours[neighbour] = distance
        return neighbours

