"""
Mail file for execution
"""

from pathfinder.astar import AStar
from pathfinder.city import City
from pathfinder.graphs import graph, spfa_graph
from pathfinder.heuristics import heuristics
from pathfinder.pathfinder import Pathfinder
from pathfinder.spfa import SPFA

dijkstra_pathfinder = Pathfinder(graph)
dijkstra_pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

astar_pathfinder = AStar(graph, heuristics)
astar_pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)

spfa_pathfinder = SPFA(spfa_graph)
spfa_pathfinder.get_shortest_path(City.BORDEAUX, City.STRASBOURG)
