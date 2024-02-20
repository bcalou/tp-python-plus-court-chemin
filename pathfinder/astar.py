from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder

class AStar(Pathfinder):
    """
    The AStar class inherited from pathfinding.
    """
    def __init__(self, graph: Graph, heuristics: dict) -> None:
        super().__init__(graph)
        self._heuristics = heuristics

    def update_neighbor(self, neighbor: City, current_city: City, weight: float) -> None:
        current_distance = self.city_info[current_city]['distance']
        total_distance = current_distance + weight

        if total_distance < self.city_info[neighbor]['distance'] + self._heuristics[neighbor]:
            self.city_info[neighbor]['closest_city'] = current_city
            self.city_info[neighbor]['distance'] = total_distance

    def get_next_city(self) -> City:
        self.unvisited_cities = {
            city: info['distance'] + self._heuristics[city]
            for city, info in self.city_info.items()
            if city not in self.visited_cities
        }
        return min(self.unvisited_cities, key=self.unvisited_cities.get)
