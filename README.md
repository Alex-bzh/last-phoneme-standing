# Last Phoneme Standing (LPS)

LPS est un jeu, écrit en python, basé sur la comparaison de phonèmes. Tout mot proposé par un joueur doit au moins débuter par le dernier phonème du mot précédent.

## Liste des fichiers

- *lexique.txt* : la base de données, au format CSV, qui contient le lemme et sa représentation phonétique ;
- *lps.py* : le programme principal, à lancer dans un environnement python ;
- *README.md* : le présent fichier qui contient des informations diverses ainsi que les instructions d'installation ;
- *tools.py* : les fonctions nécessaires à l'exécution du jeu.

## Installation

1. Télécharger la dernière archive
2. Décompacter dans le répertoire de votre choix
3. Lancer le script *lps.py* dans un environnement python :
```
$ python lps.py
```

## Utilisation

### Principe

À l'invite de commande, le premier joueur propose un mot dont il existe une entrée dans le dictionnaire (fichier *lexique.txt*). Le deuxième joueur doit alors trouver un mot dont les premiers phonèmes commencent par les derniers du mot soumis par le premier joueur.

### Déroulement d'une phase de jeu

1. Le joueur 1 propose le mot *choisir*
2. Le joueur 2 propose le mot *irascible*
3. Le programme convertit les deux mots en représentation phonétique et repère que les deux premiers phonèmes du mot *irascible* sont identiques aux deux derniers du mot *choisir*
4. Le joueur 2 marque 2 points

### Règles

- Un mot ne peut être proposé qu’une seule fois
- Seuls l’infinitif ou le masculin singulier sont acceptés