from pathfinder.path import Path
from pathfinder.city import City


class PathFinder():
    def __init__(self, graph):
        self.graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        # Le dictionnaire cities contient toutes les villes
        # chacune a comme attributs sa distance de start ainsi que la précédente ville de son chemin
        cities = {}
        cities_to_test: list[City] = []
        for city in self.graph:
            cities_to_test.append(city)
            cities[city] = {"distance": float("inf"), "origin": start}
        cities[start]["distance"] = 0
        cities_to_test = sorted(
            cities_to_test, key=lambda d: cities[d]["distance"])
        while len(cities_to_test) > 0:
            current_city = cities_to_test[0]
            for neighbor_city in self.graph[current_city]:
                if neighbor_city != cities[current_city]["origin"]:
                    distance = cities[current_city]["distance"] + \
                        self.graph[current_city][neighbor_city]
                    if distance < cities[neighbor_city]["distance"]:
                        cities[neighbor_city]["distance"] = distance
                        cities[neighbor_city]["origin"] = current_city
                        difference = cities[neighbor_city]["distance"] - distance
                        for neighbor_neighbor in self.graph[neighbor_city]:
                            # Si on trouve un chemin plus court à une ville qui fait parti du chemin d'autres villes
                            # on retire la différence de distance pour chacune de ces autres villes
                            if cities[neighbor_neighbor]["origin"] == neighbor_city:
                                neighbor_neighbor["distance"] -= difference
            cities_to_test.remove(current_city)
            # entre chaque iteration de la boucle on tri cities_to_test en fonction de la distance de chaque ville
            # afin de choisir la ville la plus prometteuse pour la prochaine iteration
            cities_to_test = sorted(
                cities_to_test, key=lambda d: cities[d]["distance"])
        final_path: Path = {
            "total": cities[end]["distance"],
            "steps": []
        }
        current_city = end
        while current_city != start:
            final_path["steps"].insert(0, cities[current_city]["origin"])
            current_city = cities[current_city]["origin"]
        final_path["steps"].append(end)
        return final_path
