from pathfinder.city import City
from pathfinder.pathfinder import PathFinder
from pathfinder.graphs import Graph, graph
from pathfinder.types import Path

pathfinder = PathFinder(graph)

path: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

print(path["total"])