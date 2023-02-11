from pathfinder.pathfinder import *
from pathfinder.astar import *
from pathfinder.heuristics import *

pathfinder = PathFinder(graph)
astar = AStar(graph, heuristics)

# print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
