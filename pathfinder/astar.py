
from pathfinder.city import City
from pathfinder.pathfinder import PathFinder
from pathfinder.path import Path

class AStar(PathFinder):
    def __init__(self, graph : dict[City, dict[City, int]], heuristics : dict[City, int]):
        self.graph = graph
        self.heuristics = heuristics

    def get_shortest_path(self, start : City, end : City) -> Path:
        checked = []
        to_check = [start]

        path_map = {
            start : [None, 0]
        }
        i = 0
        while len(to_check) != 0:
            i += 1
            # researching the most intesting city
            cities_cost : dict[City, int] = {x : path_map[x][1] for x in path_map if x in to_check}
            # get city with the lowest cost
            current : City = min(cities_cost.items(), key=lambda x: x[1] + self.heuristics[x[0]])[0]
            # for c in cities_cost:
            #     print(c.value, cities_cost[c] ,  cities_cost[c] + self.heuristics[c])
            # print( i , "->",current.value)
            to_check.remove(current)

            lenght : int = path_map[current][1]

            for neighbor in self.graph[current]:
                dist = self.graph[current][neighbor] + lenght
                if neighbor not in checked:
                    if neighbor not in path_map \
                        or path_map[neighbor][1] > dist:
                        path_map[neighbor] = [current, dist]
                    if neighbor not in to_check:
                        to_check.append(neighbor)
                    if neighbor == end:
                        to_check = []
                        break
            checked.append(current)

        return self._compute_path(path_map, end)