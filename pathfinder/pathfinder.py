from typing import Dict
from pathfinder.city import City
from pathfinder.path import Path
from pathfinder.graph import graph
import math


class PathFinder:
    def __init__(self, graph: Dict):
        self.graph = graph

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

    def _route(self, end, cities_to_visit, cities):
        for neighbor in self.graph[cities_to_visit[0]]:
            if(neighbor in cities.keys()):
                if(cities[neighbor][1] > self.graph[cities_to_visit[0]][neighbor]+cities[cities_to_visit[0]][1]):
                    cities[neighbor] = [
                            cities_to_visit[0], self.graph[cities_to_visit[0]][neighbor]+cities[cities_to_visit[0]][1]]
                    cities_to_visit.append(neighbor)
            else:
                cities[neighbor] = [cities_to_visit[0], self.graph[cities_to_visit[0]]
                                        [neighbor]+cities[cities_to_visit[0]][1]]
                cities_to_visit.append(neighbor)
            cities_to_visit = self._check_end(end, cities_to_visit, cities)
        cities_to_visit.remove(cities_to_visit[0])

    def _sort(self, cities: Dict, cities_to_visit : list[City]):
        for i in range(1, len(cities_to_visit)):
            y = i
            while(cities[cities_to_visit[i]][1] <= cities[cities_to_visit[y]][1] and y != -1):
                y -= 1
            cities_to_visit.insert(y+1, cities_to_visit[i])
            cities_to_visit.pop(i+1)  
        return cities_to_visit

    def _check_end(self, end, cities_to_visit, cities):
        if end in cities.keys():
            for city_check in cities_to_visit:
                if cities[city_check][1] > cities[end][1]:
                    cities_to_visit.remove(city_check)
        return cities_to_visit

    def _path(self, start, cities, parcours):
        current_path: list[City] = []
        while parcours.value != start.value:
            current_path.append(parcours)
            parcours = cities[parcours][0]
        current_path.append(start)
        current_path.reverse()
        return current_path
