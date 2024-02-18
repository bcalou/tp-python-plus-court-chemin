from pathfinder.pathfinder import Pathfinder
from pathfinder.astar import AStar
from pathfinder.spfa import SPFA
from pathfinder.graphs import graph, spfa_graph
from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.types import Path

pathfinder = Pathfinder(graph)
pathfinder_a = AStar(graph, heuristics)
pathfinder_spfa = SPFA(spfa_graph)

# path_d: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
# print(f" Dijkstra : {path_d}")

# path_a: Path = pathfinder_a.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
# print(f"A* : {path_a}")

path_spfa: Path = \
    pathfinder_spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(f"SPFA : {path_spfa}")
