from data import getRandomIntList
from version_panda import buildDataFrame, printDataFrame


def run_gestform():
    # Le programme demande à l'utilisateur combien d'entier il souhaite tester
    nb_element = input("Veuillez renseigner le nombre d'élément que vous souhaitez tester (MIN 1 / MAX 10000) : ")
    # Le programme vérifie que la saisie de l'utilisateur est correcte => compris dans l'intervale: [1;10000]
    try:
        nb_element = int(nb_element)
        if nb_element < 1 or nb_element > 10000:
            raise ValueError
    except ValueError:
        print("Désolé, la valeur saisie n'est pas un nombre autorisé...")
        run_gestform()
    else:
        # La saisie de l'utilisateur est correcte, le programme peut continuer

        # Récupération de la liste aléatoire des entiers
        my_list = getRandomIntList(nb_element)

        # Construction d'un DataFrame avec le module pandas
        df = buildDataFrame(my_list)

        # Affichage du DataFrame
        printDataFrame(df)
