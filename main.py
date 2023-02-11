from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph
from pathfinder.heuristics import heuristics
from pathfinder.pathfinder import PathFinder

pathfinder: PathFinder = PathFinder(graph)
print(pathfinder.get_shortest_path(City.STRASBOURG, City.BORDEAUX))

astar = AStar(graph, heuristics)
print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
