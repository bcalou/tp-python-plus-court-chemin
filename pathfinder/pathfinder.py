from functools import total_ordering
from pathfinder.city import *
from pathfinder.path import *
from pathfinder.graph import *
from typing import TypedDict
import math

class PathFinder :
    def __init__(self, graph):
        self.graph = graph
        self.tested=[]
    
    def closest_city(self, city, km) :
        total=km+math.inf
        closest=city
        for i in graph[city] :
            if (i in self.tested) :
                print(i ," déjà visitée.")
            else :
                if((km+graph[city][i])<total) :
                    total=km+graph[city][i]
                    closest=i
        return([closest, total])
    
    def get_shortest_path(self, start, end) :
        self.tested=[]

        path: Path = {
            "total" : math.inf,
            "steps" : []
        }

        closest=[start, 0]
        self.tested.append(start)
        
        while (closest[0]!=end) :
            print(closest)
            self.tested.append(closest[0])
            path["steps"].append(closest[0])
            closest=self.closest_city(closest[0], closest[1])

        #closest=self.closest_city(closest[0], closest[1])
        path["steps"].append(end)
        path["total"]=closest[1]
                
        
        return path