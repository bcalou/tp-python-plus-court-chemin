from pathfinder.city import City
from pathfinder.graphs import Graph
from pathfinder.pathfinder import PathFinder


class AStar(PathFinder):
    heuristics: dict[City,float]
    def __init__(self, graph: Graph, heuristics: dict[City, float]):
        super().__init__(graph)
        self.heuristics = heuristics
        print("Class AStar Initialised")

    def get_next_city(self) -> City:
        """Rerturn next city if present in unchecked cities,
        else nearest city"""

        if self.end in self.unchecked_cities:
            return self.end
        else:
            return self.get_nearest_unchecked_city()


    def get_cost(self, city: City):
        # print(city)
        # print(self.get_path_distance(city) + self.heuristics[city])
        return (self.get_path_distance(city) + self.heuristics[city])