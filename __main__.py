from pathfinder.pathfinder import Pathfinder
from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph
from pathfinder.heuristics import heuristics

def main():

    pathfinder: Pathfinder = Pathfinder(graph)
    astar: AStar = AStar(graph, heuristics)

    print(astar.get_shortest_path(City.BORDEAUX, City.STRASBOURG))

main()
