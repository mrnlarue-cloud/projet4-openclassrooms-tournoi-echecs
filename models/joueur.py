# Définition de la classe Joueur.
# Cette classe sert à représenter un joueur du tournoi.
class Joueur:

    # La méthode __init__ est appelée automatiquement
    # quand on crée un nouvel objet à partir de la classe Joueur.
    # Elle sert à donner des valeurs de départ à chaque attribut du joueur.
    def __init__(self, prenom, nom, date_naissance, identifiant_national, classement):
        # On stocke le prénom du joueur dans l'objet.
        self.prenom = prenom

        # On stocke le nom du joueur dans l'objet.
        self.nom = nom

        # On stocke la date de naissance du joueur.
        self.date_naissance = date_naissance

        # On stocke l'identifiant national du joueur.
        self.identifiant_national = identifiant_national

        # On stocke le classement du joueur.
        self.classement = classement

    # Cette méthode permet de transformer l'objet Joueur
    # en dictionnaire Python.
    # C'est utile pour préparer une future sauvegarde en JSON,
    # car le JSON ne sait pas enregistrer directement un objet personnalisé.
    def to_dict(self):
        return {
            "prenom": self.prenom,
            "nom": self.nom,
            "date_naissance": self.date_naissance,
            "identifiant_national": self.identifiant_national,
            "classement": self.classement,
        }

    # Le décorateur @classmethod indique que cette méthode
    # travaille avec la classe elle-même.
    # Ici, on l'utilise pour recréer un objet Joueur
    # à partir d'un dictionnaire.
    # "cls" représente la classe Joueur.
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["prenom"],
            data["nom"],
            data["date_naissance"],
            data["identifiant_national"],
            data["classement"],
        )

    # La méthode __str__ permet de définir
    # ce qui s'affiche quand on utilise print() sur un objet Joueur.
    # Sans cette méthode, Python afficherait quelque chose de peu lisible.
    def __str__(self):
        return f"{self.prenom} {self.nom} - classement : {self.classement}"