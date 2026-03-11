# On importe datetime depuis le module datetime.
# C'est un module natif.
# Il permet de récupérer la date et l'heure actuelles.
from datetime import datetime

from .match import Match


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

    def to_dict(self):
        # Cette méthode transforme l'objet Tour en dictionnaire.
        # Le but est d'obtenir une structure simple que JSON pourra enregistrer.

        return {
            # On enregistre le nom du tour.
            "nom": self.nom,
            # On enregistre la date de début.
            # C'est déjà une chaîne de caractères ou None.
            "date_debut": self.date_debut,
            # On enregistre la date de fin.
            # C'est déjà une chaîne de caractères ou None.
            "date_fin": self.date_fin,
            # self.matchs contient des objets Match.
            # Or JSON ne sait pas enregistrer directement des objets Python.
            # On doit donc convertir chaque objet Match en dictionnaire.
            "matchs": [match.to_dict() for match in self.matchs],
        }

    @classmethod
    def from_dict(cls, data):
        # Cette méthode recrée un objet Tour à partir d'un dictionnaire.
        #
        # "cls" représente la classe Tour.
        # On l'utilise pour créer une nouvelle instance de Tour.

        # On crée d'abord un objet Tour avec son nom.
        tour = cls(data["nom"])

        # On remet la date de début depuis le dictionnaire.
        tour.date_debut = data["date_debut"]

        # On remet la date de fin depuis le dictionnaire.
        tour.date_fin = data["date_fin"]

        # data["matchs"] contient une liste de dictionnaires.
        # Chaque dictionnaire représente un match.
        # On doit donc reconstruire un objet Match pour chacun d'eux.
        tour.matchs = [Match.from_dict(match) for match in data["matchs"]]

        # On renvoie l'objet Tour entièrement reconstruit.
        return tour

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
