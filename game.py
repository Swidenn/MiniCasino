# coding: utf-8

"""
Développer par DELIOT Yllan
Terminal Générale n°9
17/10/2020

But de ce fichier:
Code d'initialisation du jeu en lui même (dédié que
pour ça) il permet en t'autre de changer globalement
tous ce qui a un rapport avec le jeu.
"""
import pygame

class Game:
    """
    Class: Du jeu en lui même (dédié que
    pour ça) il permet en t'autre de changer globalement
    tous ce qui a un rapport avec le jeu.
    """

    def __init__(self):

        self.press = {}

# 1- Ici j'initialise tous ce qui il y'aura pour le menu pause.
        self.pause_image = pygame.image.load("assets/png/pause_background.png")
        self.pause_image_rect = self.pause_image.get_rect()
        self.pause_image_rect.x = 0
        self.pause_image_rect.y = 0

        self.pause_play_image = pygame.image.load("assets/png/play_pause.png")
        self.pause_play_image_rect = self.pause_play_image.get_rect()
        self.pause_play_image_rect.x = 1080/2 - self.pause_play_image_rect.width
        self.pause_play_image_rect.y = 490

        self.menu_button_image = pygame.image.load("assets/png/menu_button.png")
        self.pause_menu_button_image_rect = self.menu_button_image.get_rect()
        self.pause_menu_button_image_rect.x = 1080/2
        self.pause_menu_button_image_rect.y = 490

        self.quit_button_image = pygame.image.load("assets/png/quit_button.png")
        self.quit_button_image_rect = self.quit_button_image.get_rect()
        self.quit_button_image_rect.x = 1080/2 - self.quit_button_image_rect.width/2
        self.quit_button_image_rect.y = 590

# 2- Ici j'initialise tous ce qui il y'aura pour le menu choose.
        self.choose_image = pygame.image.load("assets/png/choose_background.png")
        self.choose_image_rect = self.choose_image.get_rect()
        self.choose_image_rect.x = 0
        self.choose_image_rect.y = 0

        self.choix_milieu_image = pygame.image.load("assets/png/choose_milieu.png")
        self.choix_milieu_image_rect = self.choix_milieu_image.get_rect()
        self.choix_milieu_image_rect.x = 1080/2 - self.choix_milieu_image_rect.width/2
        self.choix_milieu_image_rect.y = 106

# 3- Ici c'est les booléens qui indiqueront l'état dans lequel le jeu se trouve
        self.is_menu = True
        self.is_choose_menu = False
        self.is_paused = False
        self.is_game = False
        self.is_course_epique = False

    def paused(self, screen):
        """
        Fonction d'affichage du menu pause

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        self.is_game = False

        screen.blit(self.pause_image, self.pause_image_rect)
        screen.blit(self.pause_play_image, self.pause_play_image_rect)
        screen.blit(self.menu_button_image, self.pause_menu_button_image_rect)
        screen.blit(self.quit_button_image, self.quit_button_image_rect)

    def choose(self, screen):
        """
        Fonction d'affichage du menu choose

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        self.is_menu = False

        screen.blit(self.choose_image, self.choose_image_rect)
        screen.blit(self.choix_milieu_image, self.choix_milieu_image_rect)
