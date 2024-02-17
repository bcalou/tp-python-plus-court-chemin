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

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Applique l'algorithme de Dijkstra"""
        visited_cities: list[City] = []
        cities_to_visit: list[City] = [start]

        # Compte le nombre de màj des distances
        stats: int = 0

        # Ces deux dictionnaire fonctionnent ensemble
        # distance_to_cities permet de connaitre la distance
        # d'une ville à `start` en fonction d'un chemin
        distance_to_cities: dict[City, float] = {start: 0}
        # previous_city stock ce chemin
        previous_city: dict[City, City] = {}

        while len(cities_to_visit) != 0:
            # cities_to_visit est trié dans l'ordre croissant des distances
            # Ici on prends la ville la plus proche
            current_city: City = cities_to_visit[0]

            if current_city == end:
                # Si cette condition est vraie alors la ville
                # la plus proche est la ville d'arrivé.
                # Il n'y a pas d'autre chemin plus court possible.
                break

            neighbours: dict[City, float] = self.graph.get(current_city)
            sorted_neighbours = sort_dict_by_value(neighbours)

            for neighbour, distance in sorted_neighbours:
                # La distance à une ville c'est la distance à la ville actuelle
                # + Ville actuelle vers voisine
                current_distance = distance_to_cities[current_city] + distance

                # Si la voisine n'est pas répertorier, ou si ce nouveau
                # chemin est plus court, on màj distance&previous
                if (neighbour not in distance_to_cities
                   or distance_to_cities[neighbour] > current_distance):
                    stats += 1
                    distance_to_cities[neighbour] = current_distance
                    previous_city[neighbour] = current_city

            # Ajouter les voisines aux villes à visiter
            for city, _ in neighbours.items():
                # Si elle n'ont pas déjà été visité / prévu d'être visité
                if city not in visited_cities and city not in cities_to_visit:
                    cities_to_visit.append(city)

            # Trie les villes à visiter en fonction de la distance à `start`
            cities_to_visit = sorted(
                cities_to_visit,
                key=lambda x: distance_to_cities[x]
            )

            # Cette ville à été visité
            visited_cities.append(current_city)
            cities_to_visit.remove(current_city)

        # On parcours le chemin à l'envert
        result_path: list[City] = [end]
        for city in result_path:
            if city == start:
                break
            result_path.append(previous_city[city])
        result_path = list(reversed(result_path))

        print(f"Nombre de mise à jour des distances: {stats}")

        return Path(total=distance_to_cities[end], steps=result_path)
