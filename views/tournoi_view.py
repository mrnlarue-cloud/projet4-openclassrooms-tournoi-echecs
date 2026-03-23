# Cette fonction affiche dans la console la liste des tournois
# déjà enregistrés dans le fichier JSON.
# Elle ne lit pas le fichier elle-même :
# elle reçoit simplement une liste de noms préparée ailleurs.
def afficher_tournois_enregistres(noms_tournois):
    print("\n=== Tournois enregistrés ===")

    # Si la liste est vide, cela signifie qu'aucun tournoi
    # n'a été trouvé ou qu'aucun tournoi n'a encore été enregistré.
    if not noms_tournois:
        print("Aucun tournoi enregistré.")
        return

    # Si la liste contient des éléments,
    # on affiche chaque tournoi avec un numéro
    # pour rendre la lecture plus claire dans la console.
    for numero, nom_tournoi in enumerate(noms_tournois, start=1):
        print(f"{numero}. {nom_tournoi}")


# Cette fonction demande à l'utilisateur les informations de base
# nécessaires pour créer un nouveau tournoi.
# Elle ne crée pas l'objet Tournoi elle-même :
# elle récupère seulement les données saisies dans la console.
def demander_informations_tournoi():
    print("\n=== Création d'un nouveau tournoi ===")

    # On récupère chaque information séparément
    # pour garder une saisie simple et lisible.
    nom = input("Nom du tournoi : ").strip()
    lieu = input("Lieu : ").strip()
    date = input("Date : ").strip()
    description = input("Description : ").strip()

    # On renvoie les données dans un dictionnaire
    # pour que le contrôleur puisse ensuite les utiliser.
    return {
        "nom": nom,
        "lieu": lieu,
        "date": date,
        "description": description,
    }


# Cette fonction affiche un message de confirmation
# après l'enregistrement d'un tournoi.
def afficher_message_tournoi_enregistre(nom_tournoi):
    print(f'\nLe tournoi "{nom_tournoi}" a bien été enregistré.')


# Cette fonction demande à l'utilisateur quel tournoi il veut charger.
# Elle récupère simplement le numéro saisi dans la console.
# La vérification du choix sera faite dans le contrôleur.
def demander_numero_tournoi():
    return input("\nNuméro du tournoi à charger : ").strip()


# Cette fonction demande à l'utilisateur
# le numéro du tour qu'il veut consulter.
def demander_numero_tour():
    return input("\nNuméro du tour à consulter : ").strip()


# Cette fonction affiche un message de confirmation
# quand un tournoi a bien été chargé.
def afficher_tournoi_charge(nom_tournoi):
    print(f'\nTournoi chargé : "{nom_tournoi}"')


# Cette fonction affiche un message si le numéro saisi
# ne correspond à aucun tournoi enregistré.
def afficher_choix_tournoi_invalide():
    print("\nNuméro de tournoi invalide.")


# Cette fonction affiche les informations principales
# du tournoi qui vient d'être chargé.
# Elle reçoit directement l'objet Tournoi
# déjà reconstruit par le contrôleur.
def afficher_details_tournoi_charge(tournoi):
    print("\n=== Détails du tournoi chargé ===")
    print(f"Nom : {tournoi.nom}")
    print(f"Lieu : {tournoi.lieu}")
    print(f"Date : {tournoi.date_debut}")
    print(f"Description : {tournoi.description}")
    print(f"Nombre de joueurs : {len(tournoi.joueurs)}")
    print(f"Nombre de tours : {len(tournoi.tours)}")


# Cette fonction affiche le menu des actions possibles
# pour un tournoi déjà chargé.
# Elle ne fait qu'afficher les choix disponibles.
def afficher_menu_tournoi():
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


# Cette fonction récupère le choix de l'utilisateur
# dans le menu du tournoi.
def demander_choix_menu_tournoi():
    return input("Votre choix : ").strip()


# Cette fonction demande à l'utilisateur
# les informations nécessaires pour créer un joueur.
# Elle renvoie les données saisies
# dans un dictionnaire simple.
def demander_informations_joueur():
    print("\n=== Ajout d'un joueur ===")

    # On récupère les informations de base
    # du joueur depuis la console.
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    date_naissance = input("Date de naissance : ").strip()
    identifiant_national = input("Identifiant national : ").strip()
    classement = input("Classement : ").strip()

    # On renvoie les données au contrôleur
    # pour qu'il puisse créer l'objet Joueur.
    return {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": date_naissance,
        "identifiant_national": identifiant_national,
        "classement": classement,
    }


# Cette fonction affiche une liste de joueurs dans la console.
# Elle peut servir pour l'affichage classique
# ou pour un rapport avec un titre différent.
def afficher_joueurs_tournoi(joueurs, titre="=== Joueurs du tournoi ==="):
    print(f"\n{titre}")

    # Si aucun joueur n'est encore ajouté,
    # on affiche un message simple.
    if not joueurs:
        print("Aucun joueur n'est encore enregistré dans ce tournoi.")
        return

    # On affiche chaque joueur avec un numéro
    # pour rendre la lecture plus claire.
    for numero, joueur in enumerate(joueurs, start=1):
        print(
            f"{numero}. {joueur.nom} {joueur.prenom} - "
            f"Classement : {joueur.classement}"
        )


# Cette fonction affiche la liste des tours
# enregistrés dans un tournoi.
def afficher_tours_tournoi(tours):
    print("\n=== Rapport : liste des tours ===")

    # Si aucun tour n'existe encore,
    # on affiche un message simple.
    if not tours:
        print("Aucun tour n'est encore enregistré dans ce tournoi.")
        return

    # On affiche chaque tour avec son numéro,
    # sa date de début et sa date de fin.
    for numero, tour in enumerate(tours, start=1):
        date_fin = tour.date_fin

        if date_fin is None:
            date_fin = "Tour en cours"

        print(
            f"{numero}. {tour.nom} - "
            f"Début : {tour.date_debut} - "
            f"Fin : {date_fin}"
        )


# Cette fonction affiche les matchs d'un tour.
def afficher_matchs_tour(tour):
    print(f"\n=== Rapport : matchs du {tour.nom} ===")

    # Si aucun match n'est enregistré,
    # on affiche un message simple.
    if not tour.matchs:
        print("Aucun match n'est enregistré dans ce tour.")
        return

    # On affiche chaque match avec son numéro,
    # les deux joueurs et leurs scores.
    for numero, match in enumerate(tour.matchs, start=1):
        print(
            f"{numero}. "
            f"{match.joueur_1.prenom} {match.joueur_1.nom} "
            f"vs "
            f"{match.joueur_2.prenom} {match.joueur_2.nom} "
            f"- score : {match.score_joueur_1} / {match.score_joueur_2}"
        )
