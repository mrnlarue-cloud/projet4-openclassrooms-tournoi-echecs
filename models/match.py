# Import de la classe Joueur depuis le fichier joueur.py.
# Cet import est utile ici, car dans la méthode from_dict(),
# on devra recréer des objets Joueur à partir de dictionnaires.
from models.joueur import Joueur


# Définition de la classe Match.
# Cette classe sert à représenter un match entre deux joueurs,
# avec un score pour chacun.
class Match:

    # La méthode __init__ est appelée automatiquement
    # quand on crée un nouvel objet Match.
    # Elle sert à initialiser les joueurs et leurs scores.
    def __init__(self, joueur_1, joueur_2, score_joueur_1=0, score_joueur_2=0):
        # On stocke le premier joueur du match.
        self.joueur_1 = joueur_1

        # On stocke le deuxième joueur du match.
        self.joueur_2 = joueur_2

        # On stocke le score du premier joueur.
        # Par défaut, la valeur est 0 si rien n'est précisé.
        self.score_joueur_1 = score_joueur_1

        # On stocke le score du deuxième joueur.
        # Par défaut, la valeur est 0 si rien n'est précisé.
        self.score_joueur_2 = score_joueur_2

    # Cette méthode permet de transformer l'objet Match
    # en dictionnaire Python.
    # Les deux joueurs sont eux aussi transformés en dictionnaires
    # grâce à leur propre méthode to_dict().
    def to_dict(self):
        return {
            "joueur_1": self.joueur_1.to_dict(),
            "joueur_2": self.joueur_2.to_dict(),
            "score_joueur_1": self.score_joueur_1,
            "score_joueur_2": self.score_joueur_2,
        }

    # Le décorateur @classmethod indique que cette méthode
    # travaille avec la classe Match elle-même.
    # Cette méthode permet de recréer un objet Match
    # à partir d'un dictionnaire.
    # Comme les joueurs sont stockés sous forme de dictionnaires,
    # on utilise Joueur.from_dict() pour recréer de vrais objets Joueur.
    @classmethod
    def from_dict(cls, data):
        return cls(
            Joueur.from_dict(data["joueur_1"]),
            Joueur.from_dict(data["joueur_2"]),
            data["score_joueur_1"],
            data["score_joueur_2"],
        )

    # La méthode __str__ permet de définir un affichage lisible
    # quand on utilise print() sur un objet Match.
    # Cela permet de voir rapidement quels joueurs s'affrontent
    # et quel est le score enregistré.
    def __str__(self):
        return (
            f"{self.joueur_1.prenom} {self.joueur_1.nom} "
            f"vs "
            f"{self.joueur_2.prenom} {self.joueur_2.nom} "
            f"- score : {self.score_joueur_1} / {self.score_joueur_2}"
        )
