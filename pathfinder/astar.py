from typing import List, Dict, Tuple
from heapq import heappop, heappush
from .city import City
from .graphs import Graph
from .types import Path
from .pathfinder import Pathfinder

class AStarPathfinder(Pathfinder):
    def __init__(self, graph: Graph):
        super().__init__(graph)

    def get_shortest_path(self, start: City, end: City) -> Path:
        distances: Dict[City, float] = {city: float('inf') for city in self.graph}
        distances[start] = 0
        previous: Dict[City, City] = {}

        priority_queue: List[Tuple[float, City]] = [(0, start)]

        while priority_queue:
            current_distance, current_city = heappop(priority_queue)

            if current_city == end:
                break

            if current_distance > distances[current_city]:
                continue

            for neighbor, weight in self.graph[current_city].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_city
                    # Calcul de l'estimation heuristique (distance à vol d'oiseau / vitesse du cycliste)
                    heuristic = self.heuristic(neighbor, end)
                    priority = distance + heuristic  # Ajout de l'heuristique au coût actuel
                    heappush(priority_queue, (priority, neighbor))

        path = [end]
        while end != start:
            end = previous[end]
            path.append(end)
        path.reverse()

        return {'total': distances[path[-1]], 'steps': path}

    def heuristic(self, city: City, end: City) -> float:
        # Calcul de la distance à vol d'oiseau entre la ville et la destination
        # Ici, je suppose que la vitesse du cycliste est de 16 km/h
        # Vous pouvez ajuster cette valeur en fonction de vos besoins
        # Assurez-vous que la distance est exprimée en heures pour correspondre au temps
        return self.distance(city, end) / 16

    def distance(self, city1: City, city2: City) -> float:
        # Implémentez le calcul de la distance à vol d'oiseau entre deux villes ici
        # Vous pouvez utiliser la formule de la distance euclidienne entre deux points géographiques
        # Assurez-vous que la distance est exprimée en heures pour correspondre au temps
        pass
