from pathfinder.pathfinder import PathFinder
from pathfinder.graphs import graph
from pathfinder.city import City


BDXSTBG = PathFinder (graph)

print(BDXSTBG.get_shortest_path(City.BORDEAUX,City.STRASBOURG))