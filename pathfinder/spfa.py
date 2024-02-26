"""
SPFA Pathfinder
"""

from pathfinder.city import City
from pathfinder.pathfinder import Pathfinder


class SPFA(Pathfinder):
    """Shortest Path Faster Algorithm"""

    def _get_next_city_to_visit(self) -> City:
        """Get the next city to visit"""

        # In SPFA, we don't care about ordering, just take the next one
        return self._cities_to_visit[0]

    def _is_finished(self) -> bool:
        """Return true if the algorithm has finished its job"""

        # In SPFA, visit all cities
        return len(self._cities_to_visit) == 0
