
from pathfinder.city import City
from pathfinder.path import path
from pathfinder.graph import graph



class PathFinder :
    def __init__(self, graph):
         self.graph = graph

    cities = {}

    def get_shortest_path(self, start : City, end : City) -> path :

        self.cities = {}
        current_city : City = start
        cities_to_visit : list[City] = [start]
        
        idx : int = 0
        #je rempli le dict cities
        for city in graph :
           self.cities.update({city.name : {"distance" : float("inf"), "from" : City.BORDEAUX}})
        
        self.cities[start.name]["distance"] = 0
        self.cities[start.name]["from"] = City(start)
        while idx != len(City) :
            neighbor : list[City] = graph[current_city]
            for visited_city in neighbor :
                if neighbor[visited_city] + self.cities[current_city.name]["distance"] < self.cities[visited_city.name]["distance"]:
                    self.cities[visited_city.name]["distance"] = neighbor[visited_city] + self.cities[current_city.name]["distance"]
                    self.cities[visited_city.name]["from"] = City(current_city)
                if cities_to_visit.count(visited_city) == 0 : 
                    cities_to_visit.append(visited_city)
            idx +=1
            if idx != len(City) :
                current_city = cities_to_visit[idx]
                
        print("-----------------------------------------")
        for city in self.cities.items() :
             print(city)
        print("-----------------------------------------")


        the_path : path = {
            'total' : 0,
            'steps' : []
        }

        the_path["total"] = self.cities[end.name]["distance"]

        city_path : City = end

        while city_path != start :
            the_path["steps"].append(self.cities[city_path.name]['from'])
            city_path = self.cities[city_path.name]['from']

        the_path["steps"].insert(0,end)
        the_path["steps"].reverse()

        print(the_path)
        return the_path