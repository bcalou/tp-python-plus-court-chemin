from pathfinder.pathfinder import *
from pathfinder.astar import *
from pathfinder.heuristics import *
from pathfinder.spfa import *

pathfinder = PathFinder(graph)
astar = AStar(graph, heuristics)
spfa = SPFA(spfa_graph)

# print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

# print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

print(spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
