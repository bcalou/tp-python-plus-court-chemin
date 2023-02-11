from pathfinder.pathfinder import *

class SPFA(PathFinder):
    def __init__(self, graph: Graph):
        super().__init__(graph)

    def _should_skip_city(self, city: City) -> bool:
        return False
    
    def _should_visit_city_when_met(self, city:City) -> bool:
        return False
    
    def _should_visit_city_when_weight_changed(self, city: City) -> bool:
        return True if city not in self._cities_to_visit else False
