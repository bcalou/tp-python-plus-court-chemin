from pathfinder.astar import AStar
from pathfinder.pathfinder import *

pathfinder = PathFinder(graph)

astar = AStar(graph, heuristics)
print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

