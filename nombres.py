# coding: utf-8

"""
Développer par DELIOT Yllan
Terminal Générale n°9
18/10/2020

But de ce fichier:
Code ayant juste les nombres utilisé pour les cheavaux
"""
import pygame


class Nombre:

    def __init__(self):

        self.y_haut = 34
        self.y_bas = 161

        self.x_un = 44
        self.x_deux = 144
        self.x_trois = 243
        self.x_quatre = 342
        self.x_cinq = 442
        self.x_six = 544
        self.x_sept = 644
        self.x_huit = 743
        self.x_neuf = 843
        self.x_dix = 942

        # Nombre en haut
        self.un_tampon = pygame.image.load("assets/png/nombres/1.png")
        self.un_image = self.un_tampon
        self.un_rect = self.un_image.get_rect()
        self.un_rect.x = self.x_un
        self.un_rect.y = self.y_haut


        self.deux_tampon = pygame.image.load("assets/png/nombres/2.png")
        self.deux_image = self.deux_tampon
        self.deux_rect = self.deux_image.get_rect()
        self.deux_rect.x = self.x_deux
        self.deux_rect.y = self.y_haut

        self.trois_tampon = pygame.image.load("assets/png/nombres/3.png")
        self.trois_image = self.trois_tampon
        self.trois_rect = self.trois_image.get_rect()
        self.trois_rect.x = self.x_trois
        self.trois_rect.y = self.y_haut

        self.quatre_tampon = pygame.image.load("assets/png/nombres/4.png")
        self.quatre_image = self.quatre_tampon
        self.quatre_rect = self.quatre_image.get_rect()
        self.quatre_rect.x = self.x_quatre
        self.quatre_rect.y = self.y_haut

        self.cinq_tampon = pygame.image.load("assets/png/nombres/5.png")
        self.cinq_image = self.cinq_tampon
        self.cinq_rect = self.cinq_image.get_rect()
        self.cinq_rect.x = self.x_cinq
        self.cinq_rect.y = self.y_haut

        self.six_tampon = pygame.image.load("assets/png/nombres/6.png")
        self.six_image = self.six_tampon
        self.six_rect = self.six_image.get_rect()
        self.six_rect.x = self.x_six
        self.six_rect.y = self.y_haut

        self.sept_tampon = pygame.image.load("assets/png/nombres/7.png")
        self.sept_image = self.sept_tampon
        self.sept_rect = self.sept_image.get_rect()
        self.sept_rect.x = self.x_sept
        self.sept_rect.y = self.y_haut

        self.huit_tampon = pygame.image.load("assets/png/nombres/8.png")
        self.huit_image = self.huit_tampon
        self.huit_rect = self.huit_image.get_rect()
        self.huit_rect.x = self.x_huit
        self.huit_rect.y = self.y_haut

        self.neuf_tampon = pygame.image.load("assets/png/nombres/9.png")
        self.neuf_image = self.neuf_tampon
        self.neuf_rect = self.neuf_image.get_rect()
        self.neuf_rect.x = self.x_neuf
        self.neuf_rect.y = self.y_haut

        self.dix_tampon = pygame.image.load("assets/png/nombres/10.png")
        self.dix_image = self.dix_tampon
        self.dix_rect = self.dix_image.get_rect()
        self.dix_rect.x = self.x_dix
        self.dix_rect.y = self.y_haut

        # Nombre en bas
        self.onze_tampon = pygame.image.load("assets/png/nombres/11.png")
        self.onze_image = self.onze_tampon
        self.onze_rect = self.onze_image.get_rect()
        self.onze_rect.x = self.x_un
        self.onze_rect.y = self.y_bas

        self.douze_tampon = pygame.image.load("assets/png/nombres/12.png")
        self.douze_image = self.douze_tampon
        self.douze_rect = self.douze_image.get_rect()
        self.douze_rect.x = self.x_deux
        self.douze_rect.y = self.y_bas

        self.treize_tampon = pygame.image.load("assets/png/nombres/13.png")
        self.treize_image = self.treize_tampon
        self.treize_rect = self.treize_image.get_rect()
        self.treize_rect.x = self.x_trois
        self.treize_rect.y = self.y_bas

        self.quatorze_tampon = pygame.image.load("assets/png/nombres/14.png")
        self.quatorze_image = self.quatorze_tampon
        self.quatorze_rect = self.quatorze_image.get_rect()
        self.quatorze_rect.x = self.x_quatre
        self.quatorze_rect.y = self.y_bas

        self.quinze_tampon = pygame.image.load("assets/png/nombres/15.png")
        self.quinze_image = self.quinze_tampon
        self.quinze_rect = self.quinze_image.get_rect()
        self.quinze_rect.x = self.x_cinq
        self.quinze_rect.y = self.y_bas

        self.seize_tampon = pygame.image.load("assets/png/nombres/16.png")
        self.seize_image = self.seize_tampon
        self.seize_rect = self.seize_image.get_rect()
        self.seize_rect.x = self.x_six
        self.seize_rect.y = self.y_bas

        self.dixsept_tampon = pygame.image.load("assets/png/nombres/17.png")
        self.dixsept_image = self.dixsept_tampon
        self.dixsept_rect = self.dixsept_image.get_rect()
        self.dixsept_rect.x = self.x_sept
        self.dixsept_rect.y = self.y_bas

        self.dixhuit_tampon = pygame.image.load("assets/png/nombres/18.png")
        self.dixhuit_image = self.dixhuit_tampon
        self.dixhuit_rect = self.dixhuit_image.get_rect()
        self.dixhuit_rect.x = self.x_huit
        self.dixhuit_rect.y = self.y_bas

        self.dixneuf_tampon = pygame.image.load("assets/png/nombres/19.png")
        self.dixneuf_image = self.dixneuf_tampon
        self.dixneuf_rect = self.dixneuf_image.get_rect()
        self.dixneuf_rect.x = self.x_neuf
        self.dixneuf_rect.y = self.y_bas

        self.vingt_tampon = pygame.image.load("assets/png/nombres/20.png")
        self.vingt_image = self.vingt_tampon
        self.vingt_rect = self.vingt_image.get_rect()
        self.vingt_rect.x = self.x_dix
        self.vingt_rect.y = self.y_bas

        self.scale_d = (85, 85)
        self.scale_t = (80, 80)
        self.scale = (77, 77)

    def nb_position(self, screen):
        """
        fonction d'affichage des nombres de 1 à 20

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        screen.blit(self.un_image, self.un_rect)
        screen.blit(self.deux_image, self.deux_rect)
        screen.blit(self.trois_image, self.trois_rect)
        screen.blit(self.quatre_image, self.quatre_rect)
        screen.blit(self.cinq_image, self.cinq_rect)
        screen.blit(self.six_image, self.six_rect)
        screen.blit(self.sept_image, self.sept_rect)
        screen.blit(self.huit_image, self.huit_rect)
        screen.blit(self.neuf_image, self.neuf_rect)
        screen.blit(self.dix_image, self.dix_rect)
        screen.blit(self.onze_image, self.onze_rect)
        screen.blit(self.douze_image, self.douze_rect)
        screen.blit(self.treize_image, self.treize_rect)
        screen.blit(self.quatorze_image, self.quatorze_rect)
        screen.blit(self.quinze_image, self.quinze_rect)
        screen.blit(self.seize_image, self.seize_rect)
        screen.blit(self.dixsept_image, self.dixsept_rect)
        screen.blit(self.dixhuit_image, self.dixhuit_rect)
        screen.blit(self.dixneuf_image, self.dixneuf_rect)
        screen.blit(self.vingt_image, self.vingt_rect)
