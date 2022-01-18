from typing import final
from pathfinder.pathfinder import PathFinder
from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.heuristics import heuristics

graph = 0
pathfinder =  PathFinder(graph)
astar = AStar(graph, heuristics)

pathfinderFinalpath = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(pathfinderFinalpath)

AStarFinalPath = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(AStarFinalPath)