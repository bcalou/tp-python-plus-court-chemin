from pathfinder.pathfinder import Pathfinder
from pathfinder.types import Step
from pathfinder.types import Graph, Heuristic


class AStar(Pathfinder):
    __heuristics: Heuristic

    def __init__(self, graph: Graph, heuristics: Heuristic):
        Pathfinder.__init__(self, graph)
        self.__heuristics = heuristics

    def _lowest_cost_in_discoverd_cities(self) -> Step:
        """Find lowest cost with heuristic to determine the next step"""
        shortest_path: Step = {
            "city": self._current_step["city"],
            "origin": self._current_step,
            "bestCost": float('inf')
        }

        for known_city in self._discovered_steps:
            city_with_heuristics: float = known_city["bestCost"]\
                + self.__heuristics[known_city["city"]]
            actual_shortest_with_heuristics: float = shortest_path["bestCost"]\
                + self.__heuristics[shortest_path["city"]]

            shortest_path = known_city if actual_shortest_with_heuristics > \
                city_with_heuristics else shortest_path

        # A star must stop when end is discovered and not processed
        # TODO: change _can_continue_research instead
        if self._end in self._discovered_cities:
            for step in self._discovered_steps:
                if step["city"] == self._end:
                    self._discovered_cities.remove(self._end)
                    self._discovered_steps.remove(step)
                    self._processed_cities.append(self._end)
                    self._processed_steps.append(step)

        return shortest_path

    # Ce code ne fait pas ce qui est souhaité ?
    # def _can_continue_research(self) -> bool:
        # """Express the condition to continue explore new cities.
        # Here, the end city must not be discovered"""
        # return self._end not in self._discovered_cities
