from pathfinder.city import City

heuristics: dict[City, float] = {
    City.BORDEAUX: 47,
    City.DIJON: 15,
    City.LILLE: 25,
    City.PARIS: 25,
    City.LYON: 24,
    City.NANTES: 44,
    City.ORLEANS: 27,
    City.MARSEILLE: 39,
    City.STRASBOURG: 0,
    City.RENNES: 43,
    City.ROUEN: 31,
    City.TOULOUSE: 46
}