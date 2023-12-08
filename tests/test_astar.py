import unittest

from pathfinder.city import City
from pathfinder.astar import AStar
from pathfinder.graphs import graph
from pathfinder.heuristics import heuristics

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 59,
      "steps": [City.BORDEAUX, City.ORLEANS, City.DIJON, City.STRASBOURG]
    }
  },
  {
    "start": City.LILLE,
    "end": City.STRASBOURG,
    "path": {
      "total": 29,
      "steps": [City.LILLE, City.STRASBOURG]
    }
  },
  {
    "start": City.RENNES,
    "end": City.STRASBOURG,
    "path": {
      "total": 50,
      "steps": [City.RENNES, City.ROUEN, City.PARIS, City.STRASBOURG]
    }
  }
]


class TestAStar(unittest.TestCase):
    def test_a_star(self):
        astar = AStar(graph, heuristics)

        for test in tests:
            result = astar.get_shortest_path(test["start"], test["end"])

            self.assertEqual(
                result["total"],
                test["path"]["total"],
                f"Distance from {test['start']} to {test['end']} is wrong \
                (expected: {test['path']['total']}, got: {result['total']})"
            )

            self.assertEqual(
                result["steps"],
                test["path"]["steps"],
                f"Steps from {test['start']} to {test['end']} are incorrect \
                (expected: {test['path']['steps']}, got: {result['steps']})"
            )
