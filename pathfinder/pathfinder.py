from typing import List, Dict, Tuple
from heapq import heappop, heappush
from .city import City
from .graphs import Graph
from .types import Path

class Pathfinder:
    def __init__(self, graph: Graph):
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        # Initialisation
        distances: Dict[City, float] = {city: float('inf') for city in self.graph}
        distances[start] = 0
        previous: Dict[City, City] = {}

        # File de priorité pour stocker les villes non traitées
        priority_queue: List[Tuple[float, City]] = [(0, start)]

        while priority_queue:
            # Récupérer la ville avec la plus courte distance
            current_distance, current_city = heappop(priority_queue)

            # Si la distance actuelle est supérieure à la distance enregistrée, ignorer
            if current_distance > distances[current_city]:
                continue

            # Parcourir les voisins de la ville actuelle
            for neighbor, weight in self.graph[current_city].items():
                distance = current_distance + weight
                # Mettre à jour la distance si un chemin plus court est trouvé
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_city
                    heappush(priority_queue, (distance, neighbor))

        # Reconstruction du chemin à partir des informations précédentes
        path = [end]
        while end != start:
            end = previous[end]
            path.append(end)
        path.reverse()

        return {'total': distances[path[-1]], 'steps': path}
