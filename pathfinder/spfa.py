from pathfinder.pathfinder import *


class SPFA(PathFinder):
    def __init__(self, graph: Graph):
        super().__init__(graph)

    def _should_skip_city(self, city: City) -> bool:
        """Determine wether there is no need to visit a city. May vary
        depending on the algorithm used"""

        return False

    def _should_visit_city_when_met(self, city: City) -> bool:
        """Determine whether the algorithm should visit a city when it meets
        one. May vary depending on the algorithm used"""

        return False

    def _should_visit_city_when_weight_changed(self, city: City) -> bool:
        """Determine whether the algorithm should visit a city when its weight
        was updated. May vary depending on the algorithm used"""

        return True if city not in self._cities_to_visit else False
