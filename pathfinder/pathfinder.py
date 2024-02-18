from pathfinder.graphs import Graph
from pathfinder.city import City
from pathfinder.types import Path
from pathfinder.types import Step


class Pathfinder():
    __processed_steps: list[Step] = []
    __processed_cities: list[City] = []
    __discovered_steps: list[Step] = []
    __discovered_cities: list[City] = []
    __start: City
    __end: City
    __current_step: Step

    def __init__(self, graph: Graph):
        self.__graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Return the path with the min cost to go from start to end point"""
        self.__start = start
        self.__current_step = {
            "city": self.__start,
            "origin": None,
            "bestCost": 0
        }
        self.__end = end

        self.__discovered_cities.append(self.__start)
        self.__discovered_steps.append(self.__current_step)

        while self.__end not in self.__processed_cities:
            self.__find_next_step()

        path: Path = self.__get_path_from_steps()
        self.__reset()
        return path

    def __find_next_step(self) -> None:
        """Discover cities around the actual one and compare
        discovered cities' cost. The lowest is the next city to visit"""
        self.__visit_neighbourhood()

        # Change the current city from discovered to processed
        self.__discovered_cities.remove(self.__current_step["city"])
        self.__discovered_steps.remove(self.__current_step)
        self.__processed_cities.append(self.__current_step["city"])
        self.__processed_steps.append(self.__current_step)

        shortest_path: Step = {
            "city": self.__current_step["city"],
            "origin": self.__current_step,
            "bestCost": float('inf')
        }

        # Compare the shortest path available from discovered cities
        for known_city in self.__discovered_steps:
            shortest_path = known_city if shortest_path["bestCost"] > \
                known_city["bestCost"] else shortest_path

        self.__current_step = shortest_path

    def __visit_neighbourhood(self) -> None:
        """Create or update infos about cities around the current one"""
        for city in self.__graph[self.__current_step["city"]]:
            # Ignore the city if it's already processed
            if city in self.__processed_cities:
                continue

            cost: float = self.__graph[self.__current_step["city"]][city]\
                + self.__current_step["bestCost"]

            # Update origin and cost if it's lower than the previous one
            if city in self.__discovered_cities:
                for known_step in self.__discovered_steps:
                    if known_step["city"] == city:
                        if known_step["bestCost"] > cost:
                            known_step["bestCost"] = cost
                            known_step["origin"] = self.__current_step

            # If it's a new city, create it's associated step (origin + cost)
            else:
                new_step: Step = {
                    "city": city,
                    "origin": self.__current_step,
                    "bestCost": cost
                }
                self.__discovered_cities.append(city)
                self.__discovered_steps.append(new_step)

    def __get_path_from_steps(self) -> Path:
        """Recreate the path going from end to start"""
        total_cost: float = float("inf")
        cities_on_path: list[City] = [self.__end]

        for step in self.__processed_steps:
            if step["city"] == self.__end:
                total_cost = step["bestCost"]
                origin: Step | None = step["origin"]
                while origin is not None and origin["city"] != self.__start:
                    cities_on_path.insert(0, origin["city"])
                    origin = origin["origin"]
                cities_on_path.insert(0, self.__start)

        path: Path = {"total": total_cost, "steps": cities_on_path}
        return path

    def __reset(self) -> None:
        """Clean lists used to explore the graph"""
        self.__processed_steps = []
        self.__processed_cities = []
        self.__discovered_steps = []
        self.__discovered_cities = []
