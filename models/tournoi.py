# Définition de la classe Tournoi.
# Cette classe représente un tournoi d'échecs.
class Tournoi:

    def __init__(self, nom, lieu, date_debut, description, nombre_tours=4):
        # Informations générales du tournoi.
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        # On ne peut pas déjà savoir.
        self.date_fin = None
        self.description = description

        # Nombre de tours (4 par défaut).
        self.nombre_tours = nombre_tours

        # Liste des joueurs inscrits.
        self.joueurs = []

        # Liste des tours joués.
        self.tours = []

    def ajouter_joueur(self, joueur):
        # Ajoute un joueur dans la liste des joueurs du tournoi
        self.joueurs.append(joueur)