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
Mon livrable se présente sous la forme de 7 fichiers:  
* __*main.py*__ -> c'est le point de départ de l'exécution du programme
* __*data.py*__ -> génération des données du programme
* __*gestform.py*__ -> articulation des différentes étapes du programme
* __*version_panda.py*__ -> utilisation d'un Dataframe pandas pour calculer puis présenter la solution
* __*requirements.txt*__ -> liste des modules nécessaires au fonctionnement du programme
* __*README.md*__ -> Énoncé de l'exercice / Explications du code
* __*GestForm_test.ipynb*__ -> Notebook Google Colab

J'ai développé dans un premier temps avec l'IDE __*PyCharm*__ les 6 premiers fichiers ci-dessus.  
J'ai ensuite développé dans un notebook en ligne __*Google Colab*__.  
Afin d'enrichir le programme, dans la version PyCharm, j'ai rajouté une fonctionnalité qui __permet à l'utilisateur de saisir au clavier le nombre d'entiers qu'il souhaite tester__, avec une gestion des erreurs de saisie.  
J'ai également choisi de gérer la problématique dans un DataFrame pandas.
J'affiche le résultat sous la forme d'un DataFrame dans le Terminal pour la version PyCharm (colonne 'Result' du DataFrame).

Je suis allé un peu plus loin dans la version Colab. J'ai calculé les occurences de 'Geste' 'Forme' 'Gestform' 'n', pour finalement afficher un graphique camembert avec les pourcentages d'occurrences.

## GitHub
J'ai créé un repository __*pythonGestFormProject*__ sur mon compte GitHub dans lequel j'ai déposé les 7 fichiers du livrable.  
Une fois sur le notebook __*GestForm_test.ipynb*__ dans GitHub, il y a en haut à gauche un lien "Open in Colab" qui permet d'ouvrir le notebook dans Google Colab en ligne et ainsi exécuter les cellules.  
Concernant la version "PyCharm", le fichier __*requirements.txt*__ permet de créer un environnement virtuel identique à celui que j'ai utilisé afin de garantir la bonne exécution du programme sur une autre machine. J'ai utilisé la version de Python 3.10.
