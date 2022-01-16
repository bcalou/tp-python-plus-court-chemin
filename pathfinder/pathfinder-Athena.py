from math import dist
from pathfinder.graph import *
from pathfinder.path import Path

class PathFinder:
    def __init__(self,graph):
        self.graph = graph

    def get_shortest_path(self,start:City,end:City)->Path:
        cities_to_visit:list[City] = list(graph.keys())
        cities:list[City] = [start]
        list_path_city:dict[City,Path]= {}
        tempPath:Path = {
            "total" : 0,
            "steps" : cities
        }

        list_path_city[start] = tempPath

        for city in cities:
            if(city != end):
                AllCitiesNeighbor:dict[City,int] = graph[city]

                for citiesNeighbor in AllCitiesNeighbor:
                    if(citiesNeighbor in cities_to_visit):
                        distance:float = AllCitiesNeighbor[citiesNeighbor] + list_path_city[city]["total"]
                        tempPath:Path = {
                            "total" : distance,
                            "steps" : city
                        }

                        if(citiesNeighbor in list_path_city):
                            if(list_path_city[citiesNeighbor]["total"]> AllCitiesNeighbor[citiesNeighbor]):
                                list_path_city[city] = tempPath

                        else:
                            cities.append(citiesNeighbor)
                            list_path_city[city] = tempPath
                
            cities_to_visit.remove(city)
        
        print(len(list_path_city))
        print(list_path_city)
        path:Path = {
            "total" : 0,
            "steps" : cities
        }
        return path
