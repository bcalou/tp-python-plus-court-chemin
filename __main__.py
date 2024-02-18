from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph, spfa_graph
from pathfinder.heuristics import heuristics
from pathfinder.pathfinder import Pathfinder
from pathfinder.spfa import SPFA

pathfinder = Pathfinder(graph)
shortest_path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(shortest_path)

astar = AStar(graph, heuristics)
shortest_path_astar = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(shortest_path_astar)

spfa = SPFA(spfa_graph)
shortest_path_spfa = spfa.get_shortest_path(City.NANTES, City.LILLE)
print(shortest_path_spfa)
