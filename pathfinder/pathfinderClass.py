from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.graphs import Graph
from pathfinder.weights import Weight

class PathFinder:
    def __init__(self, given_graph: Graph, given_weight: Weight):
        self.graph = given_graph
        self.weight = given_weight

        self.all_cities = [
            City.BORDEAUX,
            City.DIJON,
            City.LILLE,
            City.ROUEN,
            City.PARIS,
            City.RENNES,
            City.ORLEANS,
            City.NANTES,
            City.LYON,
            City.TOULOUSE,
            City.MARSEILLE,
            City.STRASBOURG,
        ]

        # City which weight have to be calculated
        self.cities_to_visit = list()


    def get_shortest_path(self, start: City, end: City) -> Path:

        self.weight[start]["distance"] = 0
        self.cities_to_visit.append(start)

        while(len(self.cities_to_visit) >= 1):
            # Get the city in city_to_visit with the smallest weight
            city_with_the_smallest_weight: City = start
            for city in self.cities_to_visit:
                
                if self.weight[city]['distance'] < self.weight[city_with_the_smallest_weight]['distance']:
                    city_with_the_smallest_weight = city

            self._set_weight(city_with_the_smallest_weight)
            ###################################################

        print(self.weight)
        shortest_path: Path = {'total': 0, 'steps': list()}
        return shortest_path


    def _set_weight(self, current_city: City):
        print("____________________________________________")
        print(f'CURRENT CITY : {current_city}')

        if current_city in self.cities_to_visit:
            self.cities_to_visit.remove(current_city)
            print(f'Rmove city : {current_city}')
        
        list_neighbour_cities = self.graph[current_city]
        print(f'list_neighbour_cities : {list_neighbour_cities}')


        print(f'cities to visit : {self.cities_to_visit}')

        for neighbour in list_neighbour_cities:

            if neighbour not in self.cities_to_visit:
                self.cities_to_visit.append(neighbour)

            if self.graph[current_city][neighbour] < self.weight[neighbour]['distance']:

                self.weight[neighbour]['distance'] = self.graph[current_city][neighbour]
                self.weight[neighbour]['come_from'] = current_city

        print(f'cities to visit : {self.cities_to_visit}')
    


# Mettre la ville de départ son poid à 0

#Dans celle qui reste à visiter, on commence par celle qui a la plus petite distance (-> Toulouse), on supprime toulouse
# de la liste des villes à visiter.

# Dès que l'on découvre une ville, on l'ajoute à la liste des ville à visiter

# Si on a déjà un poid par la ville d'arrivé et si le poid d'une ville est supérieur à ce poid alors rien ne sert de 
# continuer en direction de cette ville.

# On arrête le script quand la liste de la ville à visiter est nul.

