from typing import TypedDict, List
from .city import City

class Path(TypedDict):
    total: float
    steps: List[City]
