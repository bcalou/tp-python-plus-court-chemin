# Classe Path qui est un typedict
# Variables :
#   - total : le coût total du chemin (float)
#   - path : le chemin (list[City])


from typing import TypedDict
from pathfinder.city import City

class Path(TypedDict):
    total: float
    steps: list[City]