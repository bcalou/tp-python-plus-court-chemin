from typing import List, TypedDict
from pathfinder.city import City

class Path(TypedDict):
    total:float
    steps:list[City] | City