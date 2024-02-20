from pathfinder.city import City
from pathfinder.graphs import graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path

pathfinder = Pathfinder(graph)

path: Path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

print(path["total"])
print(path["steps"])
