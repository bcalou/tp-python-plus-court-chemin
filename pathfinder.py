from pathfinder.pathfinder import *

pathfinder = PathFinder(graph)

print(pathfinder.get_shortest_path(City.STRASBOURG, City.BORDEAUX))
