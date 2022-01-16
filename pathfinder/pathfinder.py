from cmath import inf
from pathfinder.graph import *
from pathfinder.city import *
from pathfinder.path import *

class PathFinder:
    graph: Dict[City, Dict[City, int]]
    cities_to_visit: list[City] = []
    cities = {}
    visited_cities: list[City] = []

    def __init__(self, graph: Dict[City, Dict[City, int]]) -> None:
        self.graph = graph

    def visit_city(self, city: City) -> None:
        self.cities_to_visit.remove(city)
        self.visited_cities.append(city)
        for adjacent_city in graph[city].items():
            if adjacent_city[0] not in self.visited_cities:
                self.cities_to_visit.append(adjacent_city[0])
                print("New distance for", adjacent_city[0].value, ":", adjacent_city[1] + self.cities[city]["distance"], "from", city.value)
                self.cities[adjacent_city[0]]["distance"] = adjacent_city[1] + self.cities[city]["distance"]
                self.cities[adjacent_city[0]]["from"] = city

    def get_shortest_path(self, start: City, end: City) -> Path:
        self.cities_to_visit.append(start)
        for city in graph.keys():
            if city == start:
                self.cities[city] = {
                    "distance": float("inf")
                }
            else:
                self.cities[city] = {
                    "distance": float("inf")
                }
        while len(self.cities_to_visit) != 0:
            closest_city = self.cities_to_visit[0]
            for city in self.cities_to_visit:
                if city not in self.visited_cities:
                    if self.cities[city]["distance"] < self.cities[closest_city]["distance"]:
                        closest_city = city
            print("Next visit :", closest_city)
            self.visit_city(closest_city)
            










        
"""         test: Path = {
            "total": 10,
            "steps": [City.BORDEAUX]
        }
        return test """
