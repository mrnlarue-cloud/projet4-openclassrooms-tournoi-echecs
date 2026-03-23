from datetime import datetime

from .match import Match


class Tour:
    """Représente un tour du tournoi."""

    def __init__(self, nom):
        """Initialise un tour avec son nom."""
        self.nom = nom
        self.date_debut = None
        self.date_fin = None
        self.matchs = []

    def demarrer(self):
        """Enregistre la date et l'heure de début du tour."""
        self.date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def terminer(self):
        """Enregistre la date et l'heure de fin du tour."""
        self.date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def ajouter_match(self, match):
        """Ajoute un match à la liste des matchs du tour."""
        self.matchs.append(match)

    def to_dict(self):
        """Convertit le tour en dictionnaire."""
        return {
            "nom": self.nom,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "matchs": [match.to_dict() for match in self.matchs],
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tour à partir d'un dictionnaire."""
        tour = cls(data["nom"])
        tour.date_debut = data["date_debut"]
        tour.date_fin = data["date_fin"]
        tour.matchs = [Match.from_dict(match) for match in data["matchs"]]
        return tour

    def __str__(self):
        """Retourne une représentation texte du tour."""
        return (
            f"{self.nom} - début : {self.date_debut} - "
            f"fin : {self.date_fin} - "
            f"nombre de matchs : {len(self.matchs)}"
        )