# Import de la classe Joueur depuis le fichier joueur.py.
# Cela permet d'utiliser la classe dans ce fichier principal.
from models.joueur import Joueur

# Import de la classe Match depuis le fichier match.py.
# Cela permet de créer un match entre deux joueurs.
from models.match import Match


# Création d'un premier joueur de test.
# Ici, on crée un objet Joueur avec des données fixes
# pour vérifier que la classe fonctionne correctement.
joueur_test = Joueur(
    "Alice",
    "Martin",
    "01/01/1990",
    "AB12345",
    1200,
)

# Création d'un deuxième joueur de test.
# Ce joueur servira à tester la création d'un match.
joueur_2 = Joueur(
    "Bob",
    "Durand",
    "02/02/1992",
    "CD67890",
    1150,
)

# Création d'un match de test entre les deux joueurs.
# On donne ici un score de 1 pour le premier joueur
# et 0 pour le deuxième.
match_test = Match(joueur_test, joueur_2, 1, 0)

# Affichage des objets dans la console.
# Grâce aux méthodes __str__, l'affichage sera lisible.
print(joueur_test)
print(joueur_2)
print(match_test)