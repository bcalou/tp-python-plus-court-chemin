from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph, spfa_graph
from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.heuristics import heuristics
from pathfinder.spfa import SPFA

pathfinder = Pathfinder(graph)
print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

astar = AStar(graph, heuristics)
print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

spfa = SPFA(spfa_graph)
print(spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG))