import unittest

from pathfinder.city import City
from pathfinder.pathfinder import Pathfinder
from pathfinder.graphs import graph

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 57,
      "steps": [City.BORDEAUX, City.ORLEANS, City.PARIS, City.STRASBOURG]
    }
  },
  {
    "start": City.STRASBOURG,
    "end": City.BORDEAUX,
    "path": {
      "total": 57,
      "steps": [City.STRASBOURG, City.PARIS, City.ORLEANS, City.BORDEAUX]
    }
  },
  {
    "start": City.LILLE,
    "end": City.TOULOUSE,
    "path": {
      "total": 58,
      "steps": [
        City.LILLE,
        City.PARIS,
        City.ORLEANS,
        City.BORDEAUX,
        City.TOULOUSE
      ]
    }
  },
  {
    "start": City.LILLE,
    "end": City.NANTES,
    "path": {
      "total": 31,
      "steps": [City.LILLE, City.ROUEN, City.NANTES]
    }
  },
  {
    "start": City.LYON,
    "end": City.MARSEILLE,
    "path": {
      "total": 18,
      "steps": [City.LYON, City.MARSEILLE]
    }
  }
]


class TestPathfinder(unittest.TestCase):
    def test_pathfinder(self):
        pathfinder = Pathfinder(graph)

        for test in tests:
            print("test")
            result = pathfinder.get_shortest_path(test["start"], test["end"])

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
