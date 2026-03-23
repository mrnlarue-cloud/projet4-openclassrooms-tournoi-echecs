from .joueur import Joueur
from .tour import Tour


class Tournoi:
    """Représente un tournoi d'échecs."""

    def __init__(self, nom, lieu, date_debut, description, nombre_tours=4):
        """Initialise un tournoi avec ses informations principales."""
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = None
        self.description = description
        self.nombre_tours = nombre_tours
        self.joueurs = []
        self.tours = []

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur au tournoi."""
        self.joueurs.append(joueur)

    def ajouter_tour(self, tour):
        """Ajoute un tour au tournoi."""
        self.tours.append(tour)

    def to_dict(self):
        """Convertit le tournoi en dictionnaire."""
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "description": self.description,
            "nombre_tours": self.nombre_tours,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs],
            "tours": [tour.to_dict() for tour in self.tours],
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tournoi à partir d'un dictionnaire."""
        tournoi = cls(
            data["nom"],
            data["lieu"],
            data["date_debut"],
            data["description"],
            data["nombre_tours"],
        )
        tournoi.date_fin = data["date_fin"]
        tournoi.joueurs = [Joueur.from_dict(joueur) for joueur in data["joueurs"]]
        tournoi.tours = [Tour.from_dict(tour) for tour in data["tours"]]
        return tournoi

    def __str__(self):
        """Retourne une représentation texte du tournoi."""
        return (
            f"Tournoi : {self.nom} | "
            f"Lieu : {self.lieu} | "
            f"Joueurs inscrits : {len(self.joueurs)} | "
            f"Tours joués : {len(self.tours)}"
        )