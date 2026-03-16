from views.menu_view import afficher_menu_principal, demander_choix


# Ce contrôleur affiche le menu principal en boucle.
# Le programme reste dans le menu tant que l'utilisateur
# ne choisit pas de quitter.
def lancer_menu_principal():
    while True:
        afficher_menu_principal()
        choix_utilisateur = demander_choix()

        # Si l'utilisateur choisit 1,
        # la fonctionnalité n'est pas encore disponible.
        if choix_utilisateur == "1":
            print("Création de tournoi : fonctionnalité non encore disponible.")

        # Si l'utilisateur choisit 2,
        # la fonctionnalité n'est pas encore disponible.
        elif choix_utilisateur == "2":
            print("Chargement de tournoi : fonctionnalité non encore disponible.")

        # Si l'utilisateur choisit 3,
        # la fonctionnalité n'est pas encore disponible.
        elif choix_utilisateur == "3":
            print("Affichage des tournois : fonctionnalité non encore disponible.")

        # Si l'utilisateur choisit 4,
        # on affiche un message puis on sort de la boucle.
        elif choix_utilisateur == "4":
            print("Fermeture du programme.")
            break

        # Si la saisie ne correspond à aucun choix attendu,
        # on signale que le choix est invalide.
        else:
            print("Choix invalide.")
