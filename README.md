# Gestionnaire de tournoi d'échecs

Application console en **Python** permettant de gérer des tournois d'échecs hors ligne.

Ce projet a été réalisé dans le cadre du **projet 4 OpenClassrooms**.  
L'application suit une architecture **MVC** avec une séparation entre :
- Les **modèles** (`models`) ;
- Les **vues** (`views`) ;
- Le **contrôleur** (`controllers`).

Les données sont enregistrées dans un fichier **JSON**, ce qui permet de conserver les tournois créés, les joueurs, les tours et les matchs.

## Fonctionnalités

L'application permet de :

- Créer un nouveau tournoi ;
- Charger un tournoi existant ;
- Ajouter des joueurs à un tournoi ;
- Démarrer un tournoi ;
- Générer les matchs du premier tour ;
- Saisir les scores des matchs ;
- Clôturer un tour ;
- Créer le tour suivant ;
- Afficher les 4 rapports demandés par le projet :
  - La liste des joueurs par ordre alphabétique ;
  - La liste des joueurs par classement ;
  - La liste des tours d'un tournoi ;
  - La liste des matchs d'un tour.

## Structure du projet

```text
PROJET_4_OC/
├── controllers/
│   ├── __init__.py
│   └── menu_controleur.py
├── donnees_tournoi/
│   └── tournois.json
├── models/
│   ├── __init__.py
│   ├── joueur.py
│   ├── match.py
│   ├── tour.py
│   └── tournoi.py
├── views/
│   ├── __init__.py
│   ├── menu_view.py
│   └── tournoi_view.py
├── .flake8
├── .gitignore
├── main_projet_4_oc.py
├── README.md
├── Requirements.txt
└── flake8-html/
```

## Prérequis

- **Python 3.11**

## Installation

### Création d'un environnement virtuel

Création d'un environnement virtuel  
Il est recommandé d’utiliser un environnement virtuel afin d’isoler les dépendances du projet.

- Pour Windows :
  - Création de l’environnement virtuel :
    - `python -m venv .venv`
  - Activation de l’environnement :
    - `.venv\Scripts\activate`

- Pour macOS :
  - Création de l’environnement virtuel :
    - `python3 -m venv .venv`
  - Activation de l’environnement :
    - `source .venv/bin/activate`

- Pour Linux :
  - Création de l’environnement virtuel :
    - `python3 -m venv .venv`
  - Activation de l’environnement :
    - `source .venv/bin/activate`

Une fois activé, le terminal affichera : `(.venv)` en début de ligne.

### Installation des dépendances

Depuis la racine du projet :

```bash
pip install -r Requirements.txt
```

## Lancer le programme

Depuis la racine du projet :

```bash
python main_projet_4_oc.py
```

Selon votre environnement, la commande suivante peut aussi être utilisée :

```bash
python3 main_projet_4_oc.py
```

## Fonctionnement de l'application

Le programme démarre sur un **menu principal** qui permet de :

1. Créer un nouveau tournoi ;
2. Charger un tournoi existant ;
3. Afficher les tournois enregistrés ;
4. Quitter l'application.

Une fois un tournoi chargé, un **menu de tournoi** permet notamment de :

- Consulter les détails du tournoi ;
- Ajouter les joueurs ;
- Afficher les rapports ;
- Démarrer le tournoi ;
- Saisir les scores d'un tour ;
- Clôturer le tour en cours ;
- Créer le tour suivant.

### Déroulement général d'un tournoi

Le fonctionnement prévu est le suivant :

1. Créer un tournoi ;
2. Ajouter les joueurs au tournoi ;
3. Démarrer le tournoi lorsque 8 joueurs sont enregistrés ;
4. Saisir les scores des matchs du tour en cours ;
5. Clôturer le tour ;
6. Créer le tour suivant ;
7. Répéter les étapes jusqu'à la fin du tournoi.

## Données et sauvegarde

Les données sont enregistrées dans le fichier suivant :

```text
donnees_tournoi/tournois.json
```

La sauvegarde se fait pendant l'utilisation du programme, ce qui permet de recharger un tournoi existant ultérieurement.

Lors de l'enregistrement, l'application crée automatiquement le dossier `donnees_tournoi/` s'il n'existe pas encore.

## Rapports disponibles

L'application permet d'afficher les 4 rapports demandés :

1. La liste de tous les joueurs par ordre alphabétique ;
2. La liste de tous les joueurs par classement ;
3. La liste de tous les tours du tournoi ;
4. La liste de tous les matchs d'un tour.

## Qualité du code

Le code a été vérifié avec :

- `black`
- `flake8`
- `flake8-html`

## Générer le rapport flake8-html

Depuis la racine du projet :

```bash
python -m flake8 . --format=html --htmldir=flake8-html
```

Selon votre environnement :

```bash
python3 -m flake8 . --format=html --htmldir=flake8-html
```

Le rapport HTML sera généré dans le dossier `flake8-html/`.
