from pathfinder.graph import *
from pathfinder.path import *

class PathFinder:
    def __init__(self, routes:dict[City, dict[City, int]]):
        self.routes = routes

    def get_shortest_path(self, start_city: City, end_city: City):
        self.cities = {
            City.BORDEAUX: {
                "distance": float("inf"),
                "from": None
            },
            City.DIJON: {
                "distance": float("inf"),
                "from": None
            },
            City.LILLE : {
                "distance": float("inf"),
                "from": None
            },
            City.LYON : {
                "distance": float("inf"),
                "from": None
            },
            City.MARSEILLE : {
                "distance": float("inf"),
                "from": None
            },
            City.NANTES : {
                "distance": float("inf"),
                "from": None
            },
            City.ORLEANS : {
                "distance": float("inf"),
                "from": None
            },
            City.PARIS : {
                "distance": float("inf"),
                "from": None
            },
            City.RENNES : {
                "distance": float("inf"),
                "from": None
            },
            City.ROUEN : {
                "distance": float("inf"),
                "from": None
            },
            City.STRASBOURG : {
                "distance": float("inf"),
                "from": None
            },
            City.TOULOUSE : {
                "distance": float("inf"),
                "from": None
            }
        }
        self.cities[start_city]["distance"] = 0
        cities_to_visit = [start_city]
        city_counter = 0
        while city_counter <= 11:
            for next_possible_city in self.routes[cities_to_visit[city_counter]]:
                if not next_possible_city in cities_to_visit :
                    cities_to_visit.append(next_possible_city)
                if self.cities[next_possible_city]["distance"] > self.routes[cities_to_visit[city_counter]][next_possible_city] + self.cities[cities_to_visit[city_counter]]["distance"]:
                    self.cities[next_possible_city]["distance"] = self.routes[cities_to_visit[city_counter]][next_possible_city] + self.cities[cities_to_visit[city_counter]]["distance"]
                    self.cities[next_possible_city]["from"] = cities_to_visit[city_counter]
            city_counter += 1
            
        fastest_path: Path = {
            "total" : self.cities[end_city]["distance"],
            "steps" : [end_city]
        }
        current_city = end_city
        while self.cities[current_city]["from"] != None:
            if self.cities[current_city]["from"] != None:
                fastest_path["steps"].insert(0, self.cities[current_city]["from"])
                current_city = self.cities[current_city]["from"]
        return fastest_path