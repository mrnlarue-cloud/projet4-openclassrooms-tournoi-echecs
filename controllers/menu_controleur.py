# Import du module json pour lire le contenu du fichier tournois.json.
import json

# Import de Path pour construire un chemin fiable vers le fichier JSON,
# quel que soit l'endroit depuis lequel le programme est lancé.
from pathlib import Path

# Import des fonctions de la vue du menu principal.
# Le contrôleur les utilise pour afficher le menu
# et récupérer la saisie de l'utilisateur.
from views.menu_view import afficher_menu_principal, demander_choix

# Import de la vue chargée d'afficher les tournois enregistrés.
# Le contrôleur lui transmettra la liste des noms à afficher.
from views.tournoi_view import afficher_tournois_enregistres


# Cette fonction lit le fichier JSON des tournois
# et récupère uniquement les noms des tournois enregistrés.
# Elle renvoie une liste de chaînes de caractères.
def recuperer_noms_tournois():
    # On remonte jusqu'au dossier racine du projet,
    # puis on construit le chemin vers le fichier tournois.json.
    dossier_projet = Path(__file__).resolve().parent.parent
    chemin_fichier = dossier_projet / "donnees_tournoi" / "tournois.json"

    # Si le fichier n'existe pas, on renvoie une liste vide
    # pour éviter une erreur et permettre au programme de continuer.
    if not chemin_fichier.exists():
        return []

    # On ouvre le fichier en lecture pour récupérer son contenu JSON.
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    # Cette liste va contenir uniquement les noms des tournois.
    noms_tournois = []

    # Chaque élément du fichier JSON représente un tournoi.
    # On récupère la valeur associée à la clé "nom".
    # Si jamais le nom manque, on met un texte par défaut.
    for tournoi in donnees:
        noms_tournois.append(tournoi.get("nom", "Tournoi sans nom"))

    return noms_tournois


# Cette fonction pilote le menu principal.
# Elle affiche le menu, récupère le choix saisi
# puis décide quelle action lancer.
def lancer_menu_principal():
    afficher_menu_principal()
    choix_utilisateur = demander_choix()

    # Choix 1 : la fonctionnalité sera développée plus tard.
    if choix_utilisateur == "1":
        print("Création de tournoi : fonctionnalité non encore disponible.")

    # Choix 2 : la fonctionnalité sera développée plus tard.
    elif choix_utilisateur == "2":
        print("Chargement de tournoi : fonctionnalité non encore disponible.")

    # Choix 3 : on lit les tournois enregistrés
    # puis on demande à la vue de les afficher.
    elif choix_utilisateur == "3":
        noms_tournois = recuperer_noms_tournois()
        afficher_tournois_enregistres(noms_tournois)

    # Choix 4 : on affiche simplement un message de sortie.
    elif choix_utilisateur == "4":
        print("Fermeture du programme.")

    # Si la saisie ne correspond à aucun choix prévu,
    # on informe l'utilisateur que son entrée est invalide.
    else:
        print("Choix invalide.")
