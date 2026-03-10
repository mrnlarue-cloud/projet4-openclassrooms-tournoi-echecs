# Import de la classe Joueur depuis le fichier joueur.py.
# Cet import est nécessaire pour pouvoir recréer des objets Joueur
# à partir des dictionnaires dans la méthode from_dict().
from models.joueur import Joueur


# Définition de la classe Match.
# Cette classe représente un match entre deux joueurs avec leurs scores.
class Match:

    # Méthode appelée lors de la création d'un objet Match.
    # Elle initialise les deux joueurs et leurs scores.
    def __init__(self, joueur_1, joueur_2, score_joueur_1=0, score_joueur_2=0):

        # Joueurs participant au match.
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2

        # Scores des joueurs (0 par défaut si non précisé).
        self.score_joueur_1 = score_joueur_1
        self.score_joueur_2 = score_joueur_2

    def to_dict(self):
        # Transforme l'objet Match en dictionnaire Python.
        # Utile pour enregistrer les données (par exemple dans un fichier JSON).
        # Les objets Joueur sont eux aussi convertis en dictionnaires.
        return {
            "joueur_1": self.joueur_1.to_dict(),
            "joueur_2": self.joueur_2.to_dict(),
            "score_joueur_1": self.score_joueur_1,
            "score_joueur_2": self.score_joueur_2,
        }

    @classmethod
    def from_dict(cls, data):
        # @classmethod est un décorateur.
        # Il indique que cette méthode appartient à la classe Match
        # et non à une instance particulière de Match.
        #
        # "cls" représente la classe Match elle-même.
        # Cela permet de créer un nouvel objet Match à partir d'un dictionnaire.
        #
        # Les joueurs sont recréés grâce à la méthode Joueur.from_dict().

        return cls(
            Joueur.from_dict(data["joueur_1"]),
            Joueur.from_dict(data["joueur_2"]),
            data["score_joueur_1"],
            data["score_joueur_2"],
        )

    def __str__(self):
        # Définit l'affichage du match lorsque l'on fait print(match).

        return (
            # f-string : permet d'insérer des variables dans le texte.
            f"{self.joueur_1.prenom} {self.joueur_1.nom} "
            f"vs "
            f"{self.joueur_2.prenom} {self.joueur_2.nom} "
            f"- score : {self.score_joueur_1} / {self.score_joueur_2}"
        )