# coding: utf-8

def tirage():
    """
    Cette fonction retourne une liste de 5 nombres parmis les 20 de la liste

    :return:
    retourne une liste de 5 nombres
    """
    from random import sample

    cheveaux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    return sample(cheveaux, k=5)
