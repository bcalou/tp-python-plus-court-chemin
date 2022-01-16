from typing import TypedDict

from pathfinder.city import *


class Path(TypedDict):
    total: float # distance ou coût total chemin
    steps: list[City] # liste de ville `City` 