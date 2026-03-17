import json
from pathlib import Path

from models.joueur import Joueur
from models.tournoi import Tournoi
from views.menu_view import afficher_menu_principal, demander_choix
from views.tournoi_view import (
    afficher_choix_tournoi_invalide,
    afficher_details_tournoi_charge,
    afficher_menu_tournoi,
    afficher_message_tournoi_enregistre,
    afficher_tournoi_charge,
    afficher_tournois_enregistres,
    afficher_joueurs_tournoi,
    demander_choix_menu_tournoi,
    demander_informations_tournoi,
    demander_numero_tournoi,
    demander_informations_joueur,
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


# Cette fonction met à jour un tournoi déjà enregistré
# dans le fichier JSON.
# Elle remplace les anciennes données du tournoi
# par les nouvelles données du tournoi modifié.
def mettre_a_jour_tournoi_existant(numero_tournoi, tournoi):
    tournois_enregistres = lire_tournois_enregistres()

    # On remplace dans la liste
    # le tournoi concerné par sa version mise à jour.
    tournois_enregistres[numero_tournoi - 1] = tournoi.to_dict()

    chemin_fichier = recuperer_chemin_fichier_tournois()

    # On réécrit ensuite tout le fichier JSON
    # avec la liste mise à jour.
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


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

    # On affiche les informations principales
    # du tournoi chargé.
    afficher_details_tournoi_charge(tournoi_charge)

    # On affiche ensuite le menu des actions
    # disponibles pour ce tournoi.
    afficher_menu_tournoi()

    # On récupère le choix de l'utilisateur
    # dans le menu du tournoi.
    choix_tournoi = demander_choix_menu_tournoi()

    # Choix 1 : réafficher les détails du tournoi.
    if choix_tournoi == "1":
        afficher_details_tournoi_charge(tournoi_charge)

    # Choix 2 : ajout d'un joueur au tournoi chargé.
    elif choix_tournoi == "2":
        # On demande d'abord les informations du joueur
        # à l'utilisateur dans la console.
        informations_joueur = demander_informations_joueur()

        # On crée ensuite un objet Joueur
        # à partir des données saisies.
        # L'ordre des arguments doit respecter
        # le constructeur de la classe Joueur.
        joueur = Joueur(
            informations_joueur["prenom"],
            informations_joueur["nom"],
            informations_joueur["date_naissance"],
            informations_joueur["identifiant_national"],
            int(informations_joueur["classement"]),
        )

        # On ajoute le joueur
        # à la liste des joueurs du tournoi chargé.
        tournoi_charge.joueurs.append(joueur)

        # On met immédiatement à jour
        # le tournoi existant dans le fichier JSON.
        mettre_a_jour_tournoi_existant(numero_tournoi, tournoi_charge)

        # Ce message confirme
        # que le joueur a bien été ajouté.
        print(f'Le joueur "{joueur.prenom} {joueur.nom}" a bien été ajouté.')

    # Choix 3 : affichage des joueurs du tournoi chargé.
    elif choix_tournoi == "3":
        # On affiche la liste des joueurs
        # déjà enregistrés dans ce tournoi.
        afficher_joueurs_tournoi(tournoi_charge.joueurs)

    # Choix 4 : retour simple au menu principal.
    elif choix_tournoi == "4":
        return

    # Si la saisie ne correspond à aucun choix prévu,
    # on affiche un message simple.
    else:
        print("Choix invalide.")


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
