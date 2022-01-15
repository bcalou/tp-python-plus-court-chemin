from pathfinder.pathfinder import *
from pathfinder.astar import *
from pathfinder.heuristics import *

pathfinder = PathFinder(graph)

# print(pathfinder.get_shortest_path(City.STRASBOURG, City.BORDEAUX))

astar = AStar(graph, heuristics)

print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
