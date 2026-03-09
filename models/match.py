# Définition de la classe Match : représentation d'un match entre deux joueurs.

# Import de la classe Joueur : pour recréer les joueurs dans from_dict().
from models.joueur import Joueur


class Match:
    # Méthode appelée automatiquement quand on crée un nouvel objet Match.
    # Elle sert à initialiser les deux joueurs et leurs scores.
    def __init__(self, joueur_1, joueur_2, score_joueur_1=0, score_joueur_2=0):
        # Premier joueur du match
        self.joueur_1 = joueur_1

        # Deuxième joueur du match
        self.joueur_2 = joueur_2

        # Score du premier joueur
        self.score_joueur_1 = score_joueur_1

        # Score du deuxième joueur
        self.score_joueur_2 = score_joueur_2

    # Cette méthode permet de convertir l'objet Match en dictionnaire, utile our JSON plus tard.
    def to_dict(self):
        return {
            "joueur_1": self.joueur_1.to_dict(),
            "joueur_2": self.joueur_2.to_dict(),
            "score_joueur_1": self.score_joueur_1,
            "score_joueur_2": self.score_joueur_2
        }

    # Le décorateur @classmethod indique que cette méthode travaille avec la classe elle-même.
    # Cette méthode permet de recréer un match à partir d'un dictionnaire.
    @classmethod
    def from_dict(cls, data):
        return cls(
            Joueur.from_dict(data["joueur_1"]),
            Joueur.from_dict(data["joueur_2"]),
            data["score_joueur_1"],
            data["score_joueur_2"]
        )

    # Cette méthode permet d'afficher le match de manière plus lisible avec un print().
    def __str__(self):
        return (
            f"{self.joueur_1.prenom} {self.joueur_1.nom} "
            f"vs "
            f"{self.joueur_2.prenom} {self.joueur_2.nom} "
            f"- score : {self.score_joueur_1} / {self.score_joueur_2}"
        )