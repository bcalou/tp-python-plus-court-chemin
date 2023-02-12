from pathfinder.pathfinderClass import PathFinder
from pathfinder.graphs import graph, spfa_graph
from pathfinder.heuristics import heuristics
from pathfinder.city import City
from pathfinder.astar import Astar
from pathfinder.spfa import SPFA

def main():
    #pathfinder = PathFinder(graph)
    #pathfinder_path = pathfinder.get_shortest_path(City.LILLE, City.TOULOUSE)


    #astar = Astar(graph, heuristics)
    #pathfinder_path  = astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

    spfa = SPFA(spfa_graph)
    pathfinder_path = spfa.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

    print(pathfinder_path)

main()