from pathfinder.graphs import graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City


def run_pathfinder():
    pathfinder: Pathfinder = Pathfinder(graph)
    
    print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))


run_pathfinder()
