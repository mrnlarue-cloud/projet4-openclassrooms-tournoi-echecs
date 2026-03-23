import json
from pathlib import Path

from models.joueur import Joueur
from models.match import Match
from models.tour import Tour
from models.tournoi import Tournoi
from views.menu_view import afficher_menu_principal, demander_choix
from views.tournoi_view import (
    afficher_choix_tournoi_invalide,
    afficher_details_tournoi_charge,
    afficher_joueurs_tournoi,
    afficher_menu_tournoi,
    afficher_message_tournoi_enregistre,
    afficher_tournoi_charge,
    afficher_tournois_enregistres,
    afficher_tours_tournoi,
    demander_choix_menu_tournoi,
    demander_informations_joueur,
    demander_informations_tournoi,
    demander_numero_tournoi,
)


# Cette fonction construit le chemin vers le fichier JSON
# qui contient tous les tournois enregistrés.
def recuperer_chemin_fichier_tournois():
    dossier_projet = Path(__file__).resolve().parent.parent
    return dossier_projet / "donnees_tournoi" / "tournois.json"


# Cette fonction lit le fichier JSON
# et renvoie la liste des tournois enregistrés.
# Si le fichier n'existe pas, on renvoie simplement une liste vide.
def lire_tournois_enregistres():
    chemin_fichier = recuperer_chemin_fichier_tournois()

    if not chemin_fichier.exists():
        return []

    try:
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        print("Le fichier JSON est invalide.")
        return []


# Cette fonction enregistre un nouveau tournoi dans le JSON.
# On lit d'abord la liste actuelle, puis on y ajoute le tournoi créé.
def enregistrer_tournoi(tournoi):
    tournois_enregistres = lire_tournois_enregistres()
    tournois_enregistres.append(tournoi.to_dict())

    chemin_fichier = recuperer_chemin_fichier_tournois()

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


# Cette fonction remplace un tournoi déjà présent dans le JSON
# par sa version mise à jour.
def mettre_a_jour_tournoi_existant(numero_tournoi, tournoi):
    tournois_enregistres = lire_tournois_enregistres()

    # Le numéro affiché à l'utilisateur commence à 1,
    # alors que l'index Python commence à 0.
    tournois_enregistres[numero_tournoi - 1] = tournoi.to_dict()

    chemin_fichier = recuperer_chemin_fichier_tournois()

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


# Cette fonction récupère uniquement les noms des tournois
# pour permettre un affichage simple dans la vue.
def recuperer_noms_tournois():
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = []

    for tournoi in tournois_enregistres:
        noms_tournois.append(tournoi.get("nom", "Tournoi sans nom"))

    return noms_tournois


# Cette fonction crée un nouveau tournoi
# à partir des informations saisies par l'utilisateur.
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


# Cette fonction vérifie si le joueur saisi
# existe déjà dans le tournoi en cours.
def verifier_doublon_joueur(joueurs, informations_joueur):
    nom_saisi = informations_joueur["nom"].strip().lower()
    prenom_saisi = informations_joueur["prenom"].strip().lower()
    date_naissance_saisie = informations_joueur["date_naissance"].strip()
    identifiant_saisi = informations_joueur["identifiant_national"].strip().upper()

    for joueur in joueurs:
        nom_existant = joueur.nom.strip().lower()
        prenom_existant = joueur.prenom.strip().lower()
        date_naissance_existante = joueur.date_naissance.strip()
        identifiant_existant = joueur.identifiant_national.strip().upper()

        meme_nom = nom_existant == nom_saisi
        meme_prenom = prenom_existant == prenom_saisi
        meme_date_naissance = date_naissance_existante == date_naissance_saisie
        meme_identifiant = identifiant_existant == identifiant_saisi

        # Même identifiant national :
        # on considère qu'il s'agit du même joueur.
        if meme_identifiant:
            return (
                "Un joueur avec cet identifiant national "
                "existe déjà dans ce tournoi."
            )

        # Même nom + même prénom + même date de naissance :
        # on considère qu'il s'agit du même joueur.
        if meme_nom and meme_prenom and meme_date_naissance:
            return (
                "Un joueur avec le même nom, le même prénom "
                "et la même date de naissance existe déjà "
                "dans ce tournoi."
            )

    return None


# Cette fonction vérifie si le tournoi peut être démarré.
# Pour cette étape, il faut exactement 8 joueurs
# et aucun tour déjà enregistré.
def verifier_demarrage_tournoi(tournoi):
    if len(tournoi.joueurs) != 8:
        return False, "Le tournoi doit contenir exactement 8 joueurs pour démarrer."

    if len(tournoi.tours) > 0:
        return False, "Le tournoi a déjà été démarré."

    return True, ""


# Cette fonction trie les joueurs du meilleur classement
# vers le moins bon pour créer le premier tour.
def trier_joueurs_par_classement(joueurs):
    return sorted(joueurs, key=lambda joueur: joueur.classement, reverse=True)


# Cette fonction prépare le rapport des joueurs
# triés par classement
def afficher_rapport_joueurs_par_classement(tournoi):
    joueurs_tries = trier_joueurs_par_classement(tournoi.joueurs)

    afficher_joueurs_tournoi(
        joueurs_tries,
        "=== Rapport : joueurs par classement ===",
    )


# Cette fonction prépare le rapport
# de la liste des tours du tournoi.
def afficher_rapport_tours(tournoi):
    afficher_tours_tournoi(tournoi.tours)


# Cette fonction crée les 4 matchs du premier tour
# à partir de la liste triée des 8 joueurs.
def creer_matchs_premier_tour(joueurs_tries):
    matchs = []

    for index in range(0, len(joueurs_tries), 2):
        joueur_1 = joueurs_tries[index]
        joueur_2 = joueurs_tries[index + 1]

        match = Match(joueur_1, joueur_2)
        matchs.append(match)

    return matchs


# Cette fonction trie les joueurs par ordre alphabétique.
# On trie d'abord par nom, puis par prénom.
def trier_joueurs_par_ordre_alphabetique(joueurs):
    return sorted(
        joueurs,
        key=lambda joueur: (
            joueur.nom.lower(),
            joueur.prenom.lower(),
        ),
    )


# Cette fonction prépare le rapport des joueurs
# triés par ordre alphabétique
# puis envoie la liste triée à la vue.
def afficher_rapport_joueurs_ordre_alphabetique(tournoi):
    joueurs_tries = trier_joueurs_par_ordre_alphabetique(tournoi.joueurs)

    afficher_joueurs_tournoi(
        joueurs_tries,
        "=== Rapport : joueurs par ordre alphabétique ===",
    )


# Cette fonction démarre réellement le tournoi.
# Elle crée Tour 1, ses matchs, sauvegarde le tout
# puis affiche les appariements dans la console.
def demarrer_tournoi(numero_tournoi, tournoi):
    demarrage_autorise, message = verifier_demarrage_tournoi(tournoi)

    if not demarrage_autorise:
        print(message)
        return

    # On trie les joueurs par classement
    # avant de créer les matchs du premier tour.
    joueurs_tries = trier_joueurs_par_classement(tournoi.joueurs)

    # On crée le premier tour et on enregistre sa date de début.
    tour_1 = Tour("Tour 1")
    tour_1.demarrer()

    # On crée les matchs du premier tour
    # puis on les ajoute au tour.
    matchs = creer_matchs_premier_tour(joueurs_tries)

    for match in matchs:
        tour_1.ajouter_match(match)

    # On ajoute le tour au tournoi
    # puis on sauvegarde immédiatement dans le JSON.
    tournoi.ajouter_tour(tour_1)
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    print("\nLe tournoi a bien démarré.")
    print(f"{tour_1.nom} créé avec {len(tour_1.matchs)} matchs :")

    for numero_match, match in enumerate(tour_1.matchs, start=1):
        print(
            f"{numero_match}. "
            f"{match.joueur_1.prenom} {match.joueur_1.nom} "
            f"vs "
            f"{match.joueur_2.prenom} {match.joueur_2.nom}"
        )


# Cette fonction demande un score valide à l'utilisateur.
# Elle redemande tant que la valeur saisie n'est pas correcte.
def demander_score_valide(message):
    while True:
        saisie = input(message).strip()

        try:
            score = float(saisie)
        except ValueError:
            print("Veuillez saisir 0, 0.5 ou 1.")
            continue

        if score in [0, 0.5, 1]:
            return score

        print("Veuillez saisir 0, 0.5 ou 1.")


# Cette fonction permet de saisir les scores
# du dernier tour enregistré dans le tournoi.
def saisir_scores_tour(tournoi, numero_tournoi):
    if not tournoi.tours:
        print("Aucun tour n'a encore été créé.")
        return

    # On considère que le dernier tour de la liste
    # correspond au tour actuellement en cours.
    dernier_tour = tournoi.tours[-1]

    if not dernier_tour.matchs:
        print("Aucun match n'est enregistré dans ce tour.")
        return

    print(f"\n=== Saisie des scores - {dernier_tour.nom} ===")

    for match in dernier_tour.matchs:
        print(
            f"\nMatch : "
            f"{match.joueur_1.prenom} {match.joueur_1.nom} "
            f"vs "
            f"{match.joueur_2.prenom} {match.joueur_2.nom}"
        )

        # On demande les deux scores du match
        # puis on les enregistre dans l'objet Match.
        score_joueur_1 = demander_score_valide("Score du joueur 1 (0, 0.5, 1) : ")
        score_joueur_2 = demander_score_valide("Score du joueur 2 (0, 0.5, 1) : ")

        match.score_joueur_1 = score_joueur_1
        match.score_joueur_2 = score_joueur_2

    # Une fois tous les scores saisis,
    # on sauvegarde immédiatement le tournoi mis à jour.
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    print("\nLes scores du tour ont bien été enregistrés.")


# Cette fonction clôture le tour en cours.
# Elle vérifie d'abord que le tour existe,
# qu'il n'est pas déjà terminé
# et que tous les scores ont bien été saisis.
def cloturer_tour(tournoi, numero_tournoi):
    if not tournoi.tours:
        print("Aucun tour n'a encore été créé.")
        return

    dernier_tour = tournoi.tours[-1]

    if dernier_tour.date_fin is not None:
        print("Ce tour a déjà été clôturé.")
        return

    # Dans la logique actuelle, un match laissé à 0 / 0
    # est considéré comme non renseigné.
    for match in dernier_tour.matchs:
        if match.score_joueur_1 == 0 and match.score_joueur_2 == 0:
            print("Tous les scores du tour doivent être saisis avant la clôture.")
            return

    # On enregistre la date et l'heure de fin du tour.
    dernier_tour.terminer()

    # On sauvegarde immédiatement le tournoi mis à jour.
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    print(f"\n{dernier_tour.nom} a bien été clôturé.")


# Cette fonction construit la liste des rencontres déjà jouées
# dans les tours précédents.
# Chaque rencontre est stockée avec les identifiants nationaux
# triés pour que l'ordre des joueurs n'ait pas d'importance.
def recuperer_matchs_deja_joues(tournoi):
    matchs_deja_joues = []

    for tour in tournoi.tours:
        for match in tour.matchs:
            identifiant_joueur_1 = match.joueur_1.identifiant_national
            identifiant_joueur_2 = match.joueur_2.identifiant_national

            rencontre = sorted([identifiant_joueur_1, identifiant_joueur_2])
            matchs_deja_joues.append(tuple(rencontre))

    return matchs_deja_joues


# Cette fonction vérifie si deux joueurs
# se sont déjà affrontés dans le tournoi.
def match_deja_joue(joueur_1, joueur_2, matchs_deja_joues):
    rencontre = sorted([joueur_1.identifiant_national, joueur_2.identifiant_national])
    return tuple(rencontre) in matchs_deja_joues


# Cette fonction calcule le score total de chaque joueur
# sur l'ensemble des tours déjà joués.
def calculer_scores_joueurs(tournoi):
    scores_joueurs = {}

    for joueur in tournoi.joueurs:
        scores_joueurs[joueur.identifiant_national] = 0

    for tour in tournoi.tours:
        for match in tour.matchs:
            scores_joueurs[match.joueur_1.identifiant_national] += match.score_joueur_1
            scores_joueurs[match.joueur_2.identifiant_national] += match.score_joueur_2

    return scores_joueurs


# Cette fonction trie les joueurs selon leur score total.
# En cas d'égalité, on garde ensuite le meilleur classement.
def trier_joueurs_par_score_et_classement(tournoi, scores_joueurs):
    return sorted(
        tournoi.joueurs,
        key=lambda joueur: (
            scores_joueurs[joueur.identifiant_national],
            joueur.classement,
        ),
        reverse=True,
    )


# Cette fonction crée les matchs d'un tour suivant
# en essayant d'éviter les rencontres déjà jouées.
# On garde ici une logique simple et lisible.
def creer_matchs_sans_doublon(joueurs_tries, matchs_deja_joues):
    matchs = []
    identifiants_utilises = set()

    for joueur_1 in joueurs_tries:
        # Si le joueur a déjà été apparié dans ce tour,
        # on passe au suivant.
        if joueur_1.identifiant_national in identifiants_utilises:
            continue

        adversaire_trouve = None

        # On cherche d'abord un adversaire encore disponible
        # qui n'a pas déjà joué contre ce joueur.
        for joueur_2 in joueurs_tries:
            if joueur_2.identifiant_national == joueur_1.identifiant_national:
                continue

            if joueur_2.identifiant_national in identifiants_utilises:
                continue

            if not match_deja_joue(joueur_1, joueur_2, matchs_deja_joues):
                adversaire_trouve = joueur_2
                break

        # Si aucun adversaire inédit n'a été trouvé,
        # on prend le premier joueur encore libre.
        # Cela évite de bloquer complètement la création du tour.
        if adversaire_trouve is None:
            for joueur_2 in joueurs_tries:
                if joueur_2.identifiant_national == joueur_1.identifiant_national:
                    continue

                if joueur_2.identifiant_national in identifiants_utilises:
                    continue

                adversaire_trouve = joueur_2
                break

        # Si un adversaire a été trouvé,
        # on crée le match et on marque les deux joueurs comme utilisés.
        if adversaire_trouve is not None:
            match = Match(joueur_1, adversaire_trouve)
            matchs.append(match)

            identifiants_utilises.add(joueur_1.identifiant_national)
            identifiants_utilises.add(adversaire_trouve.identifiant_national)

    return matchs


# Cette fonction crée le tour suivant après clôture du précédent.
# Les joueurs sont triés par score total puis par classement,
# et les nouveaux matchs essaient d'éviter les doublons.
def creer_tour_suivant(tournoi, numero_tournoi):
    if not tournoi.tours:
        print("Aucun tour précédent. Impossible de créer un nouveau tour.")
        return

    dernier_tour = tournoi.tours[-1]

    if dernier_tour.date_fin is None:
        print("Le tour en cours doit être clôturé avant de créer le suivant.")
        return

    if len(tournoi.tours) >= tournoi.nombre_tours:
        print("Tous les tours du tournoi ont déjà été créés.")
        return

    # On calcule les scores cumulés des joueurs
    # pour préparer l'ordre du nouveau tour.
    scores_joueurs = calculer_scores_joueurs(tournoi)

    # On trie les joueurs selon leurs résultats
    # puis selon leur classement.
    joueurs_tries = trier_joueurs_par_score_et_classement(
        tournoi,
        scores_joueurs,
    )

    # On récupère toutes les rencontres déjà jouées
    # pour éviter de refaire les mêmes matchs.
    matchs_deja_joues = recuperer_matchs_deja_joues(tournoi)

    # On construit les nouveaux matchs du tour suivant.
    matchs_nouveaux = creer_matchs_sans_doublon(
        joueurs_tries,
        matchs_deja_joues,
    )

    numero_nouveau_tour = len(tournoi.tours) + 1
    nouveau_tour = Tour(f"Tour {numero_nouveau_tour}")
    nouveau_tour.demarrer()

    for match in matchs_nouveaux:
        nouveau_tour.ajouter_match(match)

    # On ajoute le nouveau tour au tournoi
    # puis on sauvegarde immédiatement dans le JSON.
    tournoi.ajouter_tour(nouveau_tour)
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    print(f"\n{nouveau_tour.nom} créé avec {len(nouveau_tour.matchs)} matchs.")


# Cette fonction gère le menu d'un tournoi chargé.
# Elle affiche les choix et lance l'action correspondante.
def gerer_menu_tournoi_charge(numero_tournoi, tournoi_charge):
    menu_tournoi_actif = True

    while menu_tournoi_actif:
        afficher_menu_tournoi()
        choix_tournoi = demander_choix_menu_tournoi()

        if choix_tournoi == "1":
            afficher_details_tournoi_charge(tournoi_charge)

        elif choix_tournoi == "2":
            if len(tournoi_charge.joueurs) >= 8:
                print("Ce tournoi contient déjà 8 joueurs.")
                continue

            informations_joueur = demander_informations_joueur()

            try:
                classement = int(informations_joueur["classement"])
            except ValueError:
                print("Le classement doit être un nombre entier.")
                continue

            message_doublon = verifier_doublon_joueur(
                tournoi_charge.joueurs,
                informations_joueur,
            )

            if message_doublon:
                print(message_doublon)
                continue

            joueur = Joueur(
                informations_joueur["prenom"],
                informations_joueur["nom"],
                informations_joueur["date_naissance"],
                informations_joueur["identifiant_national"],
                classement,
            )

            tournoi_charge.ajouter_joueur(joueur)
            mettre_a_jour_tournoi_existant(numero_tournoi, tournoi_charge)

            print(f'\nLe joueur "{joueur.prenom} {joueur.nom}" a bien été ajouté.')

        elif choix_tournoi == "3":
            afficher_rapport_joueurs_ordre_alphabetique(tournoi_charge)

        elif choix_tournoi == "4":
            afficher_rapport_joueurs_par_classement(tournoi_charge)

        elif choix_tournoi == "5":
            menu_tournoi_actif = False

        elif choix_tournoi == "6":
            demarrer_tournoi(numero_tournoi, tournoi_charge)

        elif choix_tournoi == "7":
            saisir_scores_tour(tournoi_charge, numero_tournoi)

        elif choix_tournoi == "8":
            cloturer_tour(tournoi_charge, numero_tournoi)

        elif choix_tournoi == "9":
            creer_tour_suivant(tournoi_charge, numero_tournoi)

        else:
            print("Choix invalide.")


# Cette fonction charge un tournoi existant à partir du JSON,
# reconstruit l'objet Tournoi
# puis ouvre le menu spécifique à ce tournoi.
def charger_tournoi_existant():
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = recuperer_noms_tournois()

    afficher_tournois_enregistres(noms_tournois)

    if not tournois_enregistres:
        return

    numero_saisi = demander_numero_tournoi()

    if not numero_saisi.isdigit():
        afficher_choix_tournoi_invalide()
        return

    numero_tournoi = int(numero_saisi)

    if numero_tournoi < 1 or numero_tournoi > len(tournois_enregistres):
        afficher_choix_tournoi_invalide()
        return

    donnees_tournoi = tournois_enregistres[numero_tournoi - 1]
    tournoi_charge = Tournoi.from_dict(donnees_tournoi)

    afficher_tournoi_charge(tournoi_charge.nom)
    gerer_menu_tournoi_charge(numero_tournoi, tournoi_charge)


# Cette fonction pilote le menu principal de l'application.
# Le programme continue tant que l'utilisateur ne choisit pas de quitter.
def lancer_menu_principal():
    programme_en_cours = True

    while programme_en_cours:
        afficher_menu_principal()
        choix_utilisateur = demander_choix()

        if choix_utilisateur == "1":
            creer_nouveau_tournoi()

        elif choix_utilisateur == "2":
            charger_tournoi_existant()

        elif choix_utilisateur == "3":
            noms_tournois = recuperer_noms_tournois()
            afficher_tournois_enregistres(noms_tournois)

        elif choix_utilisateur == "4":
            print("Fermeture du programme.")
            programme_en_cours = False

        else:
            print("Choix invalide.")
