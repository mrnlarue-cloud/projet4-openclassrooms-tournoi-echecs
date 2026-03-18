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


# Cette fonction lit le fichier JSON
# et renvoie la liste des tournois enregistrés.
# Si le fichier n'existe pas encore, on renvoie une liste vide.
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


# Cette fonction enregistre un nouveau tournoi.
# On lit d'abord la liste existante,
# on ajoute le nouveau tournoi converti en dictionnaire,
# puis on réécrit tout le fichier JSON.
def enregistrer_tournoi(tournoi):
    tournois_enregistres = lire_tournois_enregistres()
    tournois_enregistres.append(tournoi.to_dict())

    chemin_fichier = recuperer_chemin_fichier_tournois()

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


# Cette fonction récupère uniquement les noms des tournois.
# Cela permet à la vue d'afficher une liste simple dans la console.
def recuperer_noms_tournois():
    tournois_enregistres = lire_tournois_enregistres()
    noms_tournois = []

    for tournoi in tournois_enregistres:
        noms_tournois.append(tournoi.get("nom", "Tournoi sans nom"))

    return noms_tournois


# Cette fonction gère la création d'un nouveau tournoi.
# La vue récupère les informations,
# puis le contrôleur crée l'objet et le sauvegarde.
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


# Cette fonction remplace, dans le JSON,
# un tournoi déjà existant par sa version mise à jour.
def mettre_a_jour_tournoi_existant(numero_tournoi, tournoi):
    tournois_enregistres = lire_tournois_enregistres()

    # L'utilisateur choisit un numéro à partir de 1,
    # alors que la liste Python commence à 0.
    tournois_enregistres[numero_tournoi - 1] = tournoi.to_dict()

    chemin_fichier = recuperer_chemin_fichier_tournois()

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tournois_enregistres, fichier, indent=4, ensure_ascii=False)


# Cette fonction vérifie si le joueur saisi
# est déjà présent dans le tournoi.
# Elle renvoie un message si un doublon est trouvé,
# sinon elle renvoie None.
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
# Ici, on refuse le démarrage si le tournoi n'a pas exactement 8 joueurs
# ou si un premier tour existe déjà.
def verifier_demarrage_tournoi(tournoi):
    if len(tournoi.joueurs) != 8:
        return False, "Le tournoi doit contenir exactement 8 joueurs pour démarrer."

    if len(tournoi.tours) > 0:
        return False, "Le tournoi a déjà été démarré."

    return True, ""


# Pour le premier tour, on trie les joueurs
# du meilleur classement vers le moins bon.
def trier_joueurs_par_classement(joueurs):
    return sorted(joueurs, key=lambda joueur: joueur.classement, reverse=True)


# Cette fonction crée les 4 matchs du premier tour
# à partir de la liste triée des 8 joueurs.
# On reste volontairement simple pour cette étape.
def creer_matchs_premier_tour(joueurs_tries):
    matchs = []

    for index in range(0, len(joueurs_tries), 2):
        joueur_1 = joueurs_tries[index]
        joueur_2 = joueurs_tries[index + 1]

        match = Match(joueur_1, joueur_2)
        matchs.append(match)

    return matchs


# Cette fonction démarre réellement le tournoi.
# Elle vérifie d'abord que les conditions sont respectées,
# puis crée Tour 1, ses 4 matchs, sauvegarde le tout
# et affiche les appariements dans la console.
def demarrer_tournoi(numero_tournoi, tournoi):
    demarrage_autorise, message = verifier_demarrage_tournoi(tournoi)

    if not demarrage_autorise:
        print(message)
        return

    # On trie les joueurs selon leur classement
    # pour préparer les appariements du premier tour.
    joueurs_tries = trier_joueurs_par_classement(tournoi.joueurs)

    # On crée le premier tour et on enregistre sa date de début.
    tour_1 = Tour("Tour 1")
    tour_1.demarrer()

    # On crée ensuite les 4 matchs du premier tour.
    matchs = creer_matchs_premier_tour(joueurs_tries)

    for match in matchs:
        tour_1.ajouter_match(match)

    # On ajoute ce nouveau tour dans le tournoi.
    tournoi.ajouter_tour(tour_1)

    # On sauvegarde immédiatement dans le JSON
    # pour conserver le tournoi mis à jour.
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
# On utilise try / except ici car la conversion en float
# peut échouer si la saisie n'est pas un nombre.
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
# On modifie directement les objets Match,
# puis on sauvegarde le tournoi mis à jour dans le JSON.
def saisir_scores_tour(tournoi, numero_tournoi):
    if not tournoi.tours:
        print("Aucun tour n'a encore été créé.")
        return

    # On prend le dernier tour de la liste,
    # car c'est lui qui correspond au tour en cours.
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

        # On saisit les deux scores du match.
        # La vérification reste simple et adaptée au projet.
        score_joueur_1 = demander_score_valide("Score du joueur 1 (0, 0.5, 1) : ")
        score_joueur_2 = demander_score_valide("Score du joueur 2 (0, 0.5, 1) : ")

        # On enregistre les résultats directement dans le match.
        match.score_joueur_1 = score_joueur_1
        match.score_joueur_2 = score_joueur_2

    # Une fois tous les scores saisis,
    # on sauvegarde immédiatement dans le JSON.
    mettre_a_jour_tournoi_existant(numero_tournoi, tournoi)

    print("\nLes scores du tour ont bien été enregistrés.")


# Cette fonction gère tout le menu d'un tournoi chargé.
# On reste dans ce menu tant que l'utilisateur ne choisit pas de revenir.
def gerer_menu_tournoi_charge(numero_tournoi, tournoi_charge):
    menu_tournoi_actif = True

    while menu_tournoi_actif:
        afficher_menu_tournoi()
        choix_tournoi = demander_choix_menu_tournoi()

        # Choix 1 : affichage des détails du tournoi.
        if choix_tournoi == "1":
            afficher_details_tournoi_charge(tournoi_charge)

        # Choix 2 : ajout d'un joueur dans le tournoi.
        elif choix_tournoi == "2":
            if len(tournoi_charge.joueurs) >= 8:
                print("Ce tournoi contient déjà 8 joueurs.")
                continue

            informations_joueur = demander_informations_joueur()

            # Ici, try / except est adapté car la conversion
            # en entier peut échouer si la saisie n'est pas correcte.
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

            # On utilise la méthode du modèle Tournoi
            # pour garder une logique plus propre.
            tournoi_charge.ajouter_joueur(joueur)

            mettre_a_jour_tournoi_existant(numero_tournoi, tournoi_charge)

            print(f'\nLe joueur "{joueur.prenom} {joueur.nom}" a bien été ajouté.')

        # Choix 3 : affichage des joueurs du tournoi.
        elif choix_tournoi == "3":
            afficher_joueurs_tournoi(tournoi_charge.joueurs)

        # Choix 4 : retour au menu principal.
        elif choix_tournoi == "4":
            menu_tournoi_actif = False

        # Choix 5 : démarrage du tournoi.
        elif choix_tournoi == "5":
            demarrer_tournoi(numero_tournoi, tournoi_charge)

        # Choix 6 : saisie des scores du tour en cours.
        elif choix_tournoi == "6":
            saisir_scores_tour(tournoi_charge, numero_tournoi)

        else:
            print("Choix invalide.")


# Cette fonction charge un tournoi existant à partir du JSON,
# reconstruit l'objet Tournoi,
# puis envoie ce tournoi vers le menu dédié.
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

    # Une fois le tournoi chargé,
    # on entre dans le menu spécifique à ce tournoi.
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