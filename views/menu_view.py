def afficher_menu_principal():
    """Affiche le menu principal."""
    print("\n=== Gestionnaire de tournoi d'échecs ===")
    print("1. Créer un nouveau tournoi")
    print("2. Charger un tournoi existant")
    print("3. Afficher les tournois enregistrés")
    print("4. Quitter")


def demander_choix():
    """Demande le choix de l'utilisateur."""
    return input("Votre choix : ").strip()


def afficher_message(message):
    """Affiche un message simple."""
    print(message)
