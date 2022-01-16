from pathfinder.city import *
from pathfinder.path import *
from pathfinder.pathfinder import *


class AStar(PathFinder):
    def __init__(self, graph: dict[City, dict[City, int]], heuristics: dict[City, float]):
        super()
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:

        # Initialisation des distances des villes
        dictCity: dict[City, Distance] = {}
        for city in self.graph.keys():
            dictCity[city] = {'parent': start, 'distance': INFINITY}
        dictCity[start]['distance'] = 0

        dictCity_to_visit: list[City] = [start]

        #  Tant qu'il reste des villes à visiter le calcul continue
        while len(dictCity_to_visit) > 0:
            visiting_city: City = dictCity_to_visit.pop()
            # On calcule les distances des plus loins aux plus proches des villes connectées à la ville scannée
            sorted_graph = sorted(self.graph[visiting_city].items(), key=lambda city: city[1] + heuristics[city[0]], reverse=True)
            for destination, distance in sorted_graph:
                # On précalcule la distance pour chaque ville
                distance += dictCity[visiting_city]['distance']
                if dictCity[destination]['distance'] == INFINITY and destination != end:
                    dictCity_to_visit.append(destination)
                if dictCity[destination]['distance'] > distance + heuristics[destination]:
                    dictCity[destination] = {'parent': visiting_city, 'distance': distance}
                    # On revisite les villes dont les distances ont été modifiées
                    dictCity_to_visit.append(destination)
                if destination == end:
                    return self.get_path(dictCity, end)
                

        return self.get_path(dictCity, end)
