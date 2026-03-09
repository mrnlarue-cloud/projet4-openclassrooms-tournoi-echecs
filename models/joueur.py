# Définition de la classe Joueur : classe sert à représenter un joueur du tournoi.
class Joueur:

    # Méthode appelée automatiquement quand on crée un nouvel objet Joueur.
    # Elle permet d'initialiser les informations du joueur.
    def __init__(self, prenom, nom, date_naissance, identifiant_national, classement):
        # Prénom du joueur
        self.prenom = prenom

        # Nom du joueur
        self.nom = nom

        # Date de naissance du joueur
        self.date_naissance = date_naissance

        # Identifiant national du joueur
        self.identifiant_national = identifiant_national

        # Classement du joueur
        self.classement = classement

    # Cette méthode permet de convertir l'objet Joueur en dictionnaire : utile pour sauvegarder en JSON.
    def to_dict(self):
        return {
            "prenom": self.prenom,
            "nom": self.nom,
            "date_naissance": self.date_naissance,
            "identifiant_national": self.identifiant_national,
            "classement": self.classement
        }

    # Le décorateur @classmethod indique que cette méthode travaille avec la classe
    # Cette méthode permet de recréer un objet Joueur à partir d'un dictionnaire.
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["prenom"],
            data["nom"],
            data["date_naissance"],
            data["identifiant_national"],
            data["classement"]
        )

    # Permet d'afficher le joueur de manière plus lisible avec un print().
    def __str__(self):
        return f"{self.prenom} {self.nom} - classement : {self.classement}"