import json
from pathlib import Path

from models.tournoi import Tournoi
from views.menu_view import afficher_menu_principal, demander_choix
from views.tournoi_view import (
    afficher_message_tournoi_enregistre,
    afficher_tournois_enregistres,
    demander_informations_tournoi,
)


# Cette fonction construit le chemin vers le fichier JSON
# qui contient les tournois enregistrés.
# On centralise ce chemin ici pour éviter de le réécrire partout.
def recuperer_chemin_fichier_tournois():
    dossier_projet = Path(__file__).resolve().parent.parent
    return dossier_projet / "donnees_tournoi" / "tournois.json"


# Cette fonction lit le contenu du fichier JSON
# et renvoie la liste des tournois enregistrés.
# Si le fichier n'existe pas encore, on renvoie une liste vide.
def lire_tournois_enregistres():
    chemin_fichier = recuperer_chemin_fichier_tournois()

    if not chemin_fichier.exists():
        return []

    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


# Cette fonction enregistre un nouveau tournoi dans le fichier JSON.
# Elle lit d'abord les tournois déjà présents,
# ajoute le nouveau tournoi converti en dictionnaire,
# puis réécrit la liste complète dans le fichier.
def enregistrer_tournoi(tournoi):
    tournois_enregistres = lire_tournois_enregistres()
    tournois_enregistres.append(tournoi.to_dict())

    chemin_fichier = recuperer_chemin_fichier_tournois()

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


# Cette fonction récupère uniquement les noms des tournois
# pour l'affichage dans la console.
def recuperer_noms_tournois():
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = []

    for tournoi in tournois_enregistres:
        noms_tournois.append(tournoi.get("nom", "Tournoi sans nom"))

    return noms_tournois


# Cette fonction gère la création d'un nouveau tournoi.
# La vue récupère les informations saisies,
# puis le contrôleur crée l'objet Tournoi
# et le sauvegarde dans le fichier JSON.
def creer_nouveau_tournoi():
    informations_tournoi = demander_informations_tournoi()

    tournoi = Tournoi(
        informations_tournoi["nom"],
        informations_tournoi["lieu"],
        informations_tournoi["date"],
        informations_tournoi["description"],
    )

    enregistrer_tournoi(tournoi)
    afficher_message_tournoi_enregistre(tournoi.nom)


# Cette fonction pilote le menu principal.
# Elle lit le choix saisi par l'utilisateur
# puis lance l'action correspondante.
def lancer_menu_principal():
    afficher_menu_principal()
    choix_utilisateur = demander_choix()

    if choix_utilisateur == "1":
        creer_nouveau_tournoi()

    elif choix_utilisateur == "2":
        print("Chargement de tournoi : fonctionnalité non encore disponible.")

    elif choix_utilisateur == "3":
        noms_tournois = recuperer_noms_tournois()
        afficher_tournois_enregistres(noms_tournois)

    elif choix_utilisateur == "4":
        print("Fermeture du programme.")

    else:
        print("Choix invalide.")
