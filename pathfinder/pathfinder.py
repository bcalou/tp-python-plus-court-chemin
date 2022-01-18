from genericpath import exists
from pathfinder.city import City
from pathfinder.path import Path
from pathfinder.graph import graph


class PathFinder:
    def __init__(self, graph) -> None:
        self.graph = graph

    def get_distance(self, start, end):
        cities_to_visit: list[City] = [start]
        cities_visited: list[City] = [start]
        cities = {}

        actual_city: City = start
        cities[start] = {
            "distance": 0,
            "from":"is start"
        }
        while actual_city != end:
            for correspondance in graph[actual_city]:
                # Set_cities_to_visit
                if correspondance not in cities_to_visit and correspondance not in cities_visited:
                    cities_to_visit.append(correspondance)

                # Set_distance    
                distance = cities[actual_city]["distance"] + graph[actual_city][correspondance]
                if correspondance not in cities:
                    cities[correspondance] = {
                        "distance": distance,
                        "from": actual_city
                    }
                elif cities[correspondance]["distance"] > distance:
                    cities[correspondance]["distance"] = distance
                    cities[correspondance]["from"] = actual_city
            # upgrade_distance
            cities_to_visit.remove(actual_city)
            cities_visited.append(actual_city)
            minstep = float("inf")
            for city in cities_to_visit:
                if cities[city]["distance"] < minstep:
                    minstep = cities[city]["distance"]
                    actual_city = city
        return cities

    def set_shortest_path(self, start, end, cities):
        steps = []
        actual_city = end
        steps.append(actual_city)
        while actual_city != start:
            actual_city = cities[actual_city]["from"]
            steps.insert(0, actual_city)
        return steps

    def get_shortest_path(self, start: City, end:City) -> Path:
        shortest_path: Path = {
            "total": 0,
            "steps": []
        }
        
        cities = self.get_distance(start, end)

        shortest_path["steps"] = self.set_shortest_path(start, end, cities)
        shortest_path["total"] = cities[end]["distance"]

        return shortest_path