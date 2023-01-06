from pathfinder.graph import Graph
from pathfinder.types import Path
from pathfinder.city import City


class PathFinder:
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        toRet: Path = {"total": 0, "steps": []}

        # Magic

        return toRet


    class Ville:
        def __init__(self, nom: str) -> None:
            self.nom: str = nom
            self.previous: City | None = None
            self.cout: float = 0