from typing import TypedDict
from .city import City

class Path(TypedDict):
    total : float
    steps : list[City]
    
    