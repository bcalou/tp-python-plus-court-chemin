from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph
from pathfinder.city import City

pathfinder = Pathfinder(graph)
print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))
