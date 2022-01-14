from pathfinder.city import *

graph = {
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
    City.LYON: {
        City.MARSEILLE: 18,
        City.TOULOUSE: 28,
        City.BORDEAUX: 31,
        City.ORLEANS: 20,
        City.DIJON: 11
    },
    City.MARSEILLE: {
        City.LYON: 18,
        City.TOULOUSE: 22
    },
    City.NANTES: {
        City.BORDEAUX: 19,
        City.RENNES: 6,
        City.ROUEN: 19,
        City.ORLEANS: 16
    },
    City.ORLEANS: {
        City.NANTES: 16,
        City.ROUEN: 11,
        City.PARIS: 7,
        City.DIJON: 15,
        City.LYON: 20,
        City.BORDEAUX: 24
    },
    City.PARIS: {
        City.ROUEN: 7,
        City.LILLE: 13,
        City.STRASBOURG: 26,
        City.DIJON: 16,
        City.ORLEANS: 7
    },
    City.RENNES: {
        City.ROUEN: 17,
        City.NANTES: 6
    },
    City.ROUEN: {
        City.RENNES: 17,
        City.LILLE: 12,
        City.PARIS: 7,
        City.ORLEANS: 11,
        City.NANTES: 19
    },
    City.STRASBOURG: {
        City.LILLE: 29,
        City.PARIS: 26,
        City.DIJON: 20
    },
    City.TOULOUSE: {
        City.BORDEAUX: 14,
        City.LYON: 28,
        City.MARSEILLE: 22
    },
}