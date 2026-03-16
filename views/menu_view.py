# views/menu_view.py


# Cette fonction affiche le menu principal dans la console.
# Son rôle est uniquement de montrer les actions possibles
# à l'utilisateur au démarrage du programme.
def afficher_menu_principal():
    print("\n=== Gestionnaire de tournoi d'échecs ===")
    print("1. Créer un nouveau tournoi")
    print("2. Charger un tournoi existant")
    print("3. Afficher les tournois enregistrés")
    print("4. Quitter")


# Cette fonction récupère le choix de l'utilisateur.
# Elle ne vérifie pas encore si la valeur est correcte.
# Elle sert seulement à lire la saisie proprement.
def demander_choix():
    return input("Votre choix : ").strip()
