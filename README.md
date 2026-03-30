# Gestionnaire de tournoi d'échecs

Application console en **Python 3.11** permettant de gérer des tournois d'échecs hors ligne.

Ce projet a été réalisé dans le cadre du **projet 4 OpenClassrooms**.  
L'application suit une architecture **MVC** avec une séparation entre :
- les **modèles** (`models`) ;
- les **vues** (`views`) ;
- le **contrôleur** (`controllers`).

Les données sont enregistrées dans un fichier **JSON**, ce qui permet de conserver les tournois créés, les joueurs, les tours et les matchs.

## Fonctionnalités

L'application permet de :

- créer un nouveau tournoi ;
- charger un tournoi existant ;
- ajouter des joueurs à un tournoi ;
- démarrer un tournoi ;
- générer les matchs du premier tour ;
- saisir les scores des matchs ;
- clôturer un tour ;
- créer le tour suivant ;
- afficher les 4 rapports demandés par le projet :
  - la liste des joueurs par ordre alphabétique ;
  - la liste des joueurs par classement ;
  - la liste des tours d'un tournoi ;
  - la liste des matchs d'un tour.

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

1. créer un nouveau tournoi ;
2. charger un tournoi existant ;
3. afficher les tournois enregistrés ;
4. quitter l'application.

Une fois un tournoi chargé, un **menu de tournoi** permet notamment de :

- consulter les détails du tournoi ;
- ajouter les joueurs ;
- afficher les rapports ;
- démarrer le tournoi ;
- saisir les scores d'un tour ;
- clôturer le tour en cours ;
- créer le tour suivant.

### Déroulement général d'un tournoi

Le fonctionnement prévu est le suivant :

1. créer un tournoi ;
2. ajouter les joueurs au tournoi ;
3. démarrer le tournoi lorsque 8 joueurs sont enregistrés ;
4. saisir les scores des matchs du tour en cours ;
5. clôturer le tour ;
6. créer le tour suivant ;
7. répéter les étapes jusqu'à la fin du tournoi.

## Données et sauvegarde

Les données sont enregistrées dans le fichier suivant :

```text
donnees_tournoi/tournois.json
```

La sauvegarde se fait pendant l'utilisation du programme, ce qui permet de recharger un tournoi existant ultérieurement.

Lors de l'enregistrement, l'application crée automatiquement le dossier `donnees_tournoi/` s'il n'existe pas encore.

## Rapports disponibles

L'application permet d'afficher les 4 rapports demandés :

1. la liste de tous les joueurs par ordre alphabétique ;
2. la liste de tous les joueurs par classement ;
3. la liste de tous les tours du tournoi ;
4. la liste de tous les matchs d'un tour.

## Qualité du code

Le code a été vérifié avec :

- `black`
- `flake8`
- `flake8-html`

## Utiliser Flake8

Pour analyser le code dans le terminal :

```bash
flake8 .
```

Ou, selon votre environnement :

```bash
python -m flake8 .
```

Cette commande vérifie le respect des règles de style et signale les éventuels écarts.

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
