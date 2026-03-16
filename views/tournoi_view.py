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
