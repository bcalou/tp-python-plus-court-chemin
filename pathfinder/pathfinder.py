from pathfinder.graphs import Graph
from pathfinder.types import Path
from pathfinder.city import City
from pathfinder.utils import sort_dict_by_value

class Pathfinder:
    """
    La classe pathfinder permet d'implémenter un
    algorithme du plus court chemin

    Par défaut elle implémenter l'algorithme de dijkstra
    (https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
    """
    graph: Graph

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path :
        visited_cities: list[City] = []
        cities_to_visit: list[City] = [start]
        distance_to_cities: dict[City, float] = {start: 0}
        previous_city: dict[City, City] = {}
        
        for current_city in cities_to_visit:
            neighbours: dict[City, float] = self.graph.get(current_city)
            sorted_neighbours: list[tuple[City, float]] = sort_dict_by_value(neighbours)

            for neighbour, distance in reversed(sorted_neighbours):
                current_distance: float = distance_to_cities[current_city] + distance
                if neighbour not in distance_to_cities or distance_to_cities[neighbour] > current_distance:
                    distance_to_cities[neighbour] = current_distance
                    previous_city[neighbour] = current_city

            for city, _ in distance_to_cities.items():
                if city not in visited_cities:
                    cities_to_visit.append(city)

            visited_cities.append(current_city)
            cities_to_visit.remove(current_city)

        #print(distance_to_cities)
        
        result_path: list[City] = [end]
        for city in result_path:
            if city == start:
                break
            result_path.append(previous_city[city])
        result_path = list(reversed(result_path))
        
        return Path(total=distance_to_cities[end], steps=result_path)
    
