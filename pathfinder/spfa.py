from pathfinder.pathfinder import Pathfinder
from pathfinder.city import City
from pathfinder.types import Path


class SPFA (Pathfinder):
    """
    La classe AStar implémente l'algorithme du même nom
    (https://fr.wikipedia.org/wiki/Algorithme_A*)
    """

    def explore_city(
        self,
        city: City,
        end: City, history: list[City]
         ) -> list[list[City]] | None:
        """
        Cette function explore chaque chemins depuis `start` et renvoit une
        liste de routes qui mènent à `end`
        """
        # Stocke les résultats
        results = []

        for destination, _ in self.graph[city].items():
            # Si la ville suivante est déjà présente dans l'historique
            # nous sommes dans une boucle, on ignore
            if destination in history:
                continue

            # On créer une copie de l'historique qui sera ensuite utilisé
            # pour chacune des villes voisines
            copy = self.copy_history(history)
            copy.append(city)

            # Si la destination est la fin, alors on rajoute cette solution
            # a la liste et on vérifie les autres chemins
            if destination == end:
                copy.append(end)
                results.append(copy)
                continue

            # On vérifie les autres ville voisines
            result = self.explore_city(destination, end, copy)

            # Si le résultats est None, la ville de destination n'a pas été
            # trouvée.
            if result is not None:
                # On stocke tout les résultats qui contienent `end`
                for route in result:
                    results.append(route)

        return results

    def count_cost(self, route: list[City]) -> float:
        """
        Renvoit le coût d'un chemin
        """
        cout = 0
        for index, city in enumerate(route):
            if index < len(route) - 1:
                cout += self.graph[city][route[index+1]]
        return cout

    def get_shortest_path(self, start: City, end: City) -> Path:
        """
        Applique l'algorithme de SPFA (?*)

        # * -> Je n'ai pas très bien compris l'algorithme SPFA, alors
        # j'ai tenté de développer l'algorithme avec une nouvelle
        # fonction, je ne sais pas qi il corresponds à 100% mais
        # il fonctionne.

        La fonction considère que la ville d'arrivé est présente et accéssible
        dans le `graph` passé à la création de l'objet Pathfinder.
        """

        # Explore tout les chemins partant de `start` et allant à `end`
        results = self.explore_city(start, end, [])

        # Trie les résultats en fonction du coût
        results = sorted(
            results,
            key=self.count_cost
        )

        return Path(total=self.count_cost(results[0]), steps=results[0])

    def copy_history(self, history: list[City]) -> list[City]:
        """
        Permet de copier correctement l'historique
        """
        if len(history) == 0:
            return []

        return history.copy()
