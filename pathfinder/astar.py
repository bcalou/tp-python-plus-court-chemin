from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder


class AStar(Pathfinder):
    """A* algorithm implementation in Python."""

    def __init__(self, graph: Graph, heuristics: dict) -> None:
        super().__init__(graph)
        self.heuristics = heuristics

    def _is_algorithm_done(self, unvisited_nodes: list, current_node: City,
                           end: City) -> bool:
        """
        A* algorithm is done when the current node is the end node.

        :param unvisited_nodes: list
        :param current_node: City
        :param end: City
        :return: bool
        """
        return current_node != end

    def _get_next_node(self, unvisited_nodes: list, current_node: City,
                       start: City) -> City:

        # Heuristics are now taken into account to get the distance to the
        # neighbors
        unvisited_neighbors = {neighbor: distance + self.heuristics[neighbor]
                               for neighbor, distance in
                               self.graph[current_node].items() if
                               neighbor in unvisited_nodes}

        # If unvisited_neighbors is empty, go back to start
        if not unvisited_neighbors:
            return start

        # Return the closest unvisited neighbor
        if unvisited_neighbors:
            current_node, _ = min(unvisited_neighbors.items(),
                                  key=lambda item: item[1])

        return current_node
