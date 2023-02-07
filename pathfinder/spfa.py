from pathfinder.pathfinder import PathFinder
from pathfinder.city import City
from pathfinder.graphs import Graph

class SPFA(PathFinder):

    # SPFA est le même algo que Dijkstra, mais on ne trie pas la liste des
    # villes à visiter par poid. On les prend dans le même ordre qu'on les a
    # ajoutées à la liste (FIFO).
    # On supprime donc la fonction de tri.
    def sort_visits(self) -> None:
        pass