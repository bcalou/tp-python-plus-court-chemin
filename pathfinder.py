from pathfinder.pathfinder import PathFinder
from pathfinder.graph import graph
from pathfinder.astar import AStar
from pathfinder.heuristics import heuristics


pathfinder = PathFinder(graph)
astar = AStar(graph, heuristics)
