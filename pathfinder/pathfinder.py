from pathfinder.graph import *
from pathfinder.path import Path

class PathFinder:
    def __init__(self,graph):
        self.graph = graph

    def create_path_result(self,start:City,end:City,list_path_city:dict[City,Path])->list[City]:
        path_result:list[City] = list()
        path_result.append(end)
        city_path:City = end
        while city_path != start:
            path_result.append(City(list_path_city[city_path]["steps"]))
            city_path = City(list_path_city[city_path]["steps"])
        path_result.reverse()
        return path_result

    def distance_calculus(self,city:City,AllCitiesNeighbor:dict[City,int],citiesNeighbor:City
        ,list_path_city:dict[City,Path],cities:list[City])->None:
        distance:float = AllCitiesNeighbor[citiesNeighbor] + list_path_city[city]["total"]
        #print("=======")
        #print("City : ",city, " Neighbor : " , citiesNeighbor) 
        #print("AllCitiesNeighbor : ",AllCitiesNeighbor[citiesNeighbor])
        #print("list_path_city : ",list_path_city[city]["total"])
        tempPath:Path = {
            "total" : distance,
            "steps" : city
        }

        if(citiesNeighbor in list_path_city): #If the city neighbor have already a distance associate
            #print("Shortest path :", list_path_city[citiesNeighbor])
            if(distance < list_path_city[citiesNeighbor]["total"]):
                list_path_city[citiesNeighbor] = tempPath
                #print("In " ,citiesNeighbor, " = ", tempPath)

        else:
            if(citiesNeighbor not in cities):
                cities.append(citiesNeighbor)
                list_path_city[citiesNeighbor] = tempPath
                #print("Out ",citiesNeighbor, " = ", tempPath)

    def get_shortest_path(self,start:City,end:City)->Path:
        cities_to_visit:list[City] = list(graph.keys()) #List of cities to visit (evaluate distance)
        cities:list[City] = [start] #List of cities to visit in order of the begining
        list_path_city:dict[City,Path]= {} #List of the shortest way by city
        tempPath:Path = { #Create the initial point of the first city
            "total" : 0,
            "steps" : start
        }
        list_path_city[start] = tempPath

        for city in cities: #Iteration on all city to visit
            if(city != end): #The last one don't need to be execute
                #print(city, "ActualCity")
                AllCitiesNeighbor:dict[City,int] = graph[city] #Get All direction cost of the actual city
                #print(AllCitiesNeighbor)
                for citiesNeighbor in AllCitiesNeighbor: #Reach neigbor city one per one (the name of the city)
                    #print(citiesNeighbor)
                    if(citiesNeighbor in cities_to_visit): #If this neighbor city is already visit (evaluate)
                        self.distance_calculus(city,AllCitiesNeighbor,citiesNeighbor,list_path_city,cities)
                                
                
            cities_to_visit.remove(city)
        
        #print(len(list_path_city))
        #for city in list_path_city:
        #    print(city, " : ", list_path_city[city])

        list_path_city[end]["steps"] = self.create_path_result(start,end,list_path_city)

        return list_path_city[end]
