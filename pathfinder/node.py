class Node:

    def __init__(self) -> None:
        self.__distance: float = float("inf")

    def get_distance(self) -> float:
        return self.__distance

    def set_distance(self, new_distance: float) -> None:
        self.__distance = new_distance
