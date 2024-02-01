from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph
from pathfinder.city import City


def main():

    pathfinder: Pathfinder = Pathfinder(graph)

    print(pathfinder.get_shortest_path(City.PARIS, City.MARSEILLE))


main()
