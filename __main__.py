from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph, spfa_graph
from pathfinder.spfa import SPFA
from pathfinder.types import Path
from pathfinder.astar import AStar

pathfinder: Pathfinder = Pathfinder(graph)
path: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(path)
print(pathfinder.get_counter())

astar = AStar(graph, heuristics)
second_path: Path = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(second_path)
print(astar.get_counter())

spfa = SPFA(spfa_graph)
third_path: Path = spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(third_path)
print(spfa.get_counter())
