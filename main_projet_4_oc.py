# Import du module json.
# Il permet d'afficher les données au format JSON de manière lisible.
import json

# Construit un chemin fiable vers le fichier JSON à partir du dossier du script.
from pathlib import Path

# Import des classes du projet.
# Ces imports permettent d'utiliser les modèles définis dans le dossier models.

# Import de la classe Joueur.
# Cette classe représente un joueur du tournoi.
from models.joueur import Joueur

# Import de la classe Match.
# Cette classe représente un match entre deux joueurs.
from models.match import Match

# Import de la classe Tour.
# Cette classe représente un tour contenant plusieurs matchs.
from models.tour import Tour

# Import de la classe Tournoi.
# Cette classe représente l'objet principal qui regroupe joueurs et tours.
from models.tournoi import Tournoi

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

# Création d'un objet Tour.
# Ce tour contiendra le match créé juste avant.
tour_1 = Tour("Tour 1")
tour_1.ajouter_match(match_test)

# Création d'un objet Tournoi.
# Cet objet représente un tournoi et contiendra les joueurs et les tours.
tournoi = Tournoi("Tournoi de Paris", "Paris", "01/01/2024", "Tournoi test")

# Ajout des joueurs au tournoi.
tournoi.ajouter_joueur(joueur_1)
tournoi.ajouter_joueur(joueur_2)

# Ajout du tour au tournoi.
tournoi.ajouter_tour(tour_1)

# Affichage des objets créés.
# Les méthodes spéciales __str__ définies dans les classes
# permettent d'obtenir une représentation texte lisible.
print(joueur_1)
print(joueur_2)
print(match_test)
print(tournoi)

# Test de sérialisation du tournoi complet.
# L'objectif est de vérifier que l'objet Tournoi
# peut être transformé en dictionnaire,
# puis reconstruit correctement à partir de ce dictionnaire.

# Conversion de l'objet tournoi en dictionnaire.
tournoi_dict = tournoi.to_dict()

# __file__ représente le fichier Python actuel.
# resolve() récupère son chemin complet.
# parent désigne le dossier dans lequel se trouve ce fichier.
dossier_projet = Path(__file__).resolve().parent

# On construit ensuite le chemin complet vers le fichier JSON.
chemin_fichier = dossier_projet / "donnees_tournoi" / "tournois.json"

# Ouverture du fichier en mode écriture.
# "w" remplace le contenu existant du fichier.
# encoding="utf-8" permet de bien gérer les accents.
with open(chemin_fichier, "w", encoding="utf-8") as fichier:
    # On enregistre une liste contenant le tournoi converti en dictionnaire.
    # On utilise une liste car le fichier est prévu pour stocker plusieurs tournois.
    json.dump([tournoi_dict], fichier, indent=4, ensure_ascii=False)

print("\nTournoi enregistré dans le fichier JSON.")

# Affichage du dictionnaire obtenu au format JSON lisible.
# json.dumps() transforme le dictionnaire en texte JSON.
# indent=4 ajoute des retours à la ligne et une indentation.
# ensure_ascii=False permet de conserver les accents lisibles.
print("\nTournoi converti en dictionnaire :")
print(json.dumps(tournoi_dict, indent=4, ensure_ascii=False))

# Ouverture du fichier JSON en mode lecture.
# "r" signifie lecture.
with open(chemin_fichier, "r", encoding="utf-8") as fichier:
    # json.load() lit le contenu du fichier JSON
    # et le transforme en données Python.
    donnees = json.load(fichier)

# Le fichier contient une liste de tournois.
# Ici, on récupère le premier tournoi de la liste.
tournoi_reconstruit = Tournoi.from_dict(donnees[0])

# Affichage du tournoi reconstruit.
# Cela permet de vérifier que l'objet recréé reste cohérent.
print("\nTournoi reconstruit :")
print(tournoi_reconstruit)

# Vérification plus précise de quelques éléments importants.
# On contrôle ici que les listes internes ont bien été restaurées.
print("\nVérifications après reconstruction :")
print(f"Nombre de joueurs : {len(tournoi_reconstruit.joueurs)}")
print(f"Nombre de tours : {len(tournoi_reconstruit.tours)}")
print(
    f"Nombre de matchs dans le premier tour : "
    f"{len(tournoi_reconstruit.tours[0].matchs)}"
)
