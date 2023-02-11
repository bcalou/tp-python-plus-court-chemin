from pathfinder.city import City

Graph = dict[City, dict[City, float]]
graph: Graph = {
    City.BORDEAUX: {
        City.NANTES: 19,
        City.ORLEANS: 24,
        City.LYON: 31,
        City.TOULOUSE: 14
    },
    City.DIJON: {
        City.STRASBOURG: 20,
        City.PARIS: 16,
        City.ORLEANS: 15,
        City.LYON: 11
    },
    City.LILLE: {
        City.ROUEN: 12,
        City.PARIS: 13,
        City.STRASBOURG: 29
    },
    City.RENNES: {
        City.ROUEN: 17,
        City.NANTES: 6,
    },
    City.NANTES: {
        City.ROUEN: 19,
        City.RENNES: 6,
        City.BORDEAUX: 19,
        City.ORLEANS: 16,
    },
    City.PARIS: {
        City.ROUEN: 7,
        City.LILLE: 13,
        City.ORLEANS: 7,
        City.STRASBOURG: 26,
        City.DIJON: 16,
    },
    City.ORLEANS: {
        City.ROUEN: 11,
        City.NANTES: 16,
        City.BORDEAUX: 24,
        City.DIJON: 15,
        City.LYON: 20,
        City.PARIS: 7
    },
    City.TOULOUSE: {
        City.BORDEAUX: 14,
        City.MARSEILLE: 22,
        City.LYON: 28,
    },
    City.MARSEILLE: {
        City.LYON: 18,
        City.TOULOUSE: 22,
    },
    City.LYON: {
        City.MARSEILLE: 18,
        City.TOULOUSE: 28,
        City.BORDEAUX: 31,
        City.DIJON: 11,
        City.ORLEANS: 20,
    },
    City.STRASBOURG: {
        City.DIJON: 20,
        City.PARIS: 26,
        City.LILLE: 29,
    },
    City.ROUEN: {
        City.RENNES: 17,
        City.NANTES: 19,
        City.PARIS: 7,
        City.ORLEANS: 11,
        City.LILLE: 12,
    },
}

spfa_graph: Graph = {
    City.BORDEAUX: {
        City.NANTES: 50,
        City.TOULOUSE: 50
    },
    City.DIJON: {
        City.STRASBOURG: 30,
    },
    City.LILLE: {
    },
    City.RENNES: {
        City.ROUEN: -50,
        City.PARIS: 20,
    },
    City.NANTES: {
        City.RENNES: 20,
        City.ORLEANS: 10,
    },
    City.PARIS: {
        City.LILLE: 50,
        City.ORLEANS: -30,
        City.STRASBOURG: -10,
    },
    City.ORLEANS: {
        City.PARIS: 40,
        City.STRASBOURG: 15,
    },
    City.TOULOUSE: {
        City.MARSEILLE: 40,
        City.LYON: -75,
    },
    City.MARSEILLE: {
        City.LYON: 30,
    },
    City.LYON: {
        City.DIJON: 20,
    },
    City.STRASBOURG: {
        City.LILLE: 50,
    },
    City.ROUEN: {
        City.PARIS: 10,
    },
}
