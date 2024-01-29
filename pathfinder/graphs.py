from pathfinder.city import City


Graph = dict[City, dict[City, float]]

graph: Graph = {
    City.PARIS: {
        City.ROUEN: 7,
        City.LILLE: 13,
        City.STRASBOURG: 26,
        City.DIJON: 16,
        City.ORLEANS: 7
    },
    City.LILLE: {
        City.PARIS: 13,
        City.STRASBOURG: 29,
        City.ROUEN: 12
    },
    City.STRASBOURG: {
        City.PARIS: 26,
        City.DIJON: 20,
        City.LILLE: 29
    },
    City.ROUEN: {
        City.LILLE: 12,
        City.PARIS: 7,
        City.ORLEANS: 11,
        City.NANTES: 19,
        City.RENNES: 17
    },
    City.RENNES: {
        City.ROUEN: 17,
        City.NANTES: 6
    },
    City.ORLEANS: {
        City.PARIS: 7,
        City.ROUEN: 11,
        City.NANTES: 16,
        City.BORDEAUX: 24,
        City.LYON: 20,
        City.DIJON: 15
    },
    City.DIJON: {
        City.STRASBOURG: 20,
        City.PARIS: 16,
        City.ORLEANS: 15,
        City.LYON: 11
    },
    City.NANTES: {
        City.RENNES: 6,
        City.ROUEN: 19,
        City.ORLEANS: 16,
        City.BORDEAUX: 19
    },
    City.LYON: {
        City.DIJON: 11,
        City.ORLEANS: 20,
        City.BORDEAUX: 31,
        City.TOULOUSE: 28,
        City.MARSEILLE: 18
    },
    City.BORDEAUX: {
        City.NANTES: 19,
        City.ORLEANS: 24,
        City.LYON: 31,
        City.TOULOUSE: 14
    },
    City.TOULOUSE: {
        City.BORDEAUX: 14,
        City.LYON: 28,
        City.MARSEILLE: 22
    },
    City.MARSEILLE: {
        City.TOULOUSE: 22,
        City.LYON: 18
    }
}

spfa_graph: Graph = {
    City.LILLE: {},
    City.ROUEN: {
        City.PARIS: -50
    },
    City.STRASBOURG: {
        City.LILLE: 50
    },
    City.PARIS: {
        City.STRASBOURG: -10,
        City.ORLEANS: -30
    },
    City.RENNES: {
        City.PARIS: 20
    },
    City.ORLEANS: {
        City.PARIS: 40,
        City.STRASBOURG: 15
    },
    City.NANTES: {
        City.ORLEANS: 10,
        City.RENNES: 20
    },
    City.DIJON: {
        City.STRASBOURG: 30
    },
    City.BORDEAUX: {
        City.NANTES: 50,
        City.TOULOUSE: 50
    },
    City.LYON: {
        City.DIJON: 20
    },
    City.TOULOUSE: {
        City.LYON: -75,
        City.MARSEILLE: 40
    },
    City.MARSEILLE: {
        City.LYON: 30
    }
}