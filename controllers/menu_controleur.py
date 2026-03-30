import json
from pathlib import Path

from models.joueur import Joueur
from models.match import Match
from models.tour import Tour
from models.tournoi import Tournoi
from views.menu_view import afficher_menu_principal, afficher_message, demander_choix
from views.tournoi_view import (
    afficher_choix_tournoi_invalide,
    afficher_details_tournoi_charge,
    afficher_entete_saisie_scores,
    afficher_joueurs_tournoi,
    afficher_match_a_saisir,
    afficher_matchs_crees,
    afficher_matchs_tour,
    afficher_menu_tournoi,
    afficher_message_tournoi_enregistre,
    afficher_tournoi_charge,
    afficher_tournois_enregistres,
    afficher_tours_tournoi,
    demander_choix_menu_tournoi,
    demander_informations_joueur,
    demander_informations_tournoi,
    demander_numero_tour,
    demander_numero_tournoi,
    demander_score_valide,
    demander_continuer_saisie_scores,
)


def recuperer_chemin_fichier_tournois():
    """Construit le chemin du fichier JSON."""
    dossier_projet = Path(__file__).resolve().parent.parent
    return dossier_projet / "donnees_tournoi" / "tournois.json"


def lire_tournois_enregistres():
    """Lit les tournois enregistrés."""
    chemin_fichier = recuperer_chemin_fichier_tournois()

    if not chemin_fichier.exists():
        return []

    try:
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        afficher_message("Le fichier JSON est invalide.")
        return []


def enregistrer_tournoi(tournoi):
    """Enregistre un nouveau tournoi."""
    tournois_enregistres = lire_tournois_enregistres()
    tournois_enregistres.append(tournoi.to_dict())

    chemin_fichier = recuperer_chemin_fichier_tournois()
    chemin_fichier.parent.mkdir(parents=True, exist_ok=True)

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


def mettre_a_jour_tournoi_existant(numero_tournoi, tournoi):
    """Met à jour un tournoi existant."""
    tournois_enregistres = lire_tournois_enregistres()
    tournois_enregistres[numero_tournoi - 1] = tournoi.to_dict()

    chemin_fichier = recuperer_chemin_fichier_tournois()
    chemin_fichier.parent.mkdir(parents=True, exist_ok=True)

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


def recuperer_noms_tournois():
    """Récupère les noms des tournois."""
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = []

    for tournoi in tournois_enregistres:
        noms_tournois.append(tournoi.get("nom", "Tournoi sans nom"))

    return noms_tournois


def creer_nouveau_tournoi():
    """Crée un nouveau tournoi."""
    informations_tournoi = demander_informations_tournoi()

    tournoi = Tournoi(
        informations_tournoi["nom"],
        informations_tournoi["lieu"],
        informations_tournoi["date"],
        informations_tournoi["description"],
    )

    enregistrer_tournoi(tournoi)
    afficher_message_tournoi_enregistre(tournoi.nom)


def verifier_doublon_joueur(joueurs, informations_joueur):
    """Vérifie si le joueur existe déjà."""
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

        if meme_identifiant:
            return (
                "Un joueur avec cet identifiant national "
                "existe déjà dans ce tournoi."
            )

        if meme_nom and meme_prenom and meme_date_naissance:
            return (
                "Un joueur avec le même nom, le même prénom "
                "et la même date de naissance existe déjà "
                "dans ce tournoi."
            )

    return None


def verifier_demarrage_tournoi(tournoi):
    """Vérifie si le tournoi peut démarrer."""
    if len(tournoi.joueurs) != 8:
        return False, "Le tournoi doit contenir exactement 8 joueurs pour démarrer."

    if len(tournoi.tours) > 0:
        return False, "Le tournoi a déjà été démarré."

    return True, ""


def trier_joueurs_par_classement(joueurs):
    """Trie les joueurs par classement décroissant."""
    return sorted(joueurs, key=lambda joueur: joueur.classement, reverse=True)


def afficher_rapport_joueurs_par_classement(tournoi):
    """Affiche le rapport des joueurs par classement."""
    joueurs_tries = trier_joueurs_par_classement(tournoi.joueurs)

    afficher_joueurs_tournoi(
        joueurs_tries,
        "=== Rapport : joueurs par classement ===",
    )


def afficher_rapport_tours(tournoi):
    """Affiche le rapport des tours."""
    afficher_tours_tournoi(tournoi.tours)


def afficher_rapport_matchs_tour(tour):
    """Affiche le rapport des matchs d'un tour."""
    afficher_matchs_tour(tour)


def afficher_rapport_matchs_d_un_tour(tournoi):
    """Permet de choisir un tour puis d'afficher ses matchs."""
    if not tournoi.tours:
        afficher_message("Aucun tour n'est encore enregistré dans ce tournoi.")
        return

    afficher_tours_tournoi(tournoi.tours)
    numero_saisi = demander_numero_tour()

    if not numero_saisi.isdigit():
        afficher_message("Numéro de tour invalide.")
        return

    numero_tour = int(numero_saisi)

    if numero_tour < 1 or numero_tour > len(tournoi.tours):
        afficher_message("Numéro de tour invalide.")
        return

    tour_selectionne = tournoi.tours[numero_tour - 1]
    afficher_rapport_matchs_tour(tour_selectionne)


def creer_matchs_premier_tour(joueurs_tries):
    """Crée les matchs du premier tour."""
    matchs = []

    for index in range(0, len(joueurs_tries), 2):
        joueur_1 = joueurs_tries[index]
        joueur_2 = joueurs_tries[index + 1]
        match = Match(joueur_1, joueur_2)
        matchs.append(match)

    return matchs


def trier_joueurs_par_ordre_alphabetique(joueurs):
    """Trie les joueurs par ordre alphabétique."""
    return sorted(
        joueurs,
        key=lambda joueur: (
            joueur.nom.lower(),
            joueur.prenom.lower(),
        ),
    )


def afficher_rapport_joueurs_ordre_alphabetique(tournoi):
    """Affiche le rapport alphabétique des joueurs."""
    joueurs_tries = trier_joueurs_par_ordre_alphabetique(tournoi.joueurs)

    afficher_joueurs_tournoi(
        joueurs_tries,
        "=== Rapport : joueurs par ordre alphabétique ===",
    )


def demarrer_tournoi(numero_tournoi, tournoi):
    """Démarre le tournoi."""
    demarrage_autorise, message = verifier_demarrage_tournoi(tournoi)

    if not demarrage_autorise:
        afficher_message(message)
        return

    joueurs_tries = trier_joueurs_par_classement(tournoi.joueurs)

    tour_1 = Tour("Tour 1")
    tour_1.demarrer()

    matchs = creer_matchs_premier_tour(joueurs_tries)

    for match in matchs:
        tour_1.ajouter_match(match)

    tournoi.ajouter_tour(tour_1)
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    afficher_message("\nLe tournoi a bien démarré.")
    afficher_matchs_crees(tour_1)


def saisir_scores_tour(tournoi, numero_tournoi):
    """
    Saisit les scores du tour en cours avec sauvegarde progressive.

    Après chaque match validé, les scores sont enregistrés immédiatement
    dans le fichier JSON.

    Résultats acceptés :
    - 1 / 0
    - 0 / 1
    - 0.5 / 0.5

    Si l'utilisateur quitte avant la fin, les matchs déjà saisis restent
    enregistrés. Lors d'une reprise, les matchs déjà renseignés sont ignorés.
    """
    if not tournoi.tours:
        afficher_message("Aucun tour n'a encore été créé.")
        return

    dernier_tour = tournoi.tours[-1]

    if not dernier_tour.matchs:
        afficher_message("Aucun match n'est enregistré dans ce tour.")
        return

    afficher_entete_saisie_scores(dernier_tour.nom)

    scores_valides = {
        (1, 0),
        (0, 1),
        (0.5, 0.5),
    }

    for match in dernier_tour.matchs:
        if not (match.score_joueur_1 == 0 and match.score_joueur_2 == 0):
            continue

        afficher_match_a_saisir(match)

        score_joueur_1 = demander_score_valide("Score du joueur 1 (0, 0.5, 1) : ")
        score_joueur_2 = demander_score_valide("Score du joueur 2 (0, 0.5, 1) : ")

        if (score_joueur_1, score_joueur_2) not in scores_valides:
            afficher_message(
                "Résultat invalide. Les scores autorisés sont : "
                "1 / 0, 0 / 1 ou 0.5 / 0.5."
            )
            return

        match.score_joueur_1 = score_joueur_1
        match.score_joueur_2 = score_joueur_2

        mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

        continuer = demander_continuer_saisie_scores()

        if continuer == "non":
            afficher_message(
                "\nLes scores déjà saisis ont été enregistrés. "
                "Vous pourrez reprendre plus tard."
            )
            return

    afficher_message("\nLes scores du tour ont bien été enregistrés.")


def cloturer_tour(tournoi, numero_tournoi):
    """Clôture le tour en cours."""
    if not tournoi.tours:
        afficher_message("Aucun tour n'a encore été créé.")
        return

    dernier_tour = tournoi.tours[-1]

    if dernier_tour.date_fin is not None:
        afficher_message("Ce tour a déjà été clôturé.")
        return

    for match in dernier_tour.matchs:
        if match.score_joueur_1 == 0 and match.score_joueur_2 == 0:
            afficher_message(
                "Tous les scores du tour doivent être saisis avant la clôture."
            )
            return

    dernier_tour.terminer()
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    afficher_message(f"\n{dernier_tour.nom} a bien été clôturé.")


def recuperer_matchs_deja_joues(tournoi):
    """Récupère les rencontres déjà jouées."""
    matchs_deja_joues = []

    for tour in tournoi.tours:
        for match in tour.matchs:
            identifiant_joueur_1 = match.joueur_1.identifiant_national
            identifiant_joueur_2 = match.joueur_2.identifiant_national

            rencontre = sorted([identifiant_joueur_1, identifiant_joueur_2])
            matchs_deja_joues.append(tuple(rencontre))

    return matchs_deja_joues


def match_deja_joue(joueur_1, joueur_2, matchs_deja_joues):
    """Vérifie si deux joueurs se sont déjà rencontrés."""
    rencontre = sorted([joueur_1.identifiant_national, joueur_2.identifiant_national])
    return tuple(rencontre) in matchs_deja_joues


def calculer_scores_joueurs(tournoi):
    """Calcule les scores cumulés des joueurs."""
    scores_joueurs = {}

    for joueur in tournoi.joueurs:
        scores_joueurs[joueur.identifiant_national] = 0

    for tour in tournoi.tours:
        for match in tour.matchs:
            scores_joueurs[match.joueur_1.identifiant_national] += match.score_joueur_1
            scores_joueurs[match.joueur_2.identifiant_national] += match.score_joueur_2

    return scores_joueurs


def trier_joueurs_par_score_et_classement(tournoi, scores_joueurs):
    """Trie les joueurs par score puis classement."""
    return sorted(
        tournoi.joueurs,
        key=lambda joueur: (
            scores_joueurs[joueur.identifiant_national],
            joueur.classement,
        ),
        reverse=True,
    )


def creer_matchs_sans_doublon(joueurs_tries, matchs_deja_joues):
    """Crée les matchs d'un tour suivant."""
    matchs = []
    identifiants_utilises = set()

    for joueur_1 in joueurs_tries:
        if joueur_1.identifiant_national in identifiants_utilises:
            continue

        adversaire_trouve = None

        for joueur_2 in joueurs_tries:
            if joueur_2.identifiant_national == joueur_1.identifiant_national:
                continue

            if joueur_2.identifiant_national in identifiants_utilises:
                continue

            if not match_deja_joue(joueur_1, joueur_2, matchs_deja_joues):
                adversaire_trouve = joueur_2
                break

        if adversaire_trouve is None:
            for joueur_2 in joueurs_tries:
                if joueur_2.identifiant_national == joueur_1.identifiant_national:
                    continue

                if joueur_2.identifiant_national in identifiants_utilises:
                    continue

                adversaire_trouve = joueur_2
                break

        if adversaire_trouve is not None:
            match = Match(joueur_1, adversaire_trouve)
            matchs.append(match)

            identifiants_utilises.add(joueur_1.identifiant_national)
            identifiants_utilises.add(adversaire_trouve.identifiant_national)

    return matchs


def creer_tour_suivant(tournoi, numero_tournoi):
    """Crée le tour suivant."""
    if not tournoi.tours:
        afficher_message("Aucun tour précédent. Impossible de créer un nouveau tour.")
        return

    dernier_tour = tournoi.tours[-1]

    if dernier_tour.date_fin is None:
        afficher_message(
            "Le tour en cours doit être clôturé avant de créer le suivant."
        )
        return

    if len(tournoi.tours) >= tournoi.nombre_tours:
        afficher_message("Tous les tours du tournoi ont déjà été créés.")
        return

    scores_joueurs = calculer_scores_joueurs(tournoi)

    joueurs_tries = trier_joueurs_par_score_et_classement(
        tournoi,
        scores_joueurs,
    )

    matchs_deja_joues = recuperer_matchs_deja_joues(tournoi)

    matchs_nouveaux = creer_matchs_sans_doublon(
        joueurs_tries,
        matchs_deja_joues,
    )

    numero_nouveau_tour = len(tournoi.tours) + 1
    nouveau_tour = Tour(f"Tour {numero_nouveau_tour}")
    nouveau_tour.demarrer()

    for match in matchs_nouveaux:
        nouveau_tour.ajouter_match(match)

    tournoi.ajouter_tour(nouveau_tour)
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    afficher_message(
        f"\n{nouveau_tour.nom} créé avec {len(nouveau_tour.matchs)} matchs."
    )


def gerer_menu_tournoi_charge(numero_tournoi, tournoi_charge):
    """Gère le menu d'un tournoi chargé."""
    menu_tournoi_actif = True

    while menu_tournoi_actif:
        afficher_menu_tournoi()
        choix_tournoi = demander_choix_menu_tournoi()

        if choix_tournoi == "1":
            afficher_details_tournoi_charge(tournoi_charge)

        elif choix_tournoi == "2":
            if len(tournoi_charge.joueurs) >= 8:
                afficher_message("Ce tournoi contient déjà 8 joueurs.")
                continue

            informations_joueur = demander_informations_joueur()

            try:
                classement = int(informations_joueur["classement"])
            except ValueError:
                afficher_message("Le classement doit être un nombre entier.")
                continue

            message_doublon = verifier_doublon_joueur(
                tournoi_charge.joueurs,
                informations_joueur,
            )

            if message_doublon:
                afficher_message(message_doublon)
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

            afficher_message(
                f'\nLe joueur "{joueur.prenom} {joueur.nom}" a bien été ajouté.'
            )

        elif choix_tournoi == "3":
            afficher_rapport_joueurs_ordre_alphabetique(tournoi_charge)

        elif choix_tournoi == "4":
            afficher_rapport_joueurs_par_classement(tournoi_charge)

        elif choix_tournoi == "5":
            afficher_rapport_tours(tournoi_charge)

        elif choix_tournoi == "6":
            afficher_rapport_matchs_d_un_tour(tournoi_charge)

        elif choix_tournoi == "7":
            menu_tournoi_actif = False

        elif choix_tournoi == "8":
            demarrer_tournoi(numero_tournoi, tournoi_charge)

        elif choix_tournoi == "9":
            saisir_scores_tour(tournoi_charge, numero_tournoi)

        elif choix_tournoi == "10":
            cloturer_tour(tournoi_charge, numero_tournoi)

        elif choix_tournoi == "11":
            creer_tour_suivant(tournoi_charge, numero_tournoi)

        else:
            afficher_message("Choix invalide.")


def charger_tournoi_existant():
    """Charge un tournoi existant."""
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


def lancer_menu_principal():
    """Lance le menu principal."""
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
            afficher_message("Fermeture du programme.")
            programme_en_cours = False

        else:
            afficher_message("Choix invalide.")
