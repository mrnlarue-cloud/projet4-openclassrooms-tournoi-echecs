import json
from pathlib import Path

from models.tournoi import Tournoi
from views.menu_view import afficher_menu_principal, demander_choix
from views.tournoi_view import (
    afficher_choix_tournoi_invalide,
    afficher_details_tournoi_charge,
    afficher_menu_tournoi,
    afficher_message_tournoi_enregistre,
    afficher_tournoi_charge,
    afficher_tournois_enregistres,
    demander_choix_menu_tournoi,
    demander_informations_tournoi,
    demander_numero_tournoi,
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


# Cette fonction charge un tournoi existant à partir du fichier JSON.
# Elle affiche d'abord les tournois disponibles,
# demande à l'utilisateur lequel il veut charger,
# puis reconstruit l'objet Tournoi correspondant.
def charger_tournoi_existant():
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = recuperer_noms_tournois()

    # On affiche d'abord la liste des tournois disponibles
    # pour que l'utilisateur puisse choisir un numéro.
    afficher_tournois_enregistres(noms_tournois)

    # Si aucun tournoi n'est enregistré,
    # on arrête ici la fonction.
    if not tournois_enregistres:
        return

    numero_saisi = demander_numero_tournoi()

    # On vérifie d'abord que l'utilisateur a bien saisi un nombre.
    if not numero_saisi.isdigit():
        afficher_choix_tournoi_invalide()
        return

    numero_tournoi = int(numero_saisi)

    # On vérifie ensuite que le numéro correspond bien
    # à un tournoi présent dans la liste.
    if numero_tournoi < 1 or numero_tournoi > len(tournois_enregistres):
        afficher_choix_tournoi_invalide()
        return

    # Les listes Python commencent à l'indice 0,
    # donc on retire 1 au numéro choisi par l'utilisateur.
    donnees_tournoi = tournois_enregistres[numero_tournoi - 1]

    # On reconstruit ici un vrai objet Tournoi
    # à partir des données du fichier JSON.
    tournoi_charge = Tournoi.from_dict(donnees_tournoi)

    # On confirme d'abord que le tournoi a bien été chargé.
    afficher_tournoi_charge(tournoi_charge.nom)

    # On affiche ensuite ses informations principales
    # pour rendre le chargement plus concret pour l'utilisateur.
    afficher_details_tournoi_charge(tournoi_charge)

    # On affiche maintenant le menu des actions
    # disponibles pour le tournoi chargé.
    afficher_menu_tournoi()

    # On récupère le choix de l'utilisateur
    # dans le menu du tournoi.
    choix_tournoi = demander_choix_menu_tournoi()

    # Si l'utilisateur choisit 4,
    # on quitte simplement ce menu secondaire
    # pour revenir au menu principal.
    if choix_tournoi == "4":
        return

    # Pour l'instant, les autres choix ne sont pas encore développés.
    print("Cette action n'est pas encore disponible.")


# Cette fonction pilote le menu principal de l'application.
# Le menu reste affiché tant que l'utilisateur
# ne choisit pas explicitement de quitter.
# Selon le choix saisi, le contrôleur lance l'action adaptée.
def lancer_menu_principal():
    programme_en_cours = True

    while programme_en_cours:
        afficher_menu_principal()
        choix_utilisateur = demander_choix()

        # Choix 1 : création d'un nouveau tournoi.
        if choix_utilisateur == "1":
            creer_nouveau_tournoi()

        # Choix 2 : chargement d'un tournoi existant.
        elif choix_utilisateur == "2":
            charger_tournoi_existant()

        # Choix 3 : affichage de la liste des tournois enregistrés.
        elif choix_utilisateur == "3":
            noms_tournois = recuperer_noms_tournois()
            afficher_tournois_enregistres(noms_tournois)

        # Choix 4 : arrêt du programme.
        elif choix_utilisateur == "4":
            print("Fermeture du programme.")
            programme_en_cours = False

        # Si la saisie ne correspond à aucun choix prévu,
        # on affiche un message d'erreur simple.
        else:
            print("Choix invalide.")
