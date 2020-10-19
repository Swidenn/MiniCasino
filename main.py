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

is_premier_pris = False
is_deuxieme_pris = False
is_troisieme_pris = False
is_quatrieme_pris = False
is_cinqieme_pris = False

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

# !! Corriger les bugs et ajouter les autres nombres !!

                if course.nombre.un_rect.collidepoint(event.pos):

                    if course.nombre.un_rect.x == 283:

                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.un_rect.x == 400:

                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.un_rect.x == 507:

                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.un_rect.x == 610:

                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.un_rect.x == 708:

                        course.nombre.un_rect.x = course.nombre.x_un
                        course.nombre.un_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.deux_rect.collidepoint(event.pos):

                    if course.nombre.deux_rect.x == 283:

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.deux_rect.x == 400:

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.deux_rect.x == 507:

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.deux_rect.x == 610:

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.deux_rect.x == 708:

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.trois_rect.collidepoint(event.pos):

                    if course.nombre.trois_rect.x == 283:

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.trois_rect.x == 400:

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.trois_rect.x == 507:

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.trois_rect.x == 610:

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.trois_rect.x == 708:

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.quatre_rect.collidepoint(event.pos):

                    if course.nombre.quatre_rect.x == 283:

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.quatre_rect.x == 400:

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.quatre_rect.x == 507:

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.quatre_rect.x == 610:

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.quatre_rect.x == 708:

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.cinq_rect.collidepoint(event.pos):

                    if course.nombre.cinq_rect.x == 283:

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.cinq_rect.x == 400:

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.cinq_rect.x == 507:

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.cinq_rect.x == 610:

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.cinq_rect.x == 708:

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.six_rect.collidepoint(event.pos):

                    if course.nombre.six_rect.x == 283:

                        course.nombre.six_rect.x = course.nombre.x_six
                        course.nombre.six_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.six_rect.x == 400:

                        course.nombre.six_rect.x = course.nombre.x_six
                        course.nombre.six_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.six_rect.x == 507:

                        course.nombre.six_rect.x = course.nombre.x_six
                        course.nombre.six_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.six_rect.x == 610:

                        course.nombre.six_rect.x = course.nombre.x_six
                        course.nombre.six_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.six_rect.x == 708:

                        course.nombre.six_rect.x = course.nombre.x_six
                        course.nombre.six_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.sept_rect.collidepoint(event.pos):

                    if course.nombre.sept_rect.x == 283:

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.sept_rect.x == 400:

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.sept_rect.x == 507:

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.sept_rect.x == 610:

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.sept_rect.x == 708:

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.huit_rect.collidepoint(event.pos):

                    if course.nombre.huit_rect.x == 283:

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.huit_rect.x == 400:

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.huit_rect.x == 507:

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.huit_rect.x == 610:

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.huit_rect.x == 708:

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.neuf_rect.collidepoint(event.pos):

                    if course.nombre.neuf_rect.x == 283:

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.neuf_rect.x == 400:

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.neuf_rect.x == 507:

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.neuf_rect.x == 610:

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.neuf_rect.x == 708:

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.dix_rect.collidepoint(event.pos):

                    if course.nombre.dix_rect.x == 283:

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                        is_premier_pris = False

                    elif course.nombre.dix_rect.x == 400:

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                        is_deuxieme_pris = False

                    elif course.nombre.dix_rect.x == 507:

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                        is_troisieme_pris = False

                    elif course.nombre.dix_rect.x == 610:

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.dix_rect.x == 708:

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                        is_cinqieme_pris = False

                if course.nombre.onze_rect.collidepoint(event.pos):

                    if course.nombre.onze_rect.x == 283:

                        course.nombre.onze_rect.x = course.nombre.x_un
                        course.nombre.onze_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.onze_rect.x == 400:

                        course.nombre.onze_rect.x = course.nombre.x_un
                        course.nombre.onze_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.onze_rect.x == 507:

                        course.nombre.onze_rect.x = course.nombre.x_un
                        course.nombre.onze_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.onze_rect.x == 610:

                        course.nombre.onze_rect.x = course.nombre.x_un
                        course.nombre.onze_rect.y = course.nombre.y_haut

                        is_quatrieme_pris = False

                    elif course.nombre.onze_rect.x == 708:

                        course.nombre.onze_rect.x = course.nombre.x_un
                        course.nombre.onze_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.douze_rect.collidepoint(event.pos):

                    if course.nombre.douze_rect.x == 283:

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.douze_rect.x == 400:

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.douze_rect.x == 507:

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.douze_rect.x == 610:

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.douze_rect.x == 708:

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.treize_rect.collidepoint(event.pos):

                    if course.nombre.treize_rect.x == 283:

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.treize_rect.x == 400:

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.treize_rect.x == 507:

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.treize_rect.x == 610:

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.treize_rect.x == 708:

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.quatorze_rect.collidepoint(event.pos):

                    if course.nombre.quatorze_rect.x == 283:

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.quatorze_rect.x == 400:

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.quatorze_rect.x == 507:

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.quatorze_rect.x == 610:

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.quatorze_rect.x == 708:

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.quinze_rect.collidepoint(event.pos):

                    if course.nombre.quinze_rect.x == 283:

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.quinze_rect.x == 400:

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.quinze_rect.x == 507:

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.quinze_rect.x == 610:

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.quinze_rect.x == 708:

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.seize_rect.collidepoint(event.pos):

                    if course.nombre.seize_rect.x == 283:

                        course.nombre.seize_rect.x = course.nombre.x_six
                        course.nombre.seize_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.seize_rect.x == 400:

                        course.nombre.seize_rect.x = course.nombre.x_six
                        course.nombre.seize_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.seize_rect.x == 507:

                        course.nombre.seize_rect.x = course.nombre.x_six
                        course.nombre.seize_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.seize_rect.x == 610:

                        course.nombre.seize_rect.x = course.nombre.x_six
                        course.nombre.seize_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.seize_rect.x == 708:

                        course.nombre.seize_rect.x = course.nombre.x_six
                        course.nombre.seize_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.dixsept_rect.collidepoint(event.pos):

                    if course.nombre.dixsept_rect.x == 283:

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.dixsept_rect.x == 400:

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.dixsept_rect.x == 507:

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.dixsept_rect.x == 610:

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.dixsept_rect.x == 708:

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.dixhuit_rect.collidepoint(event.pos):

                    if course.nombre.dixhuit_rect.x == 283:

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.dixhuit_rect.x == 400:

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.dixhuit_rect.x == 507:

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.dixhuit_rect.x == 610:

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.dixhuit_rect.x == 708:

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.dixneuf_rect.collidepoint(event.pos):

                    if course.nombre.dixneuf_rect.x == 283:

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.dixneuf_rect.x == 400:

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.dixneuf_rect.x == 507:

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.dixneuf_rect.x == 610:

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.dixneuf_rect.x == 708:

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if course.nombre.vingt_rect.collidepoint(event.pos):

                    if course.nombre.vingt_rect.x == 283:

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas

                        is_premier_pris = False

                    elif course.nombre.vingt_rect.x == 400:

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas

                        is_deuxieme_pris = False

                    elif course.nombre.vingt_rect.x == 507:

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas

                        is_troisieme_pris = False

                    elif course.nombre.vingt_rect.x == 610:

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas

                        is_quatrieme_pris = False

                    elif course.nombre.vingt_rect.x == 708:

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas

                        is_cinqieme_pris = False

                if not is_premier_pris:

                    if course.nombre.un_rect.collidepoint(event.pos):

                        course.nombre.un_rect.x = 283
                        course.nombre.un_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.deux_rect.collidepoint(event.pos):

                        course.nombre.deux_rect.x = 283
                        course.nombre.deux_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.trois_rect.collidepoint(event.pos):

                        course.nombre.trois_rect.x = 283
                        course.nombre.trois_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.quatre_rect.collidepoint(event.pos):

                        course.nombre.quatre_rect.x = 283
                        course.nombre.quatre_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.cinq_rect.collidepoint(event.pos):

                        course.nombre.cinq_rect.x = 283
                        course.nombre.cinq_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.six_rect.collidepoint(event.pos):

                        course.nombre.six_rect.x = 283
                        course.nombre.six_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.sept_rect.collidepoint(event.pos):

                        course.nombre.sept_rect.x = 283
                        course.nombre.sept_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.huit_rect.collidepoint(event.pos):

                        course.nombre.huit_rect.x = 283
                        course.nombre.huit_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.neuf_rect.collidepoint(event.pos):

                        course.nombre.neuf_rect.x = 283
                        course.nombre.neuf_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.dix_rect.collidepoint(event.pos):

                        course.nombre.dix_rect.x = 283
                        course.nombre.dix_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.onze_rect.collidepoint(event.pos):
                        course.nombre.onze_rect.x = 283
                        course.nombre.onze_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.douze_rect.collidepoint(event.pos):
                        course.nombre.douze_rect.x = 283
                        course.nombre.douze_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.treize_rect.collidepoint(event.pos):
                        course.nombre.treize_rect.x = 283
                        course.nombre.treize_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.quatorze_rect.collidepoint(event.pos):
                        course.nombre.quatorze_rect.x = 283
                        course.nombre.quatorze_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.quinze_rect.collidepoint(event.pos):
                        course.nombre.quinze_rect.x = 283
                        course.nombre.quinze_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.seize_rect.collidepoint(event.pos):
                        course.nombre.seize_rect.x = 283
                        course.nombre.seize_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.dixsept_rect.collidepoint(event.pos):
                        course.nombre.dixsept_rect.x = 283
                        course.nombre.dixsept_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.dixhuit_rect.collidepoint(event.pos):
                        course.nombre.dixhuit_rect.x = 283
                        course.nombre.dixhuit_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.dixneuf_rect.collidepoint(event.pos):
                        course.nombre.dixneuf_rect.x = 283
                        course.nombre.dixneuf_rect.y = 502

                        is_premier_pris = True

                    if course.nombre.vingt_rect.collidepoint(event.pos):
                        course.nombre.vingt_rect.x = 285
                        course.nombre.vingt_rect.y = 502

                        is_premier_pris = True

                elif not is_deuxieme_pris:

                    if course.nombre.un_rect.collidepoint(event.pos):

                        course.nombre.un_rect.x = 400
                        course.nombre.un_rect.y = 542

                        is_deuxieme_pris = True

                    if course.nombre.deux_rect.collidepoint(event.pos):

                        course.nombre.deux_rect.x = 400
                        course.nombre.deux_rect.y = 542

                        is_deuxieme_pris = True

                    if course.nombre.trois_rect.collidepoint(event.pos):

                        course.nombre.trois_rect.x = 400
                        course.nombre.trois_rect.y = 542

                        is_deuxieme_pris = True

                    if course.nombre.quatre_rect.collidepoint(event.pos):

                        course.nombre.quatre_rect.x = 400
                        course.nombre.quatre_rect.y = 542

                        is_deuxieme_pris = True

                    if course.nombre.cinq_rect.collidepoint(event.pos):

                        course.nombre.cinq_rect.x = 400
                        course.nombre.cinq_rect.y = 542

                        is_deuxieme_pris = True

                    if course.nombre.six_rect.collidepoint(event.pos):

                        course.nombre.six_rect.x = 400
                        course.nombre.six_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.sept_rect.collidepoint(event.pos):

                        course.nombre.sept_rect.x = 400
                        course.nombre.sept_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.huit_rect.collidepoint(event.pos):

                        course.nombre.huit_rect.x = 400
                        course.nombre.huit_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.neuf_rect.collidepoint(event.pos):

                        course.nombre.neuf_rect.x = 400
                        course.nombre.neuf_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.dix_rect.collidepoint(event.pos):

                        course.nombre.dix_rect.x = 400
                        course.nombre.dix_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.onze_rect.collidepoint(event.pos):

                        course.nombre.onze_rect.x = 400
                        course.nombre.onze_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.douze_rect.collidepoint(event.pos):

                        course.nombre.douze_rect.x = 400
                        course.nombre.douze_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.treize_rect.collidepoint(event.pos):

                        course.nombre.treize_rect.x = 400
                        course.nombre.treize_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.quatorze_rect.collidepoint(event.pos):

                        course.nombre.quatorze_rect.x = 400
                        course.nombre.quatorze_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.quinze_rect.collidepoint(event.pos):

                        course.nombre.quinze_rect.x = 400
                        course.nombre.quinze_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.seize_rect.collidepoint(event.pos):

                        course.nombre.seize_rect.x = 400
                        course.nombre.seize_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.dixsept_rect.collidepoint(event.pos):

                        course.nombre.dixsept_rect.x = 400
                        course.nombre.dixsept_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.dixhuit_rect.collidepoint(event.pos):

                        course.nombre.dixhuit_rect.x = 400
                        course.nombre.dixhuit_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.dixneuf_rect.collidepoint(event.pos):

                        course.nombre.dixneuf_rect.x = 400
                        course.nombre.dixneuf_rect.y = 502

                        is_deuxieme_pris = True

                    if course.nombre.vingt_rect.collidepoint(event.pos):

                        course.nombre.vingt_rect.x = 400
                        course.nombre.vingt_rect.y = 502

                        is_deuxieme_pris = True

                elif not is_troisieme_pris:

                    if course.nombre.un_rect.collidepoint(event.pos):
                        course.nombre.un_rect.x = 507
                        course.nombre.un_rect.y = 542

                        is_troisieme_pris = True

                    if course.nombre.deux_rect.collidepoint(event.pos):

                        course.nombre.deux_rect.x = 507
                        course.nombre.deux_rect.y = 542

                        is_troisieme_pris = True

                    if course.nombre.trois_rect.collidepoint(event.pos):

                        course.nombre.trois_rect.x = 507
                        course.nombre.trois_rect.y = 542

                        is_troisieme_pris = True

                    if course.nombre.quatre_rect.collidepoint(event.pos):
                        course.nombre.quatre_rect.x = 507
                        course.nombre.quatre_rect.y = 542

                        is_troisieme_pris = True

                    if course.nombre.cinq_rect.collidepoint(event.pos):
                        course.nombre.cinq_rect.x = 507
                        course.nombre.cinq_rect.y = 542

                        is_troisieme_pris = True

                    if course.nombre.six_rect.collidepoint(event.pos):
                        course.nombre.six_rect.x = 507
                        course.nombre.six_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.sept_rect.collidepoint(event.pos):
                        course.nombre.sept_rect.x = 507
                        course.nombre.sept_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.huit_rect.collidepoint(event.pos):
                        course.nombre.huit_rect.x = 507
                        course.nombre.huit_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.neuf_rect.collidepoint(event.pos):
                        course.nombre.neuf_rect.x = 507
                        course.nombre.neuf_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.dix_rect.collidepoint(event.pos):
                        course.nombre.dix_rect.x = 507
                        course.nombre.dix_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.onze_rect.collidepoint(event.pos):
                        course.nombre.onze_rect.x = 507
                        course.nombre.onze_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.douze_rect.collidepoint(event.pos):
                        course.nombre.douze_rect.x = 507
                        course.nombre.douze_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.treize_rect.collidepoint(event.pos):
                        course.nombre.treize_rect.x = 507
                        course.nombre.treize_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.quatorze_rect.collidepoint(event.pos):
                        course.nombre.quatorze_rect.x = 507
                        course.nombre.quatorze_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.quinze_rect.collidepoint(event.pos):
                        course.nombre.quinze_rect.x = 507
                        course.nombre.quinze_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.seize_rect.collidepoint(event.pos):
                        course.nombre.seize_rect.x = 507
                        course.nombre.seize_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.dixsept_rect.collidepoint(event.pos):
                        course.nombre.dixsept_rect.x = 507
                        course.nombre.dixsept_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.dixhuit_rect.collidepoint(event.pos):
                        course.nombre.dixhuit_rect.x = 507
                        course.nombre.dixhuit_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.dixneuf_rect.collidepoint(event.pos):
                        course.nombre.dixneuf_rect.x = 507
                        course.nombre.dixneuf_rect.y = 502

                        is_troisieme_pris = True

                    if course.nombre.vingt_rect.collidepoint(event.pos):
                        course.nombre.vingt_rect.x = 507
                        course.nombre.vingt_rect.y = 502

                        is_troisieme_pris = True

                elif not is_quatrieme_pris:

                    if course.nombre.un_rect.collidepoint(event.pos):
                        course.nombre.un_rect.x = 610
                        course.nombre.un_rect.y = 542

                        is_quatrieme_pris = True

                    if course.nombre.deux_rect.collidepoint(event.pos):

                        course.nombre.deux_rect.x = 610
                        course.nombre.deux_rect.y = 542

                        is_quatrieme_pris = True

                    if course.nombre.trois_rect.collidepoint(event.pos):

                        course.nombre.trois_rect.x = 610
                        course.nombre.trois_rect.y = 542

                        is_quatrieme_pris = True

                    if course.nombre.quatre_rect.collidepoint(event.pos):
                        course.nombre.quatre_rect.x = 610
                        course.nombre.quatre_rect.y = 542

                        is_quatrieme_pris = True

                    if course.nombre.cinq_rect.collidepoint(event.pos):
                        course.nombre.cinq_rect.x = 610
                        course.nombre.cinq_rect.y = 542

                        is_quatrieme_pris = True

                    if course.nombre.six_rect.collidepoint(event.pos):
                        course.nombre.six_rect.x = 610
                        course.nombre.six_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.sept_rect.collidepoint(event.pos):
                        course.nombre.sept_rect.x = 610
                        course.nombre.sept_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.huit_rect.collidepoint(event.pos):
                        course.nombre.huit_rect.x = 610
                        course.nombre.huit_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.neuf_rect.collidepoint(event.pos):
                        course.nombre.neuf_rect.x = 610
                        course.nombre.neuf_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.dix_rect.collidepoint(event.pos):
                        course.nombre.dix_rect.x = 610
                        course.nombre.dix_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.onze_rect.collidepoint(event.pos):
                        course.nombre.onze_rect.x = 610
                        course.nombre.onze_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.douze_rect.collidepoint(event.pos):
                        course.nombre.douze_rect.x = 610
                        course.nombre.douze_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.treize_rect.collidepoint(event.pos):
                        course.nombre.treize_rect.x = 610
                        course.nombre.treize_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.quatorze_rect.collidepoint(event.pos):
                        course.nombre.quatorze_rect.x = 610
                        course.nombre.quatorze_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.quinze_rect.collidepoint(event.pos):
                        course.nombre.quinze_rect.x = 610
                        course.nombre.quinze_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.seize_rect.collidepoint(event.pos):
                        course.nombre.seize_rect.x = 610
                        course.nombre.seize_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.dixsept_rect.collidepoint(event.pos):
                        course.nombre.dixsept_rect.x = 610
                        course.nombre.dixsept_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.dixhuit_rect.collidepoint(event.pos):
                        course.nombre.dixhuit_rect.x = 610
                        course.nombre.dixhuit_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.dixneuf_rect.collidepoint(event.pos):
                        course.nombre.dixneuf_rect.x = 610
                        course.nombre.dixneuf_rect.y = 502

                        is_quatrieme_pris = True

                    if course.nombre.vingt_rect.collidepoint(event.pos):
                        course.nombre.vingt_rect.x = 610
                        course.nombre.vingt_rect.y = 502

                        is_quatrieme_pris = True

                elif not is_cinqieme_pris:

                    if course.nombre.un_rect.collidepoint(event.pos):
                        course.nombre.un_rect.x = 708
                        course.nombre.un_rect.y = 542

                        is_cinqieme_pris = True

                    if course.nombre.deux_rect.collidepoint(event.pos):

                        course.nombre.deux_rect.x = 708
                        course.nombre.deux_rect.y = 542

                        is_cinqieme_pris = True

                    if course.nombre.trois_rect.collidepoint(event.pos):

                        course.nombre.trois_rect.x = 708
                        course.nombre.trois_rect.y = 542

                        is_cinqieme_pris = True

                    if course.nombre.quatre_rect.collidepoint(event.pos):
                        course.nombre.quatre_rect.x = 708
                        course.nombre.quatre_rect.y = 542

                        is_cinqieme_pris = True

                    if course.nombre.cinq_rect.collidepoint(event.pos):
                        course.nombre.cinq_rect.x = 708
                        course.nombre.cinq_rect.y = 542

                        is_cinqieme_pris = True

                    if course.nombre.six_rect.collidepoint(event.pos):
                        course.nombre.six_rect.x = 708
                        course.nombre.six_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.sept_rect.collidepoint(event.pos):
                        course.nombre.sept_rect.x = 708
                        course.nombre.sept_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.huit_rect.collidepoint(event.pos):
                        course.nombre.huit_rect.x = 708
                        course.nombre.huit_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.neuf_rect.collidepoint(event.pos):
                        course.nombre.neuf_rect.x = 708
                        course.nombre.neuf_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.dix_rect.collidepoint(event.pos):
                        course.nombre.dix_rect.x = 708
                        course.nombre.dix_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.onze_rect.collidepoint(event.pos):
                        course.nombre.onze_rect.x = 708
                        course.nombre.onze_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.douze_rect.collidepoint(event.pos):
                        course.nombre.douze_rect.x = 708
                        course.nombre.douze_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.treize_rect.collidepoint(event.pos):
                        course.nombre.treize_rect.x = 708
                        course.nombre.treize_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.quatorze_rect.collidepoint(event.pos):
                        course.nombre.quatorze_rect.x = 708
                        course.nombre.quatorze_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.quinze_rect.collidepoint(event.pos):
                        course.nombre.quinze_rect.x = 708
                        course.nombre.quinze_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.seize_rect.collidepoint(event.pos):
                        course.nombre.seize_rect.x = 708
                        course.nombre.seize_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.dixsept_rect.collidepoint(event.pos):
                        course.nombre.dixsept_rect.x = 708
                        course.nombre.dixsept_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.dixhuit_rect.collidepoint(event.pos):
                        course.nombre.dixhuit_rect.x = 708
                        course.nombre.dixhuit_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.dixneuf_rect.collidepoint(event.pos):
                        course.nombre.dixneuf_rect.x = 708
                        course.nombre.dixneuf_rect.y = 502

                        is_cinqieme_pris = True

                    if course.nombre.vingt_rect.collidepoint(event.pos):
                        course.nombre.vingt_rect.x = 708
                        course.nombre.vingt_rect.y = 502

                        is_cinqieme_pris = True

                """if course.nombre.un_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.un_rect.x = 283
                        course.nombre.un_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.un_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                            course.nombre.un_rect.x = course.nombre.x_un
                            course.nombre.un_rect.y = course.nombre.y_haut

                if course.nombre.deux_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.deux_rect.x = 283
                        course.nombre.deux_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.deux_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.deux_rect.x = course.nombre.x_deux
                        course.nombre.deux_rect.y = course.nombre.y_haut

                if course.nombre.trois_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.trois_rect.x = 283
                        course.nombre.trois_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.trois_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.trois_rect.x = course.nombre.x_trois
                        course.nombre.trois_rect.y = course.nombre.y_haut

                if course.nombre.quatre_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.quatre_rect.x = 283
                        course.nombre.quatre_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.quatre_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.quatre_rect.x = course.nombre.x_quatre
                        course.nombre.quatre_rect.y = course.nombre.y_haut

                if course.nombre.cinq_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.cinq_rect.x = 283
                        course.nombre.cinq_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.cinq_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.cinq_rect.x = course.nombre.x_cinq
                        course.nombre.cinq_rect.y = course.nombre.y_haut

                if course.nombre.six_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.six_rect.x = 283
                        course.nombre.six_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.six_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                            course.nombre.six_rect.x = course.nombre.x_six
                            course.nombre.six_rect.y = course.nombre.y_haut

                if course.nombre.sept_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.sept_rect.x = 283
                        course.nombre.sept_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.sept_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.sept_rect.x = course.nombre.x_sept
                        course.nombre.sept_rect.y = course.nombre.y_haut

                if course.nombre.huit_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.huit_rect.x = 283
                        course.nombre.huit_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.huit_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.huit_rect.x = course.nombre.x_huit
                        course.nombre.huit_rect.y = course.nombre.y_haut

                if course.nombre.neuf_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.neuf_rect.x = 283
                        course.nombre.neuf_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.neuf_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.neuf_rect.x = course.nombre.x_neuf
                        course.nombre.neuf_rect.y = course.nombre.y_haut

                if course.nombre.dix_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.dix_rect.x = 283
                        course.nombre.dix_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.dix_rect.y != course.nombre.y_haut:
                            is_premier_pris = False

                        course.nombre.dix_rect.x = course.nombre.x_dix
                        course.nombre.dix_rect.y = course.nombre.y_haut

                if course.nombre.onze_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.onze_rect.x = 283
                        course.nombre.onze_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.onze_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                            course.nombre.onze_rect.x = course.nombre.x_un
                            course.nombre.onze_rect.y = course.nombre.y_bas

                if course.nombre.douze_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.douze_rect.x = 283
                        course.nombre.douze_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.douze_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.douze_rect.x = course.nombre.x_deux
                        course.nombre.douze_rect.y = course.nombre.y_bas

                if course.nombre.treize_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.treize_rect.x = 283
                        course.nombre.treize_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.treize_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.treize_rect.x = course.nombre.x_trois
                        course.nombre.treize_rect.y = course.nombre.y_bas

                if course.nombre.quatorze_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.quatorze_rect.x = 283
                        course.nombre.quatorze_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.quatorze_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.quatorze_rect.x = course.nombre.x_quatre
                        course.nombre.quatorze_rect.y = course.nombre.y_bas

                if course.nombre.quinze_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.quinze_rect.x = 283
                        course.nombre.quinze_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.quinze_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.quinze_rect.x = course.nombre.x_cinq
                        course.nombre.quinze_rect.y = course.nombre.y_bas

                if course.nombre.seize_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.seize_rect.x = 283
                        course.nombre.seize_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.seize_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                            course.nombre.seize_rect.x = course.nombre.x_six
                            course.nombre.seize_rect.y = course.nombre.y_bas

                if course.nombre.dixsept_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.dixsept_rect.x = 283
                        course.nombre.dixsept_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.dixsept_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.dixsept_rect.x = course.nombre.x_sept
                        course.nombre.dixsept_rect.y = course.nombre.y_bas

                if course.nombre.dixhuit_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.dixhuit_rect.x = 283
                        course.nombre.dixhuit_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.dixhuit_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.dixhuit_rect.x = course.nombre.x_huit
                        course.nombre.dixhuit_rect.y = course.nombre.y_bas

                if course.nombre.dixneuf_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.dixneuf_rect.x = 283
                        course.nombre.dixneuf_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.dixneuf_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.dixneuf_rect.x = course.nombre.x_neuf
                        course.nombre.dixneuf_rect.y = course.nombre.y_bas

                if course.nombre.vingt_rect.collidepoint(event.pos):

                    if not is_premier_pris:

                        course.nombre.vingt_rect.x = 285
                        course.nombre.vingt_rect.y = 502

                        is_premier_pris = True

                    else:
                        if course.nombre.vingt_rect.y != course.nombre.y_bas:
                            is_premier_pris = False

                        course.nombre.vingt_rect.x = course.nombre.x_dix
                        course.nombre.vingt_rect.y = course.nombre.y_bas"""
