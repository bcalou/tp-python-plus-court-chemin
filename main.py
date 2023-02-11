from pathfinder.pathfinderClass import PathFinder
from pathfinder.graphs import graph
from pathfinder.weights import weight
from pathfinder.city import City

def main():
    pathfinder = PathFinder(graph, weight)
    pathfinder_path = pathfinder.get_shortest_path(
      City.BORDEAUX, City.STRASBOURG
    )
    print(pathfinder_path)

main()