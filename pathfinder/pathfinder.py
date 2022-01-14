from pathfinder.graph import *
from pathfinder.path import *

cities = {
    City.BORDEAUX: {
        "distance": float("inf"),
        "from": City.DIJON
    },
    City.DIJON: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.LILLE: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.LYON: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.MARSEILLE: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.NANTES: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.ORLEANS: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.PARIS: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.RENNES: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.ROUEN: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.STRASBOURG: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
    City.TOULOUSE: {
        "distance": float("inf"),
        "from": City.BORDEAUX
    },
}

class PathFinder:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbor_range(self, ville: City, tab: list[City]):
        for voisin in graph[ville]:
            # print("v : ", voisin)
            distance = graph[ville][voisin] + cities[ville]["distance"]
            if distance < cities[voisin]["distance"]:
                # print("n : ", distance)
                if voisin not in tab:
                    # print("r: ", voisin)
                    tab.append(voisin)
                cities[voisin]["distance"] = distance 
                cities[voisin]["from"] = ville
        return tab

    def get_shortest_path(self, start: City, end: City):
        cities_to_visit: list[City] = [start]
        cities_not_to_visit: list[City] = []

        path: Path = {
            "total": 0,
            "steps": []
        }

        for city in cities_to_visit:
            if city in cities_not_to_visit:
                break
            else:
                if city == start:
                    cities[start]["distance"] = 0
                nom_ville = city.value
                # print(nom_ville)
                cities_to_visit = self.get_neighbor_range(city, cities_to_visit)
                cities_not_to_visit.append(city)

        neighbor_city: City = end
        path["total"] = cities[neighbor_city]["distance"]

        while start not in path["steps"]:
            path["steps"].insert(0, neighbor_city)
            neighbor_city = cities[neighbor_city]["from"]

        # reset
        for city in cities:
            cities[city]["distance"] = float("inf")

        return path
