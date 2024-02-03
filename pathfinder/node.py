from pathfinder.city import City


class Node:

    def __init__(self, new_city: City) -> None:
        self.__name: City = new_city
        self.__distance: float = float("inf")
        self.__previous_node: City = new_city

    def get_distance(self) -> float:
        return self.__distance

    def get_name(self) -> City:
        return self.__name

    def get_previous_node(self) -> str:
        return self.__previous_node

    def set_distance(self, new_distance: float) -> None:
        self.__distance = new_distance

    def set_previous_node(self, new_city: City):
        self.__previous_node = new_city
