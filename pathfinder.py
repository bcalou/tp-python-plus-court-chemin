from pathfinder.pathfinder import PathFinder
from pathfinder.graph import graph
from pathfinder.city import City
from pathfinder.heuristics import heuristics
from pathfinder.astar import AStar

pathfinder = PathFinder(graph)
astar = AStar(graph, heuristics)

#print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))





