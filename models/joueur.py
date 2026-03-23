class Joueur:
    """Représente un joueur du tournoi."""

    def __init__(self, prenom, nom, date_naissance, identifiant_national, classement):
        """Initialise un joueur avec ses informations."""
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        self.identifiant_national = identifiant_national
        self.classement = classement

    def to_dict(self):
        """Convertit le joueur en dictionnaire."""
        return {
            "prenom": self.prenom,
            "nom": self.nom,
            "date_naissance": self.date_naissance,
            "identifiant_national": self.identifiant_national,
            "classement": self.classement,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur à partir d'un dictionnaire."""
        return cls(
            data["prenom"],
            data["nom"],
            data["date_naissance"],
            data["identifiant_national"],
            data["classement"],
        )

    def __str__(self):
        """Retourne une représentation texte du joueur."""
        return f"{self.prenom} {self.nom} - classement : {self.classement}"