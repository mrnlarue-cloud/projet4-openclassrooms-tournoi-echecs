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
    print("5. Retour au menu principal")
    print("6. Démarrer le tournoi")
    print("7. Saisir les scores du tour")
    print("8. Clôturer le tour")
    print("9. Créer le tour suivant")


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
