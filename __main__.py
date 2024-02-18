from pathfinder.pathfinder import Pathfinder
from pathfinder.astar import AStar
from pathfinder.spfa import SPFA
from pathfinder.city import City
from pathfinder.graphs import graph
from pathfinder.graphs import spfa_graph
from pathfinder.heuristics import heuristics

def main():

    pathfinder: Pathfinder = Pathfinder(graph)
    astar: AStar = AStar(graph, heuristics)
    spfa: SPFA = SPFA(spfa_graph)

    print(spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

main()
