# Ce fichier permet de récupérer les données pour notre programme
# Les données sont une liste aléatoire de nombres entiers compris entre -1000 et 1000
import numpy as np


def getRandomIntList(nb_element):
    my_list = np.random.randint(-1000, 1001, nb_element).tolist()
    return my_list
