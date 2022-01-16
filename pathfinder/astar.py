from pathfinder.pathfinder import PathFinder
from typing import Dict
from pathfinder.city import City
from pathfinder.path import Path
from pathfinder.graph import graph
import math

class AStar(PathFinder):

    def __init__(self,graph : Dict,heuristics: Dict):
        self.graph = graph
        self.heuristics = heuristics

    def get_shortest_path(self, start: City, end: City):
        cities_to_visit: list[City] = [start]
        cities = {
            start: [None, 0]
        }
        while cities_to_visit:
            cities_to_visit = self._sort(cities,cities_to_visit)
            self._route(end, cities_to_visit, cities)
        final_Path: Path = {'total': cities[end][1], 'steps': self._path(
            start, cities, end)}
        return final_Path

    def _check_end(self, end, cities_to_visit, cities):
        if end in cities.keys():
            cities_to_visit = ["end"]
        print(cities_to_visit)
        return cities_to_visit

    def _sort(self, cities: Dict, cities_to_visit : list[City]):
        for i in range(1, len(cities_to_visit)):
            y = i
            while(cities[cities_to_visit[i]][1] <= cities[cities_to_visit[y]][1] and y != -1):
                y -= 1
            cities_to_visit.insert(y+1, cities_to_visit[i])
            cities_to_visit.pop(i+1)  
        return cities_to_visit