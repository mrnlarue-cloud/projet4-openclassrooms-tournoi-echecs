# Définition de la classe Joueur.
# Représente un joueur participant au tournoi.
class Joueur:

    # Méthode appelée lors de la création d'un objet Joueur.
    # Elle initialise les attributs de l'objet avec les données du joueur.
    def __init__(self, prenom, nom, date_naissance, identifiant_national, classement):

        # Attribut contenant le prénom du joueur.
        self.prenom = prenom

        # Attribut contenant le nom du joueur.
        self.nom = nom

        # Attribut contenant la date de naissance du joueur.
        self.date_naissance = date_naissance

        # Identifiant unique du joueur dans le système.
        self.identifiant_national = identifiant_national

        # Classement du joueur utilisé pour les tournois.
        self.classement = classement

    def to_dict(self):
        # Convertit l'objet Joueur en dictionnaire Python.
        # Cette structure est compatible avec la sérialisation en JSON.

        return {
            # Chaque clé correspond à un attribut de l'objet.
            "prenom": self.prenom,
            "nom": self.nom,
            "date_naissance": self.date_naissance,
            "identifiant_national": self.identifiant_national,
            "classement": self.classement,
        }

    @classmethod
    def from_dict(cls, data):
        # @classmethod est un décorateur indiquant que la méthode
        # est liée à la classe et non à une instance existante.
        #
        # "cls" représente la classe Joueur.
        # Cela permet de créer un nouvel objet Joueur à partir d'un dictionnaire,
        # par exemple après lecture de données JSON.

        return cls(
            # On récupère les valeurs dans le dictionnaire
            # et on les passe au constructeur de la classe.
            data["prenom"],
            data["nom"],
            data["date_naissance"],
            data["identifiant_national"],
            data["classement"],
        )

    def __str__(self):
        # Définit la représentation texte de l'objet Joueur.
        # Utilisée lorsque l'objet est affiché.

        return f"{self.prenom} {self.nom} - classement : {self.classement}"
