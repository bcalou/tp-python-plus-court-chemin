from pathfinder.city import City


def sort_dict_by_value(dictionnary: dict[City, float]) -> dict[City, float]:
    """
    Trie un dictionnaire de ville en fonction de leur distance
    """
    # La fonction sorted accepte un fonction lambda dans la valeur `key`
    # cette fonction permet de décider en fonction de quel champ le 
    # dictionnaire doit être trié.
    return sorted(dictionnary.items(), key=lambda x: x[1])
