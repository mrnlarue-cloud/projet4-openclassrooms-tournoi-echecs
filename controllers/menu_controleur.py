from views.menu_view import afficher_menu_principal, demander_choix


# Ce contrôleur lance le menu principal.
# Il demande à la vue d'afficher les options,
# puis récupère le choix saisi par l'utilisateur.
# Pour le moment, il ne fait encore aucune action métier.
# Il renvoie simplement le choix au programme principal.
def lancer_menu_principal():
    afficher_menu_principal()
    choix_utilisateur = demander_choix()
    return choix_utilisateur
