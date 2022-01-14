from pathfinder.astar import AStar
from pathfinder.astar import PathFinder
from pathfinder.city import City
from pathfinder.graph import graph, spfa_graph
from pathfinder.heuristics import heuristics

astar = PathFinder(spfa_graph)
print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))