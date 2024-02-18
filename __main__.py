from pathfinder.pathfinder import Pathfinder
from pathfinder.astar import AStar
from pathfinder.graphs import graph
from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.types import Path

pathfinder = Pathfinder(graph)
pathfinder_a = AStar(graph, heuristics)

# path_d: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
# print(f" Dijkstra : {path_d}")

path_a: Path = pathfinder_a.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(f" A* : {path_a}")
