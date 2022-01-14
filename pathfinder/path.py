from typing import TypedDict
from pathfinder.city import *

class Path(TypedDict):
    total: float
    steps: list[City]
