from ast import Import

from pathfinder.pathfinder import PathFinder


from pathfinder.pathfinder import PathFinder
from pathfinder.heuristics import heuristics

class AStar(PathFinder):
    def __init__(self, graph, heuristics):
        PathFinder.__init__(self, graph)
        self.heuristics = heuristics
    