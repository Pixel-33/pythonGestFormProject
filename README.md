# Test d'entretien "GestForm"

-------------
## Instructions
Vous devez établir un programme permettant de répondre à l’énoncé ci-dessous.
Le programme doit être écrit de préférence dans un langage en correspondance avec le poste pour lequel vous postulez (python, nodejs, angular, etc...).

## Énoncé
Soit une liste aléatoire de nombres entiers, compris entre -1000 et 1000. Pour chaque nombre n de liste, on veut effectuer les opérations suivantes:
* si le nombre est divisible par 3 : on affiche Geste
* si le nombre est divisible par 5 : on affiche Forme
* si le nombre est divisible par 3 et par 5 : on affiche Gestform (d’où le nom du test)
* sinon : on affiche le nombre n

## Livrable
Il faut fournir le ou les fichiers permettant à notre équipe de vérifier le bon fonctionnement du programme.

-----------------
-----------------
Mon livrable se présente sous la forme de 6 fichiers:  
* main.py -> c'est le point de départ de l'exécution du programme
* data.py -> génération des données du programme
* gestform.py -> articulation des différentes étapes du programme
* version_panda.py -> utilisation d'un Dataframe pandas pour calculer puis présenter la solution
* requirements.txt -> liste des modules nécessaires au fonctionnement du programme
* README.md -> Énoncé de l'exercice / Explications du code

Afin d'enrichir le programme, j'ai rajouté une fonctionnalité qui permet à l'utilisateur de saisir au clavier le nombre d'entiers qu'il souhaite tester.
J'ai également choisi de gérer la problématique dans un DataFrame pandas.
Les résultats sont ainsi affichés sous la forme d'un DataFrame dans le Terminal.
