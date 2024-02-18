from pathfinder.graphs import graph, spfa_graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.heuristics import heuristics
from pathfinder.spfa import SPFA


def run_pathfinder():
    """
    Runs three different types of pathfinder algorythms over
    various graphs
    """

    print("Dijkstra:")
    pathfinder: Pathfinder = Pathfinder(graph)
    print(pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

    print("A*:")
    astar: AStar = AStar(graph, heuristics)
    print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

    print("SPFA:")
    spfa: SPFA = SPFA(spfa_graph)
    print(spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG))


run_pathfinder()
