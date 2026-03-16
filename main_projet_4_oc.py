# Import du contrôleur du menu principal.
# Le main ne gère pas directement l'affichage du menu :
# il délègue cette tâche au contrôleur.
from controllers.menu_controleur import lancer_menu_principal


# Point d'entrée du programme.
# On lance le menu principal via le contrôleur.
# Le contrôleur appelle la vue, puis récupère le choix saisi.
if __name__ == "__main__":
    choix_utilisateur = lancer_menu_principal()

    # Pour cette étape, on affiche simplement le choix récupéré
    # afin de vérifier que le circuit fonctionne bien.
    print(f"Choix saisi : {choix_utilisateur}")