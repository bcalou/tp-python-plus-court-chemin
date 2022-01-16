from cmath import inf
from pathfinder.graph import *
from pathfinder.city import *
from pathfinder.path import *

class PathFinder:
    graph: Dict[City, Dict[City, int]]
    # Les prochaines villes à visiter
    cities_to_visit: list[City] = []
    # La distance par rapport à la ville de départ de chaque ville avec la dernière ville traversée
    distances_per_city = {}
    # Les villes qui ont été visitées, à ne pas revisiter
    visited_cities: list[City] = []

    def __init__(self, graph: Dict[City, Dict[City, int]]) -> None:
        self.graph = graph

    def visit_city(self, city: City) -> None:
        # On parcourt chaque ville reliée à la ville à visiter
        for adjacent_city, distance in graph[city].items():
            # Si la ville adjacente n'est pas encore visitée
            if adjacent_city not in self.visited_cities:
                # On ajoute la ville à la liste des prochaines villes à visiter si elle n'y est pas déjà
                if adjacent_city not in self.cities_to_visit:
                    self.cities_to_visit.append(adjacent_city)
                # Si la distance entre la ville de départ et la ville adjacente en passant par la ville à visiter est inférieure à la dernière distance enregistrée
                if distance + self.distances_per_city[city]["distance"] < self.distances_per_city[adjacent_city]["distance"] :
                    # On remplace la donnée : la distance minimale est obtenue en passant par la ville à visiter
                    #print("New distance for", adjacent_city.value, ":", distance + self.distances_per_city[city]["distance"], "from", city.value)
                    self.distances_per_city[adjacent_city]["distance"] = distance + self.distances_per_city[city]["distance"]
                    self.distances_per_city[adjacent_city]["from"] = city
        # On retire la ville des villes à visiter pour l'ajouter aux villes visitées
        self.cities_to_visit.remove(city)
        self.visited_cities.append(city)

    def get_shortest_path(self, start: City, end: City) -> Path:
        # On réinitialise les données à chaque test
        self.cities_to_visit = []
        self.distances_per_city = {}
        self.visited_cities = []
        # On ajoute la première ville à visiter qui est la ville de départ
        self.cities_to_visit.append(start)
        # On règle la distance de chaque ville à l'infini puisqu'elle n'est pas traîtée
        for city in graph.keys():
            self.distances_per_city[city] = {
                "distance": float("inf"),
                "from": start
            }
        # La ville de départ est à une distance de 0
        self.distances_per_city[start]["distance"] = 0
        self.distances_per_city[start]["from"] = None

        # Tant qu'il reste des villes à visiter, on boucle
        while len(self.cities_to_visit) != 0:
            # On répertorie par distance les prochaines villes à visiter
            next_visits: Dict[int, City] = {}
            # On remplit ce dictionnaire avec la distance par rapport à la ville de départ
            for city in self.cities_to_visit:
                next_visits[self.distances_per_city[city]["distance"]] = city
            # On trie le dictionnaire
            next_visits = sorted(next_visits.items())
            # On visite chaque ville du dictionnaire dans leur ordre de distance
            for city in next_visits:
                self.visit_city(city[1])

        # On définit le chemin final en partant de la ville de fin
        path: Path = {
            "total": self.distances_per_city[end]["distance"],
            "steps": [end]
        }
        # On récupère la ville finale
        step: City = self.distances_per_city[end]["from"]
        # Tant qu'on est pas remonté à la ville de départ, on ajoute aux étapes la ville offrant la plus courte distance
        while step != start:
            path["steps"].append(step)
            step = self.distances_per_city[step]["from"]
        # On retourne la ville finale avec les étapes dans le bon sens et la ville de départ ajoutée
        path["steps"].append(start)
        path["steps"].reverse()
        return path