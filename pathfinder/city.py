from enum import Enum

class City(Enum):
    LILLE = "Lille"
    ROUEN = "Rouen"
    STRASBOURG = "Strasbourg"
    PARIS = "Paris"
    RENNES = "Rennes"
    ORLEANS = "Orléans"
    DIJON = "Dijon"
    NANTES = "Nantes"
    BORDEAUX = "Bordeaux"
    LYON = "Lyon"
    TOULOUSE = "Toulouse"
    MARSEILLE = "Marseille"

    def __lt__(self, other):
        return self.value < other.value