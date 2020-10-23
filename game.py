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
        self.money = 50

        self.color = (191, 191, 190)
        self.font = pygame.font.SysFont("Showcard Gothic", 30)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = 995 - self.t_money_rect.width
        self.t_money_rect.y = 38

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

        self.coins_image = pygame.image.load("assets/png/coins.png")
        self.coins_image_rect = self.coins_image.get_rect()
        self.coins_image_rect.x = 1000
        self.coins_image_rect.y = 20

# 2- Ici j'initialise tous ce qui il y'aura pour le menu choose.
        self.choose_image = pygame.image.load("assets/png/choose_background.png")
        self.choose_image_rect = self.choose_image.get_rect()
        self.choose_image_rect.x = 0
        self.choose_image_rect.y = 0

        self.choix_milieu_image = pygame.image.load("assets/png/choose_milieu.png")
        self.choix_milieu_image_rect = self.choix_milieu_image.get_rect()
        self.choix_milieu_image_rect.x = 1080/2 - self.choix_milieu_image_rect.width/2
        self.choix_milieu_image_rect.y = 105

        self.choix_gauche_image = pygame.image.load("assets/png/choose_left.png")
        self.choix_gauche_image_rect = self.choix_gauche_image.get_rect()
        self.choix_gauche_image_rect.x = 19
        self.choix_gauche_image_rect.y = 105

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

        self.coins_image_rect.x = 1000
        self.coins_image_rect.y = 20

        screen.blit(self.coins_image, self.coins_image_rect)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = 995 - self.t_money_rect.width
        self.t_money_rect.y = 38

        screen.blit(self.t_money, self.t_money_rect)

        screen.blit(self.pause_play_image, self.pause_play_image_rect)
        screen.blit(self.menu_button_image, self.pause_menu_button_image_rect)
        screen.blit(self.quit_button_image, self.quit_button_image_rect)

    def pos_money(self,screen, pos_x, pos_y):

        self.coins_image_rect.x = pos_x
        self.coins_image_rect.y = pos_y - 18

        screen.blit(self.coins_image, self.coins_image_rect)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = pos_x - 5 - self.t_money_rect.width
        self.t_money_rect.y = pos_y

        screen.blit(self.t_money, self.t_money_rect)

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
        screen.blit(self.choix_gauche_image, self.choix_gauche_image_rect)
        
        screen.blit(self.coins_image, self.coins_image_rect)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = 995 - self.t_money_rect.width
        self.t_money_rect.y = 38

        screen.blit(self.t_money, self.t_money_rect)
