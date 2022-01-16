from typing import TypedDict
from pathfinder.city import *

class Path(TypedDict):
    total: int
    steps: list[City]