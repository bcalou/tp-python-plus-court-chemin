from asyncio.windows_events import NULL
from cmath import inf
from pathfinder.city import City
from pathfinder.graph import graph
from pathfinder.path import Path

class PathFinder:
    # graph : dict[City, dict[City, int]]
    def __init__(self, graph):
        self.graph = graph

    def get_shortest_path(self, start : City, end : City):
        self.cities = {}
        cities_to_visit : list[City] = [start]
        cities_already_visited : list[City] = []
        shortest_path : Path = {"total" : inf, "steps": [end]}

        #
        for city in self.graph:
            self.cities[city] = {"distance" : float("inf"), "from" : City}
        self.cities[start]["distance"] = 0

        #
        while len(cities_to_visit) > 0:
            closest_city = cities_to_visit[0]
            for each_city in cities_to_visit:
                if self.cities[each_city]["distance"] < self.cities[closest_city]["distance"]:
                    closest_city = each_city
            
            for neighbor_city in self.graph[closest_city]:
                if self.cities[neighbor_city]["distance"] > self.graph[closest_city][neighbor_city] + self.cities[closest_city]["distance"]:
                    self.cities[neighbor_city]["distance"] = self.graph[closest_city][neighbor_city] + self.cities[closest_city]["distance"]
                    self.cities[neighbor_city]["from"] = closest_city
                if neighbor_city not in cities_to_visit and neighbor_city not in cities_already_visited:
                    cities_to_visit.append(neighbor_city)
                    
            cities_to_visit.remove(closest_city)
            cities_already_visited.append(closest_city)

        #
        shortest_path["total"] = self.cities[end]["distance"]
        for each_city in self.cities:
            while end != start:
                end = self.cities[end]["from"]
                shortest_path["steps"].append(end)

        shortest_path["steps"].reverse()
        return shortest_path