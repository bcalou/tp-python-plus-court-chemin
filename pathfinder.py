from pathfinder.pathfinder import *
from pathfinder.graph import *
from pathfinder.city import *

pathfinder = PathFinder(graph)
pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)