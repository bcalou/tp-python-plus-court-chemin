from pathfinder.heuristics import heuristics
from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph, spfa_graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.spfa import SPFA


def main():
    dikjstra: Pathfinder = Pathfinder(graph)
    print(dikjstra.get_shortest_path(City.BORDEAUX, City.STRASBOURG)["total"])

    astar: AStar = AStar(graph, heuristics)
    print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)["total"])

    spfa: SPFA = SPFA(spfa_graph)
    print(spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG)["total"])
    

main()