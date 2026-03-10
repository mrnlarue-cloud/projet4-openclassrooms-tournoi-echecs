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

    def ajouter_tour(self, tour):
        # Ajoute un tour dans la liste des tours
        self.tours.append(tour)

    def __str__(self):
        # La méthode spéciale __str__ sert à définir
        # ce qui doit s'afficher quand on utilise print()
        # sur un objet de la classe Tournoi.
        #
        # Exemple :
        # print(tournoi)
        #
        # Sans cette méthode, Python afficherait quelque chose
        # de peu lisible comme :
        # <models.tournoi.Tournoi object at 0x000001...>
        #
        # Grâce à __str__, on peut afficher une description
        # claire et compréhensible du tournoi.

        return (
            # f signifie "f-string".
            # Cela permet d'insérer des variables directement
            # dans une chaîne de texte avec des accolades {}.
            # self.nom correspond au nom du tournoi.
            f"Tournoi : {self.nom} | "
            # self.lieu correspond au lieu où se déroule le tournoi.
            f"Lieu : {self.lieu} | "
            # len(self.joueurs) compte le nombre d'éléments
            # dans la liste des joueurs inscrits au tournoi.
            f"Joueurs inscrits : {len(self.joueurs)} | "
            # len(self.tours) compte le nombre de tours
            # déjà enregistrés dans le tournoi.
            f"Tours joués : {len(self.tours)}"
        )
