from views.menu_view import afficher_menu_principal, demander_choix


# Ce contrôleur lance le menu principal.
# Il affiche le menu, récupère le choix de l'utilisateur
# puis décide quoi faire selon la valeur saisie.
def lancer_menu_principal():
    afficher_menu_principal()
    choix_utilisateur = demander_choix()

    # Si l'utilisateur choisit 1,
    # la fonctionnalité n'existe pas encore.
    if choix_utilisateur == "1":
        print("Création de tournoi : fonctionnalité non encore disponible.")

    # Si l'utilisateur choisit 2,
    # la fonctionnalité n'existe pas encore.
    elif choix_utilisateur == "2":
        print("Chargement de tournoi : fonctionnalité non encore disponible.")

    # Si l'utilisateur choisit 3,
    # la fonctionnalité n'existe pas encore.
    elif choix_utilisateur == "3":
        print("Affichage des tournois : fonctionnalité non encore disponible.")

    # Si l'utilisateur choisit 4,
    # on affiche simplement un message de sortie.
    elif choix_utilisateur == "4":
        print("Fermeture du programme.")

    # Si la saisie ne correspond à aucun choix attendu,
    # on signale que le choix est invalide.
    else:
        print("Choix invalide.")
