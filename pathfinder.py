import graphlib
from pathfinder.pathfinder import PathFinder
from pathfinder.astar import AStar
from pathfinder.graph import graph
from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.path import Path

pathfinder = PathFinder(graphlib)
astar = AStar(graph, heuristics)
pathAStart = Path()

path: Path = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
print(path)