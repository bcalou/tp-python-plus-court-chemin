from pathfinder.graphs import Graph
from pathfinder.types import Path
from pathfinder.city import City


class Pathfinder:
    """
    La classe pathfinder permet d'implémenter un
    algorithme du plus court chemin

    Par défaut elle implémenter l'algorithme de dijkstra
    (https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
    """
    # Stocke le graphe des villes
    graph: Graph

    # Stocke les distances des villes par rapport au départ du chemin
    distance_to_cities: dict[City, float]

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Applique l'algorithme de Dijkstra

        La fonction considère que la ville d'arrivé est présente et accéssible
        dans le `graph` passé à la création de l'objet Pathfinder.
        """
        visited_cities: list[City] = []
        cities_to_visit: list[City] = [start]

        # Ces deux dictionnaire fonctionnent ensemble
        # distance_to_cities permet de connaitre la distance
        # d'une ville à `start` en fonction d'un chemin
        self.distance_to_cities = {start: 0}
        # previous_city stock ce chemin
        previous_city: dict[City, City] = {}

        # Dijkstra continue tant qu'il reste des villes à visiter
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

            for neighbour in list(neighbours.keys()):
                # Calcule la distance de la ville par rapport à `start`
                neighbour_distance: float = self.find_distance_to_city(
                    neighbour,
                    current_city
                )

                # Si la voisine n'est pas répertorier, ou si ce nouveau
                # chemin est plus court, on màj distance&previous
                if (neighbour not in self.distance_to_cities
                   or self.distance_to_city(neighbour) > neighbour_distance):
                    self.set_distance_to_city(neighbour, neighbour_distance)
                    previous_city[neighbour] = current_city

            # Ajouter les voisines aux villes à visiter
            for city in list(neighbours.keys()):
                # Si elle n'ont pas déjà été visité / prévu d'être visité
                if city not in visited_cities and city not in cities_to_visit:
                    cities_to_visit.append(city)

            # Trie les villes à visiter en fonction de la distance à `start`
            cities_to_visit = sorted(
                cities_to_visit,
                key=self.distance_to_city
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

        return Path(total=self.distance_to_city(end), steps=result_path)

    def distance_to_city(self, city: City) -> float:
        """
        Renvoie la distance d'une ville par rapport au départ du chemin
        depuis le tableau de valeurs connus.
        """
        return self.distance_to_cities[city]

    def set_distance_to_city(self, city: City, distance: float) -> None:
        """
        Permet de rentrer la distance d'une ville dans la table de valeurs.

        `city` est la ville qui va être ajouté.

        `distance` est la distance
        """
        self.distance_to_cities[city] = distance

    def find_distance_to_city(self, city: City, previous: City) -> float:
        """
        Permet de connaître la distance d'une ville par rapport au départ
        du chemin.

        `city` est la ville qui va être ajouté.

        `previous` est la ville par laquelle on est arrivé à `city`
        """
        distance_to_previous: float = self.distance_to_city(previous)
        distance: float = distance_to_previous + self.graph[previous][city]
        return distance
