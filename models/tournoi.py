from .joueur import Joueur
from .tour import Tour


# Définition de la classe Tournoi.
# Cette classe représente un tournoi d'échecs.
class Tournoi:

    def __init__(self, nom, lieu, date_debut, description, nombre_tours=4):
        # Informations principales du tournoi.
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut

        # La date de fin n'est pas connue au moment de la création du tournoi.
        self.date_fin = None

        self.description = description

        # Nombre de tours prévus dans le tournoi (4 par défaut).
        self.nombre_tours = nombre_tours

        # Liste des joueurs inscrits dans le tournoi.
        self.joueurs = []

        # Liste des tours joués pendant le tournoi.
        self.tours = []

    def ajouter_joueur(self, joueur):
        # Ajoute un objet Joueur dans la liste des joueurs du tournoi.
        self.joueurs.append(joueur)

    def ajouter_tour(self, tour):
        # Ajoute un objet Tour dans la liste des tours du tournoi.
        self.tours.append(tour)

    def to_dict(self):
        # Cette méthode transforme l'objet Tournoi en dictionnaire.
        # Le but est d'obtenir une structure simple compatible avec JSON.

        return {
            # On enregistre les informations simples du tournoi.
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "description": self.description,
            "nombre_tours": self.nombre_tours,
            # self.joueurs contient des objets Joueur.
            # On convertit donc chaque joueur en dictionnaire.
            "joueurs": [joueur.to_dict() for joueur in self.joueurs],
            # self.tours contient des objets Tour.
            # On convertit donc chaque tour en dictionnaire.
            "tours": [tour.to_dict() for tour in self.tours],
        }

    @classmethod
    def from_dict(cls, data):
        # Cette méthode recrée un objet Tournoi à partir d'un dictionnaire.
        # "cls" représente ici la classe Tournoi.

        # On recrée d'abord l'objet principal avec les données nécessaires
        # au constructeur __init__.
        tournoi = cls(
            data["nom"],
            data["lieu"],
            data["date_debut"],
            data["description"],
            data["nombre_tours"],
        )

        # La date de fin n'est pas dans le constructeur,
        # donc on la remet à part après la création de l'objet.
        tournoi.date_fin = data["date_fin"]

        # data["joueurs"] contient une liste de dictionnaires.
        # Chaque dictionnaire représente un joueur.
        # On reconstruit donc chaque objet Joueur.
        tournoi.joueurs = [Joueur.from_dict(joueur) for joueur in data["joueurs"]]

        # data["tours"] contient une liste de dictionnaires.
        # Chaque dictionnaire représente un tour.
        # On reconstruit donc chaque objet Tour.
        tournoi.tours = [Tour.from_dict(tour) for tour in data["tours"]]

        # On renvoie l'objet Tournoi complètement reconstruit.
        return tournoi

    def __str__(self):
        # Méthode spéciale appelée lorsque l'on fait print(tournoi).
        # Elle définit la représentation texte de l'objet Tournoi.

        return (
            # f-string : permet d'insérer des variables dans une chaîne de texte.
            f"Tournoi : {self.nom} | "
            f"Lieu : {self.lieu} | "
            # len() permet de compter le nombre d'éléments dans une liste.
            f"Joueurs inscrits : {len(self.joueurs)} | "
            f"Tours joués : {len(self.tours)}"
        )
