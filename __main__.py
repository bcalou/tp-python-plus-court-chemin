from pathfinder.graphs import graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.heuristics import heuristics


def run_pathfinder():
    pathfinder: Pathfinder = Pathfinder(graph)
    print("Dijkstra:")
    print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

    astar: AStar = AStar(graph, heuristics)
    print("A*:")
    print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))


run_pathfinder()
