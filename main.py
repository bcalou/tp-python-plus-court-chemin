from pathfinder.city import City
from pathfinder.pathfinder import PathFinder
from pathfinder.graphs import Graph, graph, spfa_graph
from pathfinder.types import Path

pathfinder = PathFinder(spfa_graph)

path: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

print(path["total"])
print(path["steps"])