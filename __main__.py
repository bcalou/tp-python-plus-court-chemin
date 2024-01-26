from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph
from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.heuristics import heuristics

pathfinder = Pathfinder(graph)
print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

astar = AStar(graph, heuristics)
print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
