from pathfinder.graphs import graph
from pathfinder.pathfinder import PathFinder
from pathfinder.city import City

pf = PathFinder(graph)
print(pf.get_shortest_path(City.BORDEAUX, City.LILLE))