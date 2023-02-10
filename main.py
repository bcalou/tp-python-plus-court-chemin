from pathfinder.pathfinder import *

pathfinder = PathFinder(graph)

# pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

print(pathfinder.get_shortest_path(City.MARSEILLE, City.LILLE))