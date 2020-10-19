# coding: utf-8

def course(c1, c2, c3, c4, c5, tirage):
    """
    Cette fonction prend en paramètre 5 positions et les test

    :param c1:
    :param c2:
    :param c3:
    :param c4:
    :param c5:
    :param liste:
    apport de la liste de cheveaux chevaux

    :return:
    Si la fonction retourne 1 -> Alors 5 cheveaux bien placé
    Si la fonction retourne 2 -> Alors 4 cheveaux bien placé
    Si la fonction retourne 2 -> Alors 5 cheveaux dans le désordre
    Si la fonction retourne 4 -> Alors 3 cheveaux bien placé du 1er au 3ème
    Si la fonction retourne 5 -> Alors 4 cheveaux dans le désorde
    Si la fonction retourne 6 -> Alors vous avez perdu
    """

    lunch = tirage
    print(lunch)

    if c1 == lunch[0] and c2 == lunch[1] and c3 == lunch[2]:
        if c4 == lunch[3] and c5 == lunch[4]:
            return 1
        else:
            return 4

    elif c5 != lunch[4] and c5 != lunch[3] and c5 != lunch[2] and c5 != lunch[1] and c5 != lunch[0]:
        return 6

    elif c1 == lunch[4] or c1 == lunch[3] or c1 == lunch[2] or c1 == lunch[1]:
        if c2 != lunch[1] and c3 != lunch[2] and c4 != lunch[3] and c5 != lunch[4]:
            return 3

    elif c1 != lunch[0]:
        if c2 == lunch[1] and c3 == lunch[2] and c4 == lunch[3] and c5 == lunch[4]:
            return 2
        elif c2 != lunch[1] and c3 != lunch[2] and c4 != lunch[3] and c5 != lunch[4]:
            return 5
