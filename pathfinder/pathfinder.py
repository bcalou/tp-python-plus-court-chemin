from pathfinder.city import City
from pathfinder.path import Path
from typing import TypedDict

class CityData(TypedDict):
  parent: City | None
  weight: float

class PathFinder:
  graph: dict[City, dict[City, int]]

  def __init__(self, graph: dict[City, dict[City, int]]):
    self.graph = graph

  def get_shortest_path(self, start: City, end: City) -> Path:
    citiesToVisit = [start]
    cities: dict[City, CityData] = {
      start: {"parent": None, "weight": 0},
      end: {"parent": None, "weight": float("inf")}
    }
    visitedCity: list[City] = []

    totalCalcul: int = 0
    while len(citiesToVisit) > 0:
      totalCalcul += 1
      # Get city with the lowest cost
      currentCity: City = self.getNearestCity(cities, citiesToVisit)
      for city in self.graph[currentCity]:
        if city in visitedCity:
          continue
        futurWeight = cities[currentCity]["weight"] + self.graph[currentCity][city]
        if city not in cities or cities[city]["weight"] > futurWeight:
          # Add the city to the list
          cities[city] = {
            "parent": currentCity,
            "weight": futurWeight
          }
          # We need to visit the city if the weight is worth it
          if cities[city]["weight"] < cities[end]["weight"] and city not in citiesToVisit:
            citiesToVisit.append(city)
      visitedCity.append(currentCity)
      citiesToVisit.remove(currentCity)
      # print("Total calculs:", totalCalcul)
    return self.make_path(cities, end)

  def getNearestCity(self, cities: dict[City, CityData], citiesToVisit: list[City]) -> City:
    citiesCost: dict[City, float] = {x : cities[x]["weight"] for x in cities if x in citiesToVisit}
    return min(citiesCost.items(), key=lambda x: x[1])[0]
    
  def make_path(self, cities: dict[City, CityData], end: City):
    path: Path = {"total": cities[end]["weight"], "steps": []}
    currentCity = end
    while currentCity != None:
      path["steps"].append(currentCity)
      currentCity = cities[currentCity]["parent"]
    path["steps"].reverse()
    return path