from models.joueur import Joueur


class Match:
    """Représente un match entre deux joueurs."""

    def __init__(self, joueur_1, joueur_2, score_joueur_1=0, score_joueur_2=0):
        """Initialise un match avec deux joueurs et leurs scores."""
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.score_joueur_1 = score_joueur_1
        self.score_joueur_2 = score_joueur_2

    def to_dict(self):
        """Convertit le match en dictionnaire."""
        return {
            "joueur_1": self.joueur_1.to_dict(),
            "joueur_2": self.joueur_2.to_dict(),
            "score_joueur_1": self.score_joueur_1,
            "score_joueur_2": self.score_joueur_2,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un match à partir d'un dictionnaire."""
        return cls(
            Joueur.from_dict(data["joueur_1"]),
            Joueur.from_dict(data["joueur_2"]),
            data["score_joueur_1"],
            data["score_joueur_2"],
        )

    def __str__(self):
        """Retourne une représentation texte du match."""
        return (
            f"{self.joueur_1.prenom} {self.joueur_1.nom} "
            f"vs "
            f"{self.joueur_2.prenom} {self.joueur_2.nom} "
            f"- score : {self.score_joueur_1} / {self.score_joueur_2}"
        )
