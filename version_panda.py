import numpy as np
import pandas as pd
from matplotlib import pyplot
from tabulate import tabulate


def getResult(df):
    # Cette fonction va renvoyer (Geste, Forme, Gestform, sinon n) en fonction des conditions de l'exercice
    if df['Divisible_by_3'] and df['Divisible_by_5']:
        result = 'Gestform'
    elif df['Divisible_by_3']:
        result = 'Geste'
    elif df['Divisible_by_5']:
        result = 'Forme'
    else:
        result = df['Data']
    return result


def buildDataFrame(my_list):
    # Construction d'un DataFrame avec 4 colonnes
    #   'Data'              -> liste des nombres aléatoires
    #   'Result'            -> résultat produit par le programme (Geste, Forme, Gestform, sinon n)
    #   'Divisible_by_3'    -> boolean pour dire si divisible par 3
    #   'Divisible_by_5'    -> boolean pour dire si divisible par 5

    my_columns = ['Data']
    df = pd.DataFrame(my_list, columns=my_columns)
    df['Result'] = np.NAN
    df['Divisible_by_3'] = df['Data'] % 3 == 0
    df['Divisible_by_5'] = df['Data'] % 5 == 0

    # Remplissage de la colonne 'Result' en appliquant la fonction 'getResult' sur toutes les lignes du DataFrame
    df['Result'] = df.apply(getResult, axis=1)

    return df


def printDataFrame(df):
    # Affichage du DataFrame dans le terminal
    print(tabulate(df, headers='keys', tablefmt='pretty'))

