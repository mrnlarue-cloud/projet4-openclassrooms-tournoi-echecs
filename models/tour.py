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
        # Enregistre la date et l'heure de fin du tour.
        self.date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def ajouter_match(self, match):
        # Ajoute un objet Match dans la liste des matchs du tour.
        self.matchs.append(match)

    def __str__(self):
        # Méthode spéciale utilisée lorsque l'on fait print(tour).
        # Elle définit la représentation texte de l'objet Tour.

        return (
            # f-string : permet d'insérer des variables dans une chaîne de texte.
            f"{self.nom} - début : {self.date_debut} - "
            f"fin : {self.date_fin} - "
            # len() compte le nombre de matchs dans la liste.
            f"nombre de matchs : {len(self.matchs)}"
        )
