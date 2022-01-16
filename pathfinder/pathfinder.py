from typing import Dict, TypedDict
from pathfinder.city import City
from pathfinder.path import Path


class CityData(TypedDict):
  parent: City | None
  weight: float

class PathFinder(dict[City, dict[City, int]]):
    graph: dict[City, dict[City, int]]

    def __init__(self, graph: dict[City, dict[City, int]]):
        self.graph = graph

    def get_closest_cities(self, citiesToVisit: list[City], cities:dict[City, CityData]):
        nearCity: City = None
        weight: float = float("inf")
        for city in citiesToVisit:
            if cities[city]["weight"]< weight:
                nearCity = city
                weight = cities[city]["weight"]
        return nearCity

    def set_path(self, cities: dict[City, CityData], end: City):
        path: Path = {"total": cities[end]["weight"], "steps": []}
        currentCity = end
        while currentCity != None:
            path["steps"].append(currentCity)
            currentCity = cities[currentCity]["parent"]
        path["steps"].reverse()
        return path

    def get_shortest_path(self, start: City, end: City):
        citiesToVisit = [start]
        cities: dict[City, CityData] = {
        start: {"parent": None, "weight": 0},
        end: {"parent": None, "weight": float("inf")}
        }

        while len(citiesToVisit) > 0:
            currentCity: City = self.get_closest_cities(citiesToVisit, cities) #retourne la ville la plus proche 
            for city in self.graph[currentCity]:
                futurWeight = cities[currentCity]["weight"] + self.graph[currentCity][city]
                if city not in cities: # first time we see this city
                    # Add the city to the list
                    cities[city] = {
                        "parent": currentCity,
                        "weight": futurWeight
                    }
                    # We need to visit the city if the weight is worth it
                    if cities[city]["weight"] < cities[end]["weight"] and city not in citiesToVisit:
                        citiesToVisit.append(city)
                # We already checked this city so instead of adding it in the list we update it (if the weight is worth it)
                elif cities[city]["weight"] > futurWeight:
                    cities[city] = {"parent": currentCity, "weight": futurWeight}
            citiesToVisit.remove(currentCity)   

        return self.set_path(cities, end)

