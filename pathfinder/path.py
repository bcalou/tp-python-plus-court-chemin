from typing import TypedDict

from pathfinder.city import *


class Path(TypedDict):
    total: float # distance ou le coût total du trajet
    steps: list[City] # une liste de ville `City` par lesquelles nous devons passer
