from typing import TypedDict, List, Union

from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: List[City]


class DataToCity(TypedDict):
    previous_city: Union[City, None]
    distance: float


CitiesData = dict[City, DataToCity]
