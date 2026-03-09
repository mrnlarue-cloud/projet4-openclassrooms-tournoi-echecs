from models.joueur import Joueur
from models.match import Match

joueur_1 = Joueur("Alice", "Martin", "01/01/1990", "AB12345", 1200)
joueur_2 = Joueur("Bob", "Durand", "02/02/1992", "CD67890", 1150)

match_test = Match(joueur_1, joueur_2, 1, 0)

print(joueur_1)
print(joueur_2)
print(match_test)