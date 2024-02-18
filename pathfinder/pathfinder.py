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

    visited_cities: list[City] = []
    cities_to_visit: list[City] = []

    # distance_to_cities permet de connaitre la distance
    # d'une ville à `start` en fonction d'un chemin
    distance_to_cities = {}
    # previous_city stock ce chemin
    previous_cities: dict[City, City] = {}

    # Stocke le chemin et son cout
    result_path: list[City] = []
    real_distance: float = 0

    # Stocke la ville précédente.
    previous_city: City

    distance_calculations: int = 0

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def setup_variables(self, start: City, end: City) -> None:
        """
        Permet de préparer les variables et les listes utiliser pour la
        résolution de l'algorithme.
        """
        self.visited_cities: list[City] = []
        self.cities_to_visit: list[City] = [start]
        self.distance_to_cities = {start: 0}
        self.previous_cities: dict[City, City] = {}
        self.result_path: list[City] = [end]
        self.real_distance: float = 0
        self.previous_city: City = start
        self.distance_calculations = 0

    def early_break(self, current_city: City, end: City) -> bool:
        """
        Cette fonction permet de quitter en avance la boucle pour les
        algorythmes compatibles.

        Cette version est compatible avec Dijkstra et A*.
        """
        # Si cette condition est vraie alors la ville
        # la plus proche est la ville d'arrivé.
        # Il n'y a pas d'autre chemin plus court possible.
        return current_city == end

    def visited_city(self, city: City) -> None:
        """Permet d'indiquer si une ville a été visité"""
        self.visited_cities.append(city)
        self.cities_to_visit.remove(city)

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Applique l'algorithme de Dijkstra

        La fonction considère que la ville d'arrivé est présente et accéssible
        dans le `graph` passé à la création de l'objet Pathfinder.
        """
        self.setup_variables(start, end)

        # Dijkstra continue tant qu'il reste des villes à visiter
        while len(self.cities_to_visit) != 0:
            # cities_to_visit est trié dans l'ordre croissant des distances
            # Ici on prends la ville la plus proche
            current_city: City = self.cities_to_visit[0]

            # TODO ASTAR Quitter dès que strasbourg visible

            if self.early_break(current_city, end):
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
                    self.previous_cities[neighbour] = current_city

            # Ajouter les voisines aux villes à visiter
            for city in list(neighbours.keys()):
                # Si elle n'ont pas déjà été visité / prévu d'être visité
                if (city not in self.visited_cities and
                    city not in self.cities_to_visit):
                    self.cities_to_visit.append(city)


            self.sort_cities_to_visit()

            # Cette ville à été visité
            self.visited_city(current_city)

            self.previous_city = current_city

        self.get_path(start)

        print(f"Distances mise à jour {self.distance_calculations} fois.")

        return Path(total=self.real_distance, steps=self.result_path)

    def sort_cities_to_visit(self) -> None:
        """
        Trie les villes à visiter en fonction de la distance à `start`
        """
        self.cities_to_visit = sorted(
            self.cities_to_visit,
            key=self.distance_to_city
        )

    def get_path(self, start: City) -> None:
        """
        Trouve le chemin en partant de la fin jusqu'a la ville du début
        """
        for city in self.result_path:
            if city == start:
                break
            self.real_distance += self.graph[self.previous_cities[city]][city]
            self.result_path.append(self.previous_cities[city])
        self.result_path = list(reversed(self.result_path))

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

        self.distance_calculations += 1

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
