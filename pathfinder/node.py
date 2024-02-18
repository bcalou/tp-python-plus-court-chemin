from pathfinder.city import City


class Node:

    def __init__(self, new_city: City) -> None:
        self.__city: City = new_city
        self.__distance: float = float("inf")
        self.__previous_city: City = new_city

    def get_distance(self) -> float:
        return self.__distance

    def get_city(self) -> City:
        return self.__city

    def get_previous_city(self) -> City:
        return self.__previous_node

    def set_distance(self, new_distance: float) -> None:
        self.__distance = new_distance

    def set_previous_city(self, new_city: City):
        self.__previous_node = new_city
