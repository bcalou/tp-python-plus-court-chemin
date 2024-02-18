from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City


class SPFA (Pathfinder):
    """
    La classe AStar implémente l'algorithme du même nom
    (https://fr.wikipedia.org/wiki/Algorithme_A*)
    """

    def early_break(self, current_city: City, end: City) -> bool:
        """
        Cette fonction permet de quitter en avance la boucle pour les
        algorythmes compatibles.
        """
        # On n'arrete pas le parcours si on voit/on est sur l'arrivé.
        # car on peut trouver un autre chemin moins cher.
        return False
