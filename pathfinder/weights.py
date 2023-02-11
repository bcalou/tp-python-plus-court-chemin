from pathfinder.city import City
from pathfinder.types import CityInfo

Weight = dict[City, CityInfo]

weight: Weight = {
    City.BORDEAUX: {
        "distance" : float("inf")
    },
    City.DIJON: {
        "distance" : float("inf")
    },
    City.LILLE: {
        "distance" : float("inf")
    },
    City.ROUEN: {
        "distance" : float("inf")
    },
    City.STRASBOURG: {
        "distance" : float("inf")
    },
    City.LYON: {
        "distance" : float("inf")
    },
    City.TOULOUSE: {
        "distance" : float("inf")
    },
    City.NANTES: {
        "distance" : float("inf")
    },
    City.PARIS: {
        "distance" : float("inf")
    },
    City.ORLEANS: {
        "distance" : float("inf")
    },
    City.RENNES: {
        "distance" : float("inf")
    },
    City.MARSEILLE: {
        "distance" : float("inf")
    }
}