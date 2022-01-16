from pathfinder.pathfinder import *
from pathfinder.astar import *

#pathfinder = PathFinder(graph)
#pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

astar_pathfinder = AStar(graph, heuristics)
astar_pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)