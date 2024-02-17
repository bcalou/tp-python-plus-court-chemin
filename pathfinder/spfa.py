from pathfinder.city import City
from pathfinder.pathfinder import Pathfinder
from pathfinder.type import Path


class SPFA(Pathfinder):
    def get_shortest_path(self, start: City, end: City) -> Path:
        """Returns the shortest path between two cities using SPFA algorithm"""
        paths: dict[City, Path] = {}
        for city in self.graph:
            paths[city] = {"total": float('inf'), "steps": []}

        paths[start] = {"total": 0, "steps": [start]}

        max_iterations: int = len(self.graph) - 2

        i: int = 0
        modified: bool = True
        while i < max_iterations and modified is True:
            modified = False
            for city, distances in self.graph.items():
                for next_city, distance in distances.items():
                    potential_distance: float = paths[city]["total"] + distance
                    if paths[next_city]["total"] <= potential_distance:
                        continue
                    # change the path only if the new path is shorter
                    paths[next_city]["total"] = potential_distance
                    paths[next_city]["steps"] = paths[city]["steps"] + [
                        next_city]
                    modified = True
            i += 1

        return paths[end]
