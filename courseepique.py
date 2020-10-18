# coding: utf-8
import pygame
from modules.course import course
from nombres import Nombre
from game import Game

class Course():

    def __init__(self):

        self.is_rules = True
        self.is_lunch = False

        self.game = Game()
        self.nombre = Nombre()

# 1- Règles de la course de chevaux!
        self.regles_image = pygame.image.load("assets/png/regles_cheveaux.png")
        self.regles_image_rect = self.regles_image.get_rect()
        self.regles_image_rect.x = 0
        self.regles_image_rect.y = 0

        self.ok_image = pygame.image.load("assets/png/ok_button.png")
        self.ok_image_rect = self.ok_image.get_rect()
        self.ok_image_rect.x = 1080/2 - self.ok_image_rect.width/2
        self.ok_image_rect.y = 590

# 2- Grille de mise
        self.selection_image = pygame.image.load("assets/png/selection_cheveaux.png")
        self.selection_image_rect = self.selection_image.get_rect()
        self.selection_image_rect.x = 0
        self.selection_image_rect.y = 0

        self.position_image = pygame.image.load("assets/png/position_carte.png")
        self.position_image_rect = self.position_image.get_rect()
        self.position_image_rect.x = 1080/2 - self.position_image_rect.width/2
        self.position_image_rect.y = 495

        self.confirm_image = pygame.image.load("assets/png/confirm_button.png")
        self.confirm_image_rect = self.confirm_image.get_rect()
        self.confirm_image_rect.x = 475
        self.confirm_image_rect.y = 620

    def rule(self, screen):
        """
        fonction qui lance les regles de la course

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        if self.is_rules:

            screen.blit(self.regles_image, self.regles_image_rect)
            screen.blit(self.ok_image, self.ok_image_rect)

    def lunch(self, screen):
        """
        fonction qui lance la grille de choix

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        if self.is_lunch:

            screen.blit(self.selection_image, self.selection_image_rect)
            self.nombre.nb_position(screen)
            screen.blit(self.position_image, self.position_image_rect)
            screen.blit(self.confirm_image, self.confirm_image_rect)
