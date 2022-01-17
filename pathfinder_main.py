from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.pathfinder import PathFinder
from pathfinder.graph import graph, spfa_graph
from pathfinder.heuristics import heuristics

# pathfinder = PathFinder(graph)
pathfinder = PathFinder(spfa_graph)
pathfinder = AStar(graph, heuristics)

path = pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

print(path['total'])
for val in path["steps"]:
    print(val)