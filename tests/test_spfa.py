import unittest

from pathfinder.city import City
from pathfinder.spfa import SPFA
from pathfinder.graphs import spfa_graph

tests = [
  {
    "start": City.BORDEAUX,
    "end": City.STRASBOURG,
    "path": {
      "total": 15,
      "steps": [
        City.BORDEAUX,
        City.NANTES,
        City.RENNES,
        City.ROUEN,
        City.PARIS,
        City.ORLEANS,
        City.STRASBOURG
      ]
    }
  },
  {
    "start": City.NANTES,
    "end": City.LILLE,
    "path": {
      "total": 15,
      "steps": [
        City.NANTES,
        City.RENNES,
        City.ROUEN,
        City.PARIS,
        City.ORLEANS,
        City.STRASBOURG,
        City.LILLE
      ]
    }
  },
  {
    "start": City.BORDEAUX,
    "end": City.LYON,
    "path": {
      "total": -25,
      "steps": [City.BORDEAUX, City.TOULOUSE, City.LYON]
    }
  },
  {
    "start": City.NANTES,
    "end": City.ORLEANS,
    "path": {
      "total": -50,
      "steps": [City.NANTES, City.RENNES, City.ROUEN, City.PARIS, City.ORLEANS]
    }
  }
]


class TestSPFA(unittest.TestCase):
    def test_spfa(self):
        spfa = SPFA(spfa_graph)

        for test in tests:
            result = spfa.get_shortest_path(test["start"], test["end"])

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
