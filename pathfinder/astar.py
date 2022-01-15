from pathfinder.pathfinder import *
from pathfinder.heuristics import *

class AStar(PathFinder):
    def __init__(self, graph, heuristics):
        PathFinder.__init__(self, graph)
        self.graph = graph
        self.heuristics = heuristics

    def get_neighbor_range(self, ville: City, tab: list[City]):
        for voisin in graph[ville]:
            print(voisin)
            print(graph[ville][voisin])
            print(cities[ville]["distance"])
            print(heuristics[voisin])
            distance_h = graph[ville][voisin] + heuristics[voisin]
            # distance = graph[ville][voisin]
            print(distance_h)
            print(cities[voisin]["distance"] + heuristics[voisin] + heuristics[voisin])
            if distance_h < cities[voisin]["distance"]:
                if voisin not in tab:
                    tab.append(voisin)
                cities[voisin]["distance"] = distance_h
                cities[voisin]["from"] = ville
        return tab

    def sort_by_range(self, tab: list[City]) -> list[City]:
        for i in range(1, len(tab)):
            start_value = cities[tab[i]]["distance"]
            start_city = tab[i]
            current_index = i - 1

            while current_index >= 0 and start_value < cities[tab[current_index]]["distance"] + heuristics[tab[current_index]]:
                tab[current_index + 1] = tab[current_index]
                current_index -= 1
            tab[current_index + 1] = start_city

        return tab

    def get_shortest_path(self, start: City, end: City):
        cities_to_visit: list[City] = [start]
        cities_not_to_visit: list[City] = []

        path: Path = {
            "total": 0,
            "steps": []
        }

        if end not in cities_to_visit:
            for city in cities_to_visit:
                if city in cities_not_to_visit:
                    break
                else:
                    if city == start:
                        cities[start]["distance"] = heuristics[start]
                    cities_to_visit = self.get_neighbor_range(city, cities_to_visit)
                    cities_to_visit = self.sort_by_range(cities_to_visit)
                    cities_not_to_visit.append(city)
                    print(cities_to_visit)
        else:
            for city in cities_to_visit:
                if city in cities_not_to_visit and end in graph[city]:
                    cities[end]["distance"] = cities[city]["distance"] + graph[city][end]
                    cities[end]["from"] = city


        neighbor_city: City = end
        path["total"] = cities[neighbor_city]["distance"]

        while start not in path["steps"]:
            distance = float("inf")
            city: City = City.BORDEAUX
            for voisin in graph[neighbor_city]:
                if cities[voisin]["distance"] < distance: 
                    distance = cities[voisin]
                    city = cities[voisin]["from"]
            print("WHILE")
            print(neighbor_city)
            path["steps"].insert(0, city)
            print(path["total"])
            path["total"] -= heuristics[neighbor_city]
            print(path["total"])
            neighbor_city = cities[city]["from"]

        # reset
        for city in cities:
            cities[city]["distance"] = float("inf")

        return path

    

    
