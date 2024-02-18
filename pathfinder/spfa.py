from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Path


class SPFA(Pathfinder):
    """SPFA algorithm ( variant of Bellman-Ford algorithm )
     implementation in Python.
    """

    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)
        self.iterations = 0
        self.current_index = 0

        # List of nodes in the graph, used to iterate over each node
        self.nodes = list(self.graph.keys())

    def _is_algorithm_done(self, unvisited_nodes: list, current_node: City,
                           end: City) -> bool:
        """
        The algorithm is done after n-1 iterations, where n is the number of
        nodes in the graph.

        :param unvisited_nodes: list
        :param current_node: City
        :param end: City
        :return: bool
        """
        return not self.iterations == len(self.graph.keys()) - 1

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Method to get the shortest path between two cities using SPFA
        algorithm.

        :param start: City
        :param end: City
        :return: Path
        """
        self.iterations = 0
        self.current_index = 0

        path = super().get_shortest_path(start, end)
        return path

    def _get_next_node(self, unvisited_nodes: list, current_node: City,
                       start: City) -> City:
        """
        In SPFA, the next node is the next node in the list of nodes.

        :param unvisited_nodes: list
        :param current_node: City
        :param start: City
        :return: City
        """

        self.current_index += 1
        # If index is greater than the number of nodes, this iteration is done
        if self.current_index >= len(self.nodes):
            self.current_index = 0
            self.iterations += 1
        node = self.nodes[self.current_index]
        while True:
            # If the total distance to the node is infinity it means we don't
            # know a path to it for now, so we skip it
            if self.paths_to_nodes[node]["total"] == float("inf"):
                self.current_index += 1
                node = self.nodes[self.current_index]
            else:
                break

        return self.nodes[self.current_index]

    def _update_unvisited_nodes(self, current_node, start, unvisited_nodes):
        pass  # No need to update unvisited nodes in SPFA
