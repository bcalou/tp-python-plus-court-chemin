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
    __next_step: Step

    def __init__(self, graph: Graph):
        self.__graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        self.__start = start
        self.__next_step = {
            "city": self.__start,
            "origin": None,
            "bestCost": 0
        }
        self.__end = end

        self.__discovered_cities.append(self.__start)
        self.__discovered_steps.append(self.__next_step)

        while self.__end not in self.__discovered_cities:
            self.__set_next_step(self.__next_step)

        path: Path = self.__get_path_from_steps()
        return path

    def __set_next_step(self, origin: Step) -> None:

        shortest_path: Step = {
                "city": origin["city"],
                "origin": origin,
                "bestCost": float('inf')
            }

        for city in self.__graph[origin["city"]]:
            if city in self.__processed_cities:
                continue

            new_step: Step = {
                "city": city,
                "origin": origin,
                "bestCost": self.__graph[origin["city"]][city] + origin["bestCost"]
            }

            self.__discovered_cities.append(city)
            self.__discovered_steps.append(new_step)

        self.__discovered_cities.remove(origin["city"])
        self.__discovered_steps.remove(origin)

        self.__processed_cities.append(origin["city"])
        self.__processed_steps.append(origin)

        #Compare the shortest path available from the cities next to this city, with the previous ones
        for known_city in self.__discovered_steps:
            shortest_path = known_city if shortest_path["bestCost"] > known_city["bestCost"] else shortest_path

        self.__next_step = shortest_path


    def __get_path_from_steps(self) -> Path:

        totalCost: float = float("inf")
        cities_on_path: list[City] = [self.__end]

        for step in self.__discovered_steps:
            if step["city"] == self.__end:
                totalCost = step["bestCost"]
                origin: Step | None = step["origin"]
                while origin["city"] != self.__start:
                    cities_on_path.insert(0, origin["city"])
                    origin = origin["origin"]
                cities_on_path.insert(0, self.__start)

        path: Path = {"total": totalCost, "steps": cities_on_path}
        return path
