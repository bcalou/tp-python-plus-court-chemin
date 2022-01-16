from pathfinder.pathfinder import PathFinder
from pathfinder.graph import graph
from pathfinder.city import City

pathfinder = PathFinder(graph)

pathfinder.get_shortest_path(City.BORDEAUX,City.STRASBOURG)