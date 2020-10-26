# coding: utf-8

"""
Développer par GAROFALO Clément
Recomposé par DELIOT Yllan
Terminal Générale n°9
23/10/2020

But de ce fichier:
Code ayant juste les nombres utilisé pour les cheavaux
"""
import pygame
import numpy as np
from game import NoMoney


class Emplacement(pygame.sprite.Sprite):
    """
    classe qui place les carte sur la Machine à Trous
    """

    def __init__(self, pos_x):
        super().__init__()
        self.image = pygame.image.load("assets/png/seven.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = 159

    def setimg(self, image):
        self.image = image


class MachineATrous:
    """
    classe du minio jeu Machine à Trous
    """

    def __init__(self):

        self.machine_is_lunch = False

        self.nomoney = NoMoney()

        self.machine_image = pygame.image.load("assets/png/fond_machineatrous.png")
        self.machine_image_rect = self.machine_image.get_rect()
        self.machine_image_rect.x = 0
        self.machine_image_rect.y = 0

        self.win_image = pygame.image.load("assets/png/machine_win.png")
        self.win_image_rect = self.win_image.get_rect()
        self.win_image_rect.x = 114
        self.win_image_rect.y = 415

        self.lose_image = pygame.image.load("assets/png/machine_losed.png")
        self.lose_image_rect = self.lose_image.get_rect()
        self.lose_image_rect.x = 114
        self.lose_image_rect.y = 415

        self.compte = 0
        self.t = False
        self.z = 0

        self.alea = []

        self.emplacements = pygame.sprite.Group()

        self.elements = ["cerise", "banane", "ananas", "diamant", "7"]
        self.proba = [0.385, 0.27, 0.19, 0.115, 0.04]
        'self.proba = [0.05, 0.05, 0.05, 0.05, 0.8]'

        self.dict = {
            "7": pygame.image.load("assets/png/seven.png"),
            "diamant": pygame.image.load("assets/png/diamant.png"),
            "ananas": pygame.image.load("assets/png/ananas.png"),
            "banane": pygame.image.load("assets/png/banane.png"),
            "cerise": pygame.image.load("assets/png/cerise.png"),
        }
        self.emplacement_gauche = Emplacement(130)
        self.emplacement_milieu = Emplacement(242)
        self.emplacement_droit = Emplacement(354)

        self.emplacements.add(self.emplacement_gauche)
        self.emplacements.add(self.emplacement_milieu)
        self.emplacements.add(self.emplacement_droit)

    def start_machine(self, screen, game):
        """
        fonction qui initialise le mini jeu Machine à Trous

        :param screen:
        surface d'affichage

        :param game:
        class game

        :return:
        """

        screen.blit(self.machine_image, self.machine_image_rect)
        self.emplacements.draw(screen)

        game.pos_money(screen, 950, 620)

        if self.t:
            self.nomoney.affichage_nomoney(screen, 183, 550, 20)

            for i in range(1000):
                self.z += 1
            if self.z >= 100000:
                self.t = False

        if self.compte == 1:
            screen.blit(self.win_image, self.win_image_rect)

        else:
            screen.blit(self.lose_image, self.lose_image_rect)

    def spin(self, game):
        """
        fonction qui verifie si on gagne ou pas

        :param game:
        class game

        :return:
        """

        game.money -= 3

        self.alea = np.random.choice(self.elements, 3, p=self.proba)

        self.emplacement_gauche.setimg(self.dict[self.alea[0]])
        self.emplacement_milieu.setimg(self.dict[self.alea[1]])
        self.emplacement_droit.setimg(self.dict[self.alea[2]])

        if self.alea[0] == self.alea[1] == self.alea[2]:

            if self.alea[0] == "7":
                game.money += 5000
                self.compte = 1

            elif self.alea[0] == "diamant":
                game.money += 300
                self.compte = 1

            elif self.alea[0] == "ananas":
                game.money += 20
                self.compte = 1

            elif self.alea[0] == "banane":
                game.money += 5
                self.compte = 1

            elif self.alea[0] == "cerise":
                game.money += 3
                self.compte = 1

        else:
            self.compte = 0
