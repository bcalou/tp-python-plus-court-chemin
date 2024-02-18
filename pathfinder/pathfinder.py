from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path


class Pathfinder:
    """
    Base class for subsequent pathfinding algorithms. This class implements
    Dijkstra's algorithm.
    """

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.paths_to_nodes = {}

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Method to get the shortest path between two cities using Dijkstra's
        algorithm.

        :param start: City
        :param end: City
        :return: Path
        """

        # Initialize the paths to all nodes with infinity except the start node
        self.paths_to_nodes = {
            city: {"total": 0, "steps": [start]} if city == start
            else {"total": float("inf"), "steps": [start]}
            for city in self.graph
        }

        # Initialize the unvisited nodes list and remove the start node
        unvisited_nodes: list = list(self.graph.keys())
        unvisited_nodes.remove(start)

        current_node: City = start
        while self._is_algorithm_done(unvisited_nodes, current_node, end):
            self._update_unvisited_nodes(current_node, start, unvisited_nodes)

            # If distance to current node + distance to neighbor is less than
            # the total distance to the neighbor, update the total distance to
            # the neighbor and the steps to get there
            for neighbor, distance in self.graph[current_node].items():
                if (self.paths_to_nodes[current_node]["total"] +
                        distance < self.paths_to_nodes[neighbor]["total"]):
                    self.paths_to_nodes[neighbor]["total"] = \
                        self.paths_to_nodes[current_node]["total"] + distance
                    self.paths_to_nodes[neighbor]["steps"] = \
                        self.paths_to_nodes[current_node]["steps"] + [neighbor]

            current_node = self._get_next_node(unvisited_nodes,
                                               current_node, start)

        return self.paths_to_nodes[end]

    def _update_unvisited_nodes(self, current_node, start, unvisited_nodes):
        """
        Method to update the unvisited nodes list. In Dijkstra's algorithm, the
        current node is removed from the unvisited nodes list.

        :param current_node: City
        :param start: City
        :param unvisited_nodes: list
        :return: None
        """
        if current_node != start:
            unvisited_nodes.remove(current_node)

    def _is_algorithm_done(self, unvisited_nodes: list, current_node: City,
                           end: City) -> bool:
        """
        Dijkstra's algorithm is done when there are no more unvisited nodes.

        :param unvisited_nodes: list
        :param current_node: City
        :param end: City
        :return: bool
        """
        return bool(unvisited_nodes)

    def _get_next_node(self, unvisited_nodes: list, current_node: City,
                       start: City) -> City:
        """
        Method to get the next node to visit. The next node is the closest
        unvisited neighbor.

        :param unvisited_nodes:
        :param current_node:
        :param start:
        :return: City
        """

        # Create a list of all unvisited neighbors for the current node
        unvisited_neighbors = {neighbor: distance for neighbor, distance in
                               self.graph[current_node].items() if
                               neighbor in unvisited_nodes}

        # If unvisited_neighbors is empty, go back to start
        if not unvisited_neighbors:
            return start

        # Get the closest unvisited neighbor
        if unvisited_neighbors:
            current_node, _ = min(unvisited_neighbors.items(),
                                  key=lambda item: item[1])

        return current_node
