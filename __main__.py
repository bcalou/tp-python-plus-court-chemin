from pathfinder.heuristics import heuristics
from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph, spfa_graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.spfa import SPFA


def main():
    dikjstra: Pathfinder = Pathfinder(graph)
    dikjstra_result = dikjstra.get_shortest_path(
        City.BORDEAUX, City.STRASBOURG
    )
    print(f"Dijkstra: {dikjstra_result['total']}")

    astar: AStar = AStar(graph, heuristics)
    astar_result = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
    print(f"Astar: {astar_result['total']}")

    spfa: SPFA = SPFA(spfa_graph)
    spfa_result = spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
    print(f"SPFA: {spfa_result['total']}")


main()
