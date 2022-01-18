from pathfinder.city import City

graph = {
    City.TOULOUSE: {
        City.BORDEAUX: 14,
        City.MARSEILLE: 22,
        City.LYON: 28
    },
    City.MARSEILLE: {
        City.LYON: 18,
        City.TOULOUSE: 22 
    },
    City.BORDEAUX: {
        City.ORLEANS: 24,
        City.TOULOUSE: 14,
        City.LYON: 31,
        City.NANTES: 19 
    },
    City.LYON: {
        City.DIJON: 11,
        City.ORLEANS: 20,
        City.BORDEAUX: 31,
        City.TOULOUSE: 28,
        City.MARSEILLE: 18 
    },
    City.DIJON: {
        City.LYON: 11,
        City.ORLEANS: 15,
        City.PARIS: 16,
        City.STRASBOURG: 20 
    },
    City.ORLEANS: {
        City.DIJON: 15,
        City.LYON:  20,
        City.BORDEAUX: 24,
        City.NANTES: 16,
        City.ROUEN: 11,
        City.PARIS: 7 
    },
    City.NANTES: {
        City.BORDEAUX: 19,
        City.ORLEANS: 16,
        City.ROUEN: 19,
        City.RENNES: 6
    },
    City.RENNES: {
        City.NANTES: 6,
        City.ROUEN: 17 
    },
    City.PARIS: {
        City.DIJON: 16,
        City.ORLEANS: 7,
        City.ROUEN:  7,
        City.LILLE: 13,
        City.STRASBOURG: 26 
    },
    City.STRASBOURG: {
        City.DIJON: 20,
        City.PARIS: 26,
        City.LILLE: 29 
    },
    City.ROUEN: {
        City.RENNES: 17,
        City.NANTES: 19,
        City.ORLEANS: 11,
        City.PARIS: 7,
        City.LILLE: 12
    },
    City.LILLE: {
        City.ROUEN: 12,
        City.PARIS: 13,
        City.STRASBOURG: 29
    },
}