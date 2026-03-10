# Import des classes du projet.
# Ces imports permettent d'utiliser les modèles définis dans le dossier models.

# Import de la classe Joueur.
# Cette classe représente un joueur du tournoi.
from models.joueur import Joueur

# Import de la classe Match.
# Cette classe représente un match entre deux joueurs.
from models.match import Match

# Import de la classe Tournoi.
# Cette classe représente l'objet principal qui regroupe joueurs et tours.
from models.tournoi import Tournoi

from models.tour import Tour

# Création d'objets Joueur.
# Chaque objet représente un joueur avec ses informations.

joueur_1 = Joueur(
    "Alice",
    "Martin",
    "01/01/1990",
    "AB12345",
    1200,
)

joueur_2 = Joueur(
    "Bob",
    "Durand",
    "02/02/1992",
    "CD67890",
    1150,
)


# Création d'un objet Match.
# Le match relie deux objets Joueur et enregistre leur score.
match_test = Match(joueur_1, joueur_2, 1, 0)


# Création d'un objet Tournoi.
# Cet objet représente un tournoi et contiendra les joueurs et les tours.
tournoi = Tournoi("Tournoi de Paris", "Paris", "01/01/2024", "Tournoi test")

tour1 = Tour("Tour 1")
tour1.ajouter_match(match_test)
tournoi.ajouter_tour(tour1)

tournoi.ajouter_joueur(joueur_1)
tournoi.ajouter_joueur(joueur_2)

# Affichage des objets créés.
# Les méthodes spéciales __str__ définies dans les classes
# permettent d'obtenir une représentation texte lisible.
print(joueur_1)
print(joueur_2)
print(match_test)
print(tournoi)
