from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph
from pathfinder.city import City
from pathfinder.types import Path

pathfinder = Pathfinder(graph)

pathBT: Path = pathfinder.get_shortest_path(City.LYON, City.MARSEILLE)
print(pathBT)
