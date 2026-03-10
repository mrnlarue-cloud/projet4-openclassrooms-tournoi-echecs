# On importe datetime depuis le module datetime.
# C'est un module natif.
# Il permet de récupérer la date et l'heure actuelles.
from datetime import datetime


class Tour:

    def __init__(self, nom):
        # Le nom du tour. Exemple : "Tour 1", "Tour 2"
        self.nom = nom

        # La date de début du tour.
        # Elle est vide (None) au départ.
        # Elle sera remplie quand on appellera la méthode démarrer().
        self.date_debut = None

        # La date de fin du tour.
        # Elle est vide (None) au départ.
        # Elle sera remplie quand on appellera la méthode terminer().
        self.date_fin = None

        # La liste des matchs de ce tour.
        # Elle est vide au départ.
        # On y ajoutera des matchs avec la méthode ajouter_match().
        self.matchs = []

    def demarrer(self):
        # datetime.now() récupère la date et l'heure de maintenant.
        # strftime() transforme cette date en texte lisible.
        # str = string = texte
        # f = format
        # time = temps
        # Donc strftime = "transforme le temps en texte avec ce format"
        # Les codes du format :
        # %d = jour
        # %m = mois
        # %Y = année
        # %H = heure
        # %M = minute
        # %S = seconde
        # Résultat final : "15/06/2025 14:30:05"
        self.date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def terminer(self):
        # Même chose que démarrer() mais pour la date de fin.
        # On enregistre la date et l'heure de maintenant.
        self.date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def ajouter_match(self, match):
        # On ajoute un match à la fin de la liste des matchs.
        # append() veut dire "ajouter à la fin de la liste".
        self.matchs.append(match)

    def __str__(self):
        # Cette méthode définit ce qui s'affiche quand on fait print(tour).
        # len(self.matchs) compte le nombre de matchs dans la liste.
        # Exemple d'affichage :
        # "Tour 1 - début : 15/06/2025 14:30:05 - fin : 15/06/2025 15:00:00 - nombre de matchs : 4"
        return (
            f"{self.nom} - début : {self.date_debut} - "
            f"fin : {self.date_fin} - "
            f"nombre de matchs : {len(self.matchs)}"
        )