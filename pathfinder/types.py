from typing import TypedDict
from pathfinder.city import City


class Path(TypedDict):
    """Ce type représente l'objet qui contient la réponse au problème donné"""
    total: float
    steps: list[City]
