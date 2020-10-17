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
from game import Game
import pygame

pygame.init()

# 1- Mise en place de la surface screen et de tout ses attributs.
pygame.display.set_caption("MiniCasino !")
screen = pygame.display.set_mode((1080, 720))

menu_image = pygame.image.load("assets/png/background.png")
menu_rect = menu_image.get_rect()
menu_rect.x = 0
menu_rect.y = 0

play_button_image = pygame.image.load("assets/png/play_button.png")
play_button_image_rect = play_button_image.get_rect()
play_button_image_rect.x = 1080 / 2 - play_button_image_rect.width / 2
play_button_image_rect.y = 590

game = Game()
course = Course()

run = True

# 2- Boucle d'affichage du jeu, sans ça pas de jeu tous simplement.
while run:

    # 3- Les booléen de conitionnement.
    if game.is_menu:
        screen.blit(menu_image, menu_rect)
        screen.blit(play_button_image, play_button_image_rect)

    if game.is_paused:
        game.paused(screen)

    elif game.is_choose_menu:
        game.choose(screen)

    if game.is_game:
        if course.is_rules:
            course.rule(screen)

        if course.is_lunch and game.is_game:
            course.lunch(screen)

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

        # 7- Evènement si une touche est lâcher
        elif event.type == pygame.KEYUP:
            game.press[event.key] = False

# 8- Evènement le boutton gauche de la souris clique
        # elif event.type == pygame.MOUSEBUTTONDOWN:

        # !!! Faire les boutons !!!
