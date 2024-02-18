from pathfinder.types import Graph
from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.types import Step


class Pathfinder():
    _processed_steps: list[Step] = []
    _processed_cities: list[City] = []
    _discovered_steps: list[Step] = []
    _discovered_cities: list[City] = []
    _start: City
    _end: City
    _current_step: Step

    def __init__(self, graph: Graph):
        self._graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Return the path with the min cost to go from start to end point"""
        self._start = start
        self._current_step = {
            "city": self._start,
            "origin": None,
            "bestCost": 0
        }
        self._end = end

        self._discovered_cities.append(self._start)
        self._discovered_steps.append(self._current_step)

        while self._can_continue_research():
            self._find_next_step()

        path: Path = self._get_path_from_steps()
        self._reset()
        return path

    def _find_next_step(self) -> None:
        """Discover cities around the actual one and compare
        discovered cities' cost. The lowest is the next city to visit"""
        self._visit_neighbourhood()

        # Change the current city from discovered to processed
        self._discovered_cities.remove(self._current_step["city"])
        self._discovered_steps.remove(self._current_step)
        self._processed_cities.append(self._current_step["city"])
        self._processed_steps.append(self._current_step)

        self._current_step = self._lowest_cost_in_discoverd_cities()

    def _visit_neighbourhood(self) -> None:
        """Create or update infos about cities around the current one"""
        for city in self._graph[self._current_step["city"]]:
            # Ignore the city if it's already processed
            if city in self._processed_cities:
                continue

            cost: float = self._graph[self._current_step["city"]][city]\
                + self._current_step["bestCost"]

            # Update origin and cost if it's lower than the previous one
            if city in self._discovered_cities:
                for known_step in self._discovered_steps:
                    if known_step["city"] == city:
                        if known_step["bestCost"] > cost:
                            known_step["bestCost"] = cost
                            known_step["origin"] = self._current_step

            # If it's a new city, create it's associated step (origin + cost)
            else:
                new_step: Step = {
                    "city": city,
                    "origin": self._current_step,
                    "bestCost": cost
                }
                self._discovered_cities.append(city)
                self._discovered_steps.append(new_step)

    def _lowest_cost_in_discoverd_cities(self) -> Step:
        """Compare the costs to determine the lowest"""

        shortest_path: Step = {
            "city": self._current_step["city"],
            "origin": self._current_step,
            "bestCost": float('inf')
        }

        for known_city in self._discovered_steps:
            shortest_path = known_city if shortest_path["bestCost"] > \
                known_city["bestCost"] else shortest_path

        return shortest_path

    def _get_path_from_steps(self) -> Path:
        """Recreate the path going from end to start"""
        total_cost: float = float("inf")
        cities_on_path: list[City] = [self._end]

        for step in self._processed_steps:
            if step["city"] == self._end:
                total_cost = step["bestCost"]
                origin: Step | None = step["origin"]
                while origin is not None and origin["city"] != self._start:
                    cities_on_path.insert(0, origin["city"])
                    origin = origin["origin"]
                cities_on_path.insert(0, self._start)

        path: Path = {"total": total_cost, "steps": cities_on_path}
        return path

    def _can_continue_research(self) -> bool:
        """Express the condition to continue explore new cities.
        Here, the end city must not be processed"""
        return self._end not in self._processed_cities

    def _reset(self) -> None:
        """Clean lists used to explore the graph"""
        self._processed_steps = []
        self._processed_cities = []
        self._discovered_steps = []
        self._discovered_cities = []
