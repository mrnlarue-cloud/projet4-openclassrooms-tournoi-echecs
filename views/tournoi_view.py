def afficher_tournois_enregistres(noms_tournois):
    """Affiche la liste des tournois enregistrés."""
    print("\n=== Tournois enregistrés ===")

    if not noms_tournois:
        print("Aucun tournoi enregistré.")
        return

    for numero, nom_tournoi in enumerate(noms_tournois, start=1):
        print(f"{numero}. {nom_tournoi}")


def demander_informations_tournoi():
    """Demande les informations du tournoi."""
    print("\n=== Création d'un nouveau tournoi ===")

    nom = input("Nom du tournoi : ").strip()
    lieu = input("Lieu : ").strip()
    date = input("Date : ").strip()
    description = input("Description : ").strip()

    return {
        "nom": nom,
        "lieu": lieu,
        "date": date,
        "description": description,
    }


def afficher_message_tournoi_enregistre(nom_tournoi):
    """Affiche la confirmation d'enregistrement."""
    print(f'\nLe tournoi "{nom_tournoi}" a bien été enregistré.')


def demander_numero_tournoi():
    """Demande le numéro du tournoi."""
    return input("\nNuméro du tournoi à charger : ").strip()


def demander_numero_tour():
    """Demande le numéro du tour."""
    return input("\nNuméro du tour à consulter : ").strip()


def afficher_tournoi_charge(nom_tournoi):
    """Affiche le tournoi chargé."""
    print(f'\nTournoi chargé : "{nom_tournoi}"')


def afficher_choix_tournoi_invalide():
    """Affiche un choix de tournoi invalide."""
    print("\nNuméro de tournoi invalide.")


def afficher_details_tournoi_charge(tournoi):
    """Affiche les détails du tournoi."""
    print("\n=== Détails du tournoi chargé ===")
    print(f"Nom : {tournoi.nom}")
    print(f"Lieu : {tournoi.lieu}")
    print(f"Date : {tournoi.date_debut}")
    print(f"Description : {tournoi.description}")
    print(f"Nombre de joueurs : {len(tournoi.joueurs)}")
    print(f"Nombre de tours : {len(tournoi.tours)}")


def afficher_menu_tournoi():
    """Affiche le menu du tournoi."""
    print("\n=== Menu du tournoi ===")
    print("1. Afficher les détails du tournoi")
    print("2. Ajouter un joueur")
    print("3. Rapport : joueurs par ordre alphabétique")
    print("4. Rapport : joueurs par classement")
    print("5. Rapport : liste des tours")
    print("6. Rapport : matchs d'un tour")
    print("7. Retour au menu principal")
    print("8. Démarrer le tournoi")
    print("9. Saisir les scores du tour")
    print("10. Clôturer le tour")
    print("11. Créer le tour suivant")


def demander_choix_menu_tournoi():
    """Demande le choix du menu tournoi."""
    return input("Votre choix : ").strip()


def demander_informations_joueur():
    """Demande les informations du joueur."""
    print("\n=== Ajout d'un joueur ===")

    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    date_naissance = input("Date de naissance : ").strip()
    identifiant_national = input("Identifiant national : ").strip()
    classement = input("Classement : ").strip()

    return {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": date_naissance,
        "identifiant_national": identifiant_national,
        "classement": classement,
    }


def afficher_joueurs_tournoi(joueurs, titre="=== Joueurs du tournoi ==="):
    """Affiche une liste de joueurs."""
    print(f"\n{titre}")

    if not joueurs:
        print("Aucun joueur n'est encore enregistré dans ce tournoi.")
        return

    for numero, joueur in enumerate(joueurs, start=1):
        print(
            f"{numero}. {joueur.nom} {joueur.prenom} - "
            f"Classement : {joueur.classement}"
        )


def afficher_tours_tournoi(tours):
    """Affiche la liste des tours."""
    print("\n=== Rapport : liste des tours ===")

    if not tours:
        print("Aucun tour n'est encore enregistré dans ce tournoi.")
        return

    for numero, tour in enumerate(tours, start=1):
        date_fin = tour.date_fin

        if date_fin is None:
            date_fin = "Tour en cours"

        print(
            f"{numero}. {tour.nom} - "
            f"Début : {tour.date_debut} - "
            f"Fin : {date_fin}"
        )


def afficher_matchs_tour(tour):
    """Affiche les matchs d'un tour."""
    print(f"\n=== Rapport : matchs du {tour.nom} ===")

    if not tour.matchs:
        print("Aucun match n'est enregistré dans ce tour.")
        return

    for numero, match in enumerate(tour.matchs, start=1):
        print(
            f"{numero}. "
            f"{match.joueur_1.prenom} {match.joueur_1.nom} "
            f"vs "
            f"{match.joueur_2.prenom} {match.joueur_2.nom} "
            f"- score : {match.score_joueur_1} / {match.score_joueur_2}"
        )


def afficher_matchs_crees(tour):
    """Affiche les matchs créés pour un tour."""
    print(f"\n{tour.nom} créé avec {len(tour.matchs)} matchs :")

    for numero, match in enumerate(tour.matchs, start=1):
        print(
            f"{numero}. "
            f"{match.joueur_1.prenom} {match.joueur_1.nom} "
            f"vs "
            f"{match.joueur_2.prenom} {match.joueur_2.nom}"
        )


def afficher_entete_saisie_scores(nom_tour):
    """Affiche le titre de la saisie des scores."""
    print(f"\n=== Saisie des scores - {nom_tour} ===")


def afficher_match_a_saisir(match):
    """Affiche le match en cours de saisie."""
    print(
        f"\nMatch : "
        f"{match.joueur_1.prenom} {match.joueur_1.nom} "
        f"vs "
        f"{match.joueur_2.prenom} {match.joueur_2.nom}"
    )


def demander_score_valide(message):
    """Demande un score valide."""
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


def demander_continuer_saisie_scores():
    """Demande si l'utilisateur souhaite continuer la saisie des scores."""
    while True:
        choix = input("\nContinuer la saisie des scores ? (oui/non) : ").strip().lower()

        if choix in ["oui", "non"]:
            return choix

        print("Veuillez répondre par 'oui' ou 'non'.")
