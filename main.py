from pathfinder.pathfinder import PathFinder
from pathfinder.spfa import SPFA
from pathfinder.graphs import spfa_graph
from pathfinder.city import City


BDXSTBG = SPFA(spfa_graph)

print(BDXSTBG.get_shortest_path(City.BORDEAUX,City.STRASBOURG))