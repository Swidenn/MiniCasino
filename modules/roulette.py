# coding: utf-8
import random

def roulette(nb_choisie):
    """
    fonction de roulette simple

    :param nb_choisie:
    nombre demandé

    :return:
    Si -> 0: Perdu
    Si -> 1: Tu as obtenu le "0" x14 de la mise
    Si -> 2: Tu as obtenu le même nombre x3 de la mise
    Si -> 3: Tu as obtenu la même couleur "Rouge" x1.5 de la mise
    Si -> 4: Tu as obtenu la même couleur "Noir" x1.5 de la mise
    """

    import random

    number = random.randint(0, 52)

    if nb_choisie == number:
        if nb_choisie == 0:
            return 1
        else:
            return 2

    elif nb_choisie%2 == 0 and number%2 == 0:
        return 3

    elif nb_choisie%2 != 0 and number%2 != 0:
        return 4

    else:
        return 0


"""dozen = {
    "first_dozen" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12],
    "second_dozen" : [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "third_dozen" : [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
}

column = {
    "first_column" : [1, 2, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
    "second_column" : [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    "third_column" : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
}

find = False

z = 15

if not find:
    for i in dozen["first_dozen"]:
        if i == z:
            print("First dozen")
            find = True

    for i in dozen["second_dozen"]:
        if i == z:
            print("Second dozen")
            find = True

    for i in dozen["third_dozen"]:
        if i == z:
            print("Third dozen")
            find = True

"""