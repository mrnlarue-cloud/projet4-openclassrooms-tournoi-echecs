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
