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

    elif game.is_game:
        if game.is_choose_menu:
            game.choose(screen)

        elif course.is_rules and not game.is_choose_menu:
            course.rule(screen)

        elif course.is_lunch and game.is_game:
            course.lunch(screen)

    elif game.is_paused:
        game.paused(screen)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if game.is_menu:

                if play_button_image_rect.collidepoint(event.pos):
                    game.is_menu = False
                    game.is_game = True
                    game.is_choose_menu = True

            if game.is_game:

                if game.choix_milieu_image_rect.collidepoint(event.pos) and not course.is_lunch:
                    game.is_choose_menu = False
                    course.is_lunch = True

                elif course.ok_image_rect.collidepoint(event.pos) and course.is_lunch:
                    course.is_rules = False

                if course.nombre.un_rect.collidepoint(event.pos):

                    if course.nombre.is_premier:
                        course.nombre.un_rect.x = 283
                        course.nombre.un_rect.y = 502
                        course.nombre.is_premier = False
                        course.nombre.is_premier_pris = True

                    else:
                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut
                        course.nombre.is_premier_pris = False
                        course.nombre.is_premier = True

                    # !!! Reformulez les conditions !!!