from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import Pathfinder, Path


class SPFA(Pathfinder):

    __visited: list[City]
    __queue: list[City]
    __paths: dict[City, Path]

    def __init__(self, graph: Graph) -> None:
        super().__init__(graph)

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Returns the shortest path, applying the SPFA implementation.
        """

        self.__visited = [start]
        self.__queue = [start]
        self.__paths = {
            start: {
                "total": 0,
                "steps": [start]
            }
        }

        while len(self.__queue) > 0:
            current_city: City = self.__queue.pop()
            self.__visited.remove(current_city)

            for neighbour, weight in self._graph[current_city].items():
                neighbour_path = self.__paths.get(neighbour)
                current_path: Path = self.__paths[current_city]

                if neighbour_path is None or \
                   (current_path["total"] + weight) < neighbour_path["total"]:

                    # Create the new shortest path to neighbour
                    new_path: Path = Pathfinder._copy_path(current_path)
                    new_path["steps"].append(neighbour)
                    new_path["total"] += weight
                    self.__paths[neighbour] = new_path

                    # Visited the neighbour, add it to the queue to visit its
                    # own neighbours.
                    if neighbour not in self.__visited:
                        self.__queue.append(neighbour)
                        self.__visited.append(neighbour)

        return self.__paths[end]
