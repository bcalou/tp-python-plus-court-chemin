from pathfinder.city import City

HeuristicsType = dict[City, float]

heuristics: HeuristicsType = {
    City.BORDEAUX: 47,
    City.DIJON: 15,
    City.LILLE: 25,
    City.ROUEN: 31,
    City.RENNES: 43,
    City.STRASBOURG: 0,
    City.PARIS: 25,
    City.ORLEANS: 27,
    City.NANTES: 44,
    City.LYON: 24,
    City.TOULOUSE: 46,
    City.MARSEILLE: 39
}