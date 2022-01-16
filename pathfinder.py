from pathfinder.astar import AStar
from pathfinder.pathfinder import *
from pathfinder.spfa import SPFA

pathfinder = PathFinder(graph)
astar = AStar(graph, heuristics)
# spfa = SPFA(spfa_graph)

print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
