from pathfinder.city import *
from pathfinder.path import *
from pathfinder.pathfinder import *


class AStar(PathFinder):
    def __init__(self, graph: dict[City, dict[City, int]], heuristics: dict[City, float]):
        super()
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Retourne le chemin le plus court chemin
        """
        # Initialisation des distances des villes
        cities: dict[City, Distance] = {}
        for city in self.graph.keys():
            cities[city] = {'parent': start, 'distance': INFINITY}
        cities[start]['distance'] = 0

        cities_to_visit: list[City] = [start]

        # On continue le calcul tant qu'il reste des villes à visiter
        while len(cities_to_visit) > 0:
            visiting_city: City = cities_to_visit.pop()
            # Pour les villes connectées à la ville scannée, on calcule les distances des plus loins aux plus proches
            sorted_graph = sorted(self.graph[visiting_city].items(), key=lambda city: city[1] + heuristics[city[0]], reverse=True)
            for destination, distance in sorted_graph:
                # On précalcule la distance pour chaque ville
                distance += cities[visiting_city]['distance']
                if cities[destination]['distance'] == INFINITY and destination != end:
                    cities_to_visit.append(destination)
                if cities[destination]['distance'] > distance + heuristics[destination]:
                    cities[destination] = {'parent': visiting_city, 'distance': distance}
                    # On revisite les villes dont les distances ont été modifiées
                    cities_to_visit.append(destination)
                if destination == end:
                    return self.get_path(cities, end)
                

        return self.get_path(cities, end)
