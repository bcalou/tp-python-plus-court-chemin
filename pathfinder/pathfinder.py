from json.encoder import INFINITY

from graph import *
from path import *


class Distance(TypedDict):
    city: City
    dist: float

class PathFinder:
    graph: dict[City, dict[City, int]] = {} # Graphe des villes
    cityList: list[City] = [] # Villes à visiter
    visitedList: list[City] = [] # Villes à visiter
    distancesDict: dict[City, Distance] = {} # Distance entre les villes
    path: Path = {'total': INFINITY, 'steps': []} # Chemin final

    def __init__(self, graph: dict[City, dict[City, int]]):
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Retourne le chemin le plus court chemin
        """
        self.path: Path = {'total': INFINITY, 'steps': []}

        self.distancesDict = {start: {'city': start, 'dist': 0}}
        self.visitedList: list[City] = [start]
        self.cityList: list[City] = [start]

        self.scan_cities(start, end)

        return self.path
    
    def scan_cities(self, start: City, end: City):
        """
        Scan par récurrence les villes
        """
        scans = self.graph[start].keys()
        min_distance = INFINITY
        next_city: City = start
        for city in scans:
            if city not in self.visitedList:
                self.cityList.append(city)
                distance: float = self.graph[start][city] + self.distancesDict[start]['dist']
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
                if city not in self.distancesDict:
                    self.distancesDict[city] = {'city': start, 'dist': distance}
                elif distance < self.distancesDict[city]['dist']:
                    self.distancesDict[city]['city'] = start
                    self.distancesDict[city]['dist'] = distance
        self.cityList.remove(start)
        self.visitedList.append(start)
        if next_city == end and self.distancesDict[next_city]['dist'] < self.path['total']:
            self.path = {'total': 0, 'steps': [end]}
            self.get_path()
            if len(self.cityList) == 0:
                return
        if next_city != start:
            self.scan_cities(next_city, end)
        return
    
    def get_path(self):
        """
        Retourne le chemin le plus court en fonction des distances de l'objet
        """
        first: City = self.path['steps'][0]
        if len(self.path['steps']) == 1:
                self.path['total'] = self.distancesDict[first]['dist']
        if self.distancesDict[first]['city'] != self.path['steps'][0]:
            self.path['steps'].insert(0, self.distancesDict[first]['city'])
            dist: float = self.distancesDict[first]['dist']
            if dist != 0:
                self.get_path()
        return 
         

pathfinder = PathFinder(graph)

print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
