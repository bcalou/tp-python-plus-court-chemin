from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.types import Path


class Pathfinder():
    _graph: Graph
    _paths: list[Path]
    _parsed_cities: list[City]
    _start: City
    _end: City

    def __init__(self, graph: Graph) -> None:
        self._graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
            Calculates the shortest path from start to end
        """

        # We start all paths at the starting city
        # all subsequent paths will be copies of this one
        self._paths = [Path(total=0, steps=[start])]
        self._parsed_cities = []
        self._start = start
        self._end = end

        while True:
            optimal_path: Path = self._optimal_path()
            
            # We found the optimal path to end, we stop
            if optimal_path["steps"][-1] == end:
                return optimal_path
            
            # Else we evaluate all paths coming from our path and we repeat
            # we remove the last path as its not relevant anymore
            self._paths.remove(optimal_path)
            self.__parse_last_path_city(optimal_path)


    def __parse_last_path_city(self, path: Path):
        """
            Evaluates all distances from the path's last city and creates
            copies storing that information
        """

        last_city: City = path["steps"][-1]
        for (neighbour, distance) in self._graph[last_city].items():
            # Useless to go back to where we already have been !
            if neighbour in self._parsed_cities: continue

            copy: Path = Pathfinder._copy_path(path)
            copy["steps"].append(neighbour)
            copy["total"] += distance
            self._paths.append(copy)

        self._parsed_cities.append(last_city)

    def _optimal_path(self) -> Path:
        """Returns Dikjstra's definition of the optimal path"""

        # Reserve sort so that deletion is faster (optimisation)
        self._paths.sort(key=lambda path: path["total"], reverse=True)
        return self._paths[-1]


    @staticmethod
    def _copy_path(path: Path) -> Path:
        """Makes a copy of the given path"""
        copy: Path = Path(total=path["total"], steps=[])

        for city in path["steps"]:
            copy["steps"].append(city)

        return copy