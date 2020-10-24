# coding: utf-8

"""
Développer par DELIOT Yllan
Terminal Générale n°9
17/10/2020

But de ce fichier:
Code d'initialisation et de lancement du jeu, contenant les
données de base utile au lancement du jeu sans rentrer dans
le jeu vraiment.
"""

from courseepique import Course
from game import *
from machineasous import MachineATrous
import pygame

pygame.init()

# 1- Mise en place de la surface screen et de tout ses attributs.
pygame.display.set_caption("MiniCasino !")
screen = pygame.display.set_mode((1080, 720))

game = Game()
course = Course()
mt = MachineATrous()
nomoney = NoMoney()

run = True

# 2- Boucle d'affichage du jeu, sans ça pas de jeu tous simplement.
while run:

    # 3- Les booléen de conitionnement.
    game.game_start(screen, course, mt)

    # 4- Flip() est essentiel pour update la surface donc très importants.
    pygame.display.flip()

    # 5- Boucle for de détection ici toutes les touches et évenements fait sur la
    #    surface sont récupérer et manipuler ici.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        # 6 - Evènement si une touche est presser
        elif event.type == pygame.KEYDOWN:
            game.press[event.key] = True

            if event.key == pygame.K_ESCAPE:
                if game.is_game:
                    game.is_game = False
                    game.is_paused = True

                elif game.is_paused:
                    game.is_paused = False
                    game.is_game = True

            if event.key == pygame.K_SPACE:

                if game.is_game and mt.machine_is_lunch:

                    if game.money >= 3:
                        pygame.time.wait(100)
                        mt.spin(game)
                    else:
                        mt.t = True
                        mt.z = 0

        # 7- Evènement si une touche est lâcher
        elif event.type == pygame.KEYUP:
            game.press[event.key] = False

        # 8- Evènement le boutton gauche de la souris clique
        elif event.type == pygame.MOUSEBUTTONDOWN:

            game.game_button(event, course, mt)
