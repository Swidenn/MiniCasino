# coding: utf-8

"""
Développer par DELIOT Yllan
Terminal Générale n°9
19/10/2020

But de ce fichier:
Code ayant le jeu course de cheveaux en lui même
"""
import time
from nombres import Nombre
from modules.tirage import tirage
from modules.course import course
from game import *


class Cheval(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.velocity = 1

        self.fin = False

        self.chaval_image = pygame.image.load("assets/png/cheval.png")
        self.chaval_image_rect = self.chaval_image.get_rect()
        self.chaval_image_rect.x = 0
        self.chaval_image_rect.y = 78

    def move_cheval(self):

        if self.chaval_image_rect.x < 1035 - self.chaval_image_rect.width:
            self.chaval_image_rect.x += self.velocity

        if self.chaval_image_rect.x >= 1035 - self.chaval_image_rect.width:
            self.fin = True


class Course:

    def __init__(self):

        self.is_rules = True
        self.is_lunch = False
        self.is_validation = False

        self.game = Game()
        self.nombre = Nombre()
        self.cheval = Cheval()
        self.nomoney = NoMoney()

        self.is_premier_pris = False
        self.is_deuxieme_pris = False
        self.is_troisieme_pris = False
        self.is_quatrieme_pris = False
        self.is_cinqieme_pris = False

        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0

        self.suite = tirage()

        self.t = False
        self.z = 0

        self.nb_resultat = course(self.c1, self.c2, self.c3, self.c4, self.c5, self.suite)

        self.nb_resultat = 0
        self.suite = []

        self.compteur = 0

        # 1- Règles de la course de chevaux!
        self.regles_image = pygame.image.load("assets/png/regles_cheveaux.png")
        self.regles_image_rect = self.regles_image.get_rect()
        self.regles_image_rect.x = 0
        self.regles_image_rect.y = 0

        self.ok_image = pygame.image.load("assets/png/ok_button.png")
        self.ok_image_rect = self.ok_image.get_rect()
        self.ok_image_rect.x = 1080 / 2 - self.ok_image_rect.width / 2
        self.ok_image_rect.y = 590

        # 2- Grille de mise
        self.selection_image = pygame.image.load("assets/png/selection_cheveaux.png")
        self.selection_image_rect = self.selection_image.get_rect()
        self.selection_image_rect.x = 0
        self.selection_image_rect.y = 0

        self.position_image = pygame.image.load("assets/png/position_carte.png")
        self.position_image_rect = self.position_image.get_rect()
        self.position_image_rect.x = 343
        self.position_image_rect.y = 487

        self.confirm_image = pygame.image.load("assets/png/confirm_button.png")
        self.confirm_image_rect = self.confirm_image.get_rect()
        self.confirm_image_rect.x = 475
        self.confirm_image_rect.y = 620

        # 3- Course de cheveaux
        self.course_image = pygame.image.load("assets/png/fond_course.png")
        self.course_image_rect = self.course_image.get_rect()
        self.course_image_rect.x = 0
        self.course_image_rect.y = 0

        # 4- losed
        self.lose_image = pygame.image.load("assets/png/fond_lose.png")
        self.lose_image_rect = self.lose_image.get_rect()
        self.lose_image_rect.x = 0
        self.lose_image_rect.y = 0

        self.retry_image = pygame.image.load("assets/png/menu_button.png")
        self.retry_image_rect = self.retry_image.get_rect()
        self.retry_image_rect.x = 1080/2 - self.retry_image_rect.width
        self.retry_image_rect.y = 490

        self.quit_img = pygame.image.load("assets/png/quit_button.png")
        self.quit_img_rect = self.quit_img.get_rect()
        self.quit_img_rect.x = 1080/2
        self.quit_img_rect.y = 490

        self.logo = pygame.image.load("assets/png/coins.png")
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.x = 550
        self.logo_rect.y = 350


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

            self.cheval.move_cheval()

    def lunch(self, screen, game):
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

            game.pos_money(screen, 1000, 655)

        if self.t:
            self.nomoney.affichage_nomoney(screen, 422, 600, 25)

            for i in range (1000):
                self.z += 1
            if self.z >= 100000:
                self.t = False

    def validation(self, screen):

        if self.is_validation:
            screen.blit(self.course_image, self.course_image_rect)
            screen.blit(self.cheval.chaval_image, self.cheval.chaval_image_rect)

            self.cheval.move_cheval()

            if self.cheval.fin:
                screen.blit(self.lose_image, self.lose_image_rect)
                screen.blit(self.quit_img, self.quit_img_rect)
                screen.blit(self.retry_image, self.retry_image_rect)

                screen.blit(self.logo, self.logo_rect)

                self.perdu = self.game.font.render("-10", 1, self.game.color)
                self.perdu_rect = self.perdu.get_rect()
                self.perdu_rect.x = 545 - self.perdu_rect.width
                self.perdu_rect.y = 368

                screen.blit(self.perdu, self.perdu_rect)

    def test_position(self, game):

        if self.nb_resultat == 1:
            game.money += 1000000
            pygame.time.wait(10000)

        elif self.nb_resultat == 2:
            game.money += 300000
            pygame.time.wait(10000)

        elif self.nb_resultat == 3:
            game.money += 150000
            pygame.time.wait(10000)

        elif self.nb_resultat == 4:
            game.money += 10000
            pygame.time.wait(10000)

        elif self.nb_resultat == 5:
            game.money += 150
            pygame.time.wait(10000)

    def grille_selection(self, event, game):

        if self.nombre.un_rect.collidepoint(event.pos):

            if self.nombre.un_rect.x == 277:

                self.nombre.un_rect.x = self.nombre.x_un
                self.nombre.un_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.un_rect.x == 384:

                self.nombre.un_rect.x = self.nombre.x_un
                self.nombre.un_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.un_rect.x == 489:

                self.nombre.un_rect.x = self.nombre.x_un
                self.nombre.un_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.un_rect.x == 595:

                self.nombre.un_rect.x = self.nombre.x_un
                self.nombre.un_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.un_rect.x == 702:

                self.nombre.un_rect.x = self.nombre.x_un
                self.nombre.un_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.deux_rect.collidepoint(event.pos):

            if self.nombre.deux_rect.x == 277:

                self.nombre.deux_rect.x = self.nombre.x_deux
                self.nombre.deux_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.deux_rect.x == 384:

                self.nombre.deux_rect.x = self.nombre.x_deux
                self.nombre.deux_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.deux_rect.x == 489:

                self.nombre.deux_rect.x = self.nombre.x_deux
                self.nombre.deux_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.deux_rect.x == 595:

                self.nombre.deux_rect.x = self.nombre.x_deux
                self.nombre.deux_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.deux_rect.x == 702:

                self.nombre.deux_rect.x = self.nombre.x_deux
                self.nombre.deux_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.trois_rect.collidepoint(event.pos):

            if self.nombre.trois_rect.x == 277:

                self.nombre.trois_rect.x = self.nombre.x_trois
                self.nombre.trois_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.trois_rect.x == 384:

                self.nombre.trois_rect.x = self.nombre.x_trois
                self.nombre.trois_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.trois_rect.x == 489:

                self.nombre.trois_rect.x = self.nombre.x_trois
                self.nombre.trois_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.trois_rect.x == 595:

                self.nombre.trois_rect.x = self.nombre.x_trois
                self.nombre.trois_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.trois_rect.x == 702:

                self.nombre.trois_rect.x = self.nombre.x_trois
                self.nombre.trois_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.quatre_rect.collidepoint(event.pos):

            if self.nombre.quatre_rect.x == 277:

                self.nombre.quatre_rect.x = self.nombre.x_quatre
                self.nombre.quatre_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.quatre_rect.x == 384:

                self.nombre.quatre_rect.x = self.nombre.x_quatre
                self.nombre.quatre_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.quatre_rect.x == 489:

                self.nombre.quatre_rect.x = self.nombre.x_quatre
                self.nombre.quatre_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.quatre_rect.x == 595:

                self.nombre.quatre_rect.x = self.nombre.x_quatre
                self.nombre.quatre_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.quatre_rect.x == 702:

                self.nombre.quatre_rect.x = self.nombre.x_quatre
                self.nombre.quatre_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.cinq_rect.collidepoint(event.pos):

            if self.nombre.cinq_rect.x == 277:

                self.nombre.cinq_rect.x = self.nombre.x_cinq
                self.nombre.cinq_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.cinq_rect.x == 384:

                self.nombre.cinq_rect.x = self.nombre.x_cinq
                self.nombre.cinq_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.cinq_rect.x == 489:

                self.nombre.cinq_rect.x = self.nombre.x_cinq
                self.nombre.cinq_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.cinq_rect.x == 595:

                self.nombre.cinq_rect.x = self.nombre.x_cinq
                self.nombre.cinq_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.cinq_rect.x == 702:

                self.nombre.cinq_rect.x = self.nombre.x_cinq
                self.nombre.cinq_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.six_rect.collidepoint(event.pos):

            if self.nombre.six_rect.x == 277:

                self.nombre.six_rect.x = self.nombre.x_six
                self.nombre.six_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.six_rect.x == 384:

                self.nombre.six_rect.x = self.nombre.x_six
                self.nombre.six_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.six_rect.x == 489:

                self.nombre.six_rect.x = self.nombre.x_six
                self.nombre.six_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.six_rect.x == 595:

                self.nombre.six_rect.x = self.nombre.x_six
                self.nombre.six_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.six_rect.x == 702:

                self.nombre.six_rect.x = self.nombre.x_six
                self.nombre.six_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.sept_rect.collidepoint(event.pos):

            if self.nombre.sept_rect.x == 277:

                self.nombre.sept_rect.x = self.nombre.x_sept
                self.nombre.sept_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.sept_rect.x == 384:

                self.nombre.sept_rect.x = self.nombre.x_sept
                self.nombre.sept_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.sept_rect.x == 489:

                self.nombre.sept_rect.x = self.nombre.x_sept
                self.nombre.sept_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.sept_rect.x == 595:

                self.nombre.sept_rect.x = self.nombre.x_sept
                self.nombre.sept_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.sept_rect.x == 702:

                self.nombre.sept_rect.x = self.nombre.x_sept
                self.nombre.sept_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.huit_rect.collidepoint(event.pos):

            if self.nombre.huit_rect.x == 277:

                self.nombre.huit_rect.x = self.nombre.x_huit
                self.nombre.huit_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.huit_rect.x == 384:

                self.nombre.huit_rect.x = self.nombre.x_huit
                self.nombre.huit_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.huit_rect.x == 489:

                self.nombre.huit_rect.x = self.nombre.x_huit
                self.nombre.huit_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.huit_rect.x == 595:

                self.nombre.huit_rect.x = self.nombre.x_huit
                self.nombre.huit_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.huit_rect.x == 702:

                self.nombre.huit_rect.x = self.nombre.x_huit
                self.nombre.huit_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.neuf_rect.collidepoint(event.pos):

            if self.nombre.neuf_rect.x == 277:

                self.nombre.neuf_rect.x = self.nombre.x_neuf
                self.nombre.neuf_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.neuf_rect.x == 384:

                self.nombre.neuf_rect.x = self.nombre.x_neuf
                self.nombre.neuf_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.neuf_rect.x == 489:

                self.nombre.neuf_rect.x = self.nombre.x_neuf
                self.nombre.neuf_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.neuf_rect.x == 595:

                self.nombre.neuf_rect.x = self.nombre.x_neuf
                self.nombre.neuf_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.neuf_rect.x == 702:

                self.nombre.neuf_rect.x = self.nombre.x_neuf
                self.nombre.neuf_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.dix_rect.collidepoint(event.pos):

            if self.nombre.dix_rect.x == 277:

                self.nombre.dix_rect.x = self.nombre.x_dix
                self.nombre.dix_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.dix_rect.x == 384:

                self.nombre.dix_rect.x = self.nombre.x_dix
                self.nombre.dix_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.dix_rect.x == 489:

                self.nombre.dix_rect.x = self.nombre.x_dix
                self.nombre.dix_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.dix_rect.x == 595:

                self.nombre.dix_rect.x = self.nombre.x_dix
                self.nombre.dix_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.dix_rect.x == 702:

                self.nombre.dix_rect.x = self.nombre.x_dix
                self.nombre.dix_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.onze_rect.collidepoint(event.pos):

            if self.nombre.onze_rect.x == 277:

                self.nombre.onze_rect.x = self.nombre.x_un
                self.nombre.onze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.onze_rect.x == 384:

                self.nombre.onze_rect.x = self.nombre.x_un
                self.nombre.onze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.onze_rect.x == 489:

                self.nombre.onze_rect.x = self.nombre.x_un
                self.nombre.onze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.onze_rect.x == 595:

                self.nombre.onze_rect.x = self.nombre.x_un
                self.nombre.onze_rect.y = self.nombre.y_haut

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.onze_rect.x == 702:

                self.nombre.onze_rect.x = self.nombre.x_un
                self.nombre.onze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.douze_rect.collidepoint(event.pos):

            if self.nombre.douze_rect.x == 277:

                self.nombre.douze_rect.x = self.nombre.x_deux
                self.nombre.douze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.douze_rect.x == 384:

                self.nombre.douze_rect.x = self.nombre.x_deux
                self.nombre.douze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.douze_rect.x == 489:

                self.nombre.douze_rect.x = self.nombre.x_deux
                self.nombre.douze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.douze_rect.x == 595:

                self.nombre.douze_rect.x = self.nombre.x_deux
                self.nombre.douze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.douze_rect.x == 702:

                self.nombre.douze_rect.x = self.nombre.x_deux
                self.nombre.douze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.treize_rect.collidepoint(event.pos):

            if self.nombre.treize_rect.x == 277:

                self.nombre.treize_rect.x = self.nombre.x_trois
                self.nombre.treize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.treize_rect.x == 384:

                self.nombre.treize_rect.x = self.nombre.x_trois
                self.nombre.treize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.treize_rect.x == 489:

                self.nombre.treize_rect.x = self.nombre.x_trois
                self.nombre.treize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.treize_rect.x == 595:

                self.nombre.treize_rect.x = self.nombre.x_trois
                self.nombre.treize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.treize_rect.x == 702:

                self.nombre.treize_rect.x = self.nombre.x_trois
                self.nombre.treize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.quatorze_rect.collidepoint(event.pos):

            if self.nombre.quatorze_rect.x == 277:

                self.nombre.quatorze_rect.x = self.nombre.x_quatre
                self.nombre.quatorze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.quatorze_rect.x == 384:

                self.nombre.quatorze_rect.x = self.nombre.x_quatre
                self.nombre.quatorze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.quatorze_rect.x == 489:

                self.nombre.quatorze_rect.x = self.nombre.x_quatre
                self.nombre.quatorze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.quatorze_rect.x == 595:

                self.nombre.quatorze_rect.x = self.nombre.x_quatre
                self.nombre.quatorze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.quatorze_rect.x == 702:

                self.nombre.quatorze_rect.x = self.nombre.x_quatre
                self.nombre.quatorze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.quinze_rect.collidepoint(event.pos):

            if self.nombre.quinze_rect.x == 277:

                self.nombre.quinze_rect.x = self.nombre.x_cinq
                self.nombre.quinze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.quinze_rect.x == 384:

                self.nombre.quinze_rect.x = self.nombre.x_cinq
                self.nombre.quinze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.quinze_rect.x == 489:

                self.nombre.quinze_rect.x = self.nombre.x_cinq
                self.nombre.quinze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.quinze_rect.x == 595:

                self.nombre.quinze_rect.x = self.nombre.x_cinq
                self.nombre.quinze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.quinze_rect.x == 702:

                self.nombre.quinze_rect.x = self.nombre.x_cinq
                self.nombre.quinze_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.seize_rect.collidepoint(event.pos):

            if self.nombre.seize_rect.x == 277:

                self.nombre.seize_rect.x = self.nombre.x_six
                self.nombre.seize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.seize_rect.x == 384:

                self.nombre.seize_rect.x = self.nombre.x_six
                self.nombre.seize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.seize_rect.x == 489:

                self.nombre.seize_rect.x = self.nombre.x_six
                self.nombre.seize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.seize_rect.x == 595:

                self.nombre.seize_rect.x = self.nombre.x_six
                self.nombre.seize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.seize_rect.x == 702:

                self.nombre.seize_rect.x = self.nombre.x_six
                self.nombre.seize_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.dixsept_rect.collidepoint(event.pos):

            if self.nombre.dixsept_rect.x == 277:

                self.nombre.dixsept_rect.x = self.nombre.x_sept
                self.nombre.dixsept_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.dixsept_rect.x == 384:

                self.nombre.dixsept_rect.x = self.nombre.x_sept
                self.nombre.dixsept_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.dixsept_rect.x == 489:

                self.nombre.dixsept_rect.x = self.nombre.x_sept
                self.nombre.dixsept_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.dixsept_rect.x == 595:

                self.nombre.dixsept_rect.x = self.nombre.x_sept
                self.nombre.dixsept_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.dixsept_rect.x == 702:

                self.nombre.dixsept_rect.x = self.nombre.x_sept
                self.nombre.dixsept_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.dixhuit_rect.collidepoint(event.pos):

            if self.nombre.dixhuit_rect.x == 277:

                self.nombre.dixhuit_rect.x = self.nombre.x_huit
                self.nombre.dixhuit_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.dixhuit_rect.x == 384:

                self.nombre.dixhuit_rect.x = self.nombre.x_huit
                self.nombre.dixhuit_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.dixhuit_rect.x == 489:

                self.nombre.dixhuit_rect.x = self.nombre.x_huit
                self.nombre.dixhuit_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.dixhuit_rect.x == 595:

                self.nombre.dixhuit_rect.x = self.nombre.x_huit
                self.nombre.dixhuit_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.dixhuit_rect.x == 702:

                self.nombre.dixhuit_rect.x = self.nombre.x_huit
                self.nombre.dixhuit_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.dixneuf_rect.collidepoint(event.pos):

            if self.nombre.dixneuf_rect.x == 277:

                self.nombre.dixneuf_rect.x = self.nombre.x_neuf
                self.nombre.dixneuf_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.dixneuf_rect.x == 384:

                self.nombre.dixneuf_rect.x = self.nombre.x_neuf
                self.nombre.dixneuf_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.dixneuf_rect.x == 489:

                self.nombre.dixneuf_rect.x = self.nombre.x_neuf
                self.nombre.dixneuf_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.dixneuf_rect.x == 595:

                self.nombre.dixneuf_rect.x = self.nombre.x_neuf
                self.nombre.dixneuf_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.dixneuf_rect.x == 702:

                self.nombre.dixneuf_rect.x = self.nombre.x_neuf
                self.nombre.dixneuf_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if self.nombre.vingt_rect.collidepoint(event.pos):

            if self.nombre.vingt_rect.x == 278:

                self.nombre.vingt_rect.x = self.nombre.x_dix
                self.nombre.vingt_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_premier_pris = False

            elif self.nombre.vingt_rect.x == 384:

                self.nombre.vingt_rect.x = self.nombre.x_dix
                self.nombre.vingt_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_deuxieme_pris = False

            elif self.nombre.vingt_rect.x == 489:

                self.nombre.vingt_rect.x = self.nombre.x_dix
                self.nombre.vingt_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_troisieme_pris = False

            elif self.nombre.vingt_rect.x == 595:

                self.nombre.vingt_rect.x = self.nombre.x_dix
                self.nombre.vingt_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_quatrieme_pris = False

            elif self.nombre.vingt_rect.x == 702:

                self.nombre.vingt_rect.x = self.nombre.x_dix
                self.nombre.vingt_rect.y = self.nombre.y_bas

                self.compteur -= 1

                self.is_cinqieme_pris = False

        if not self.is_premier_pris:

            if self.nombre.un_rect.collidepoint(event.pos):
                self.nombre.un_rect.x = 277
                self.nombre.un_rect.y = 497

                self.compteur += 1
                self.c1 = 1

                self.is_premier_pris = True

            if self.nombre.deux_rect.collidepoint(event.pos):
                self.nombre.deux_rect.x = 277
                self.nombre.deux_rect.y = 497

                self.compteur += 1
                self.c1 = 2

                self.is_premier_pris = True

            if self.nombre.trois_rect.collidepoint(event.pos):
                self.nombre.trois_rect.x = 277
                self.nombre.trois_rect.y = 497

                self.compteur += 1
                self.c1 = 3

                self.is_premier_pris = True

            if self.nombre.quatre_rect.collidepoint(event.pos):
                self.nombre.quatre_rect.x = 277
                self.nombre.quatre_rect.y = 497

                self.compteur += 1
                self.c1 = 4

                self.is_premier_pris = True

            if self.nombre.cinq_rect.collidepoint(event.pos):
                self.nombre.cinq_rect.x = 277
                self.nombre.cinq_rect.y = 497

                self.compteur += 1
                self.c1 = 5

                self.is_premier_pris = True

            if self.nombre.six_rect.collidepoint(event.pos):
                self.nombre.six_rect.x = 277
                self.nombre.six_rect.y = 497

                self.compteur += 1
                self.c1 = 6

                self.is_premier_pris = True

            if self.nombre.sept_rect.collidepoint(event.pos):
                self.nombre.sept_rect.x = 277
                self.nombre.sept_rect.y = 497

                self.compteur += 1
                self.c1 = 7

                self.is_premier_pris = True

            if self.nombre.huit_rect.collidepoint(event.pos):
                self.nombre.huit_rect.x = 277
                self.nombre.huit_rect.y = 497

                self.compteur += 1
                self.c1 = 8

                self.is_premier_pris = True

            if self.nombre.neuf_rect.collidepoint(event.pos):
                self.nombre.neuf_rect.x = 277
                self.nombre.neuf_rect.y = 497

                self.compteur += 1
                self.c1 = 9

                self.is_premier_pris = True

            if self.nombre.dix_rect.collidepoint(event.pos):
                self.nombre.dix_rect.x = 277
                self.nombre.dix_rect.y = 497

                self.compteur += 1
                self.c1 = 10

                self.is_premier_pris = True

            if self.nombre.onze_rect.collidepoint(event.pos):
                self.nombre.onze_rect.x = 277
                self.nombre.onze_rect.y = 497

                self.compteur += 1
                self.c1 = 11

                self.is_premier_pris = True

            if self.nombre.douze_rect.collidepoint(event.pos):
                self.nombre.douze_rect.x = 277
                self.nombre.douze_rect.y = 497

                self.compteur += 1
                self.c1 = 12

                self.is_premier_pris = True

            if self.nombre.treize_rect.collidepoint(event.pos):
                self.nombre.treize_rect.x = 277
                self.nombre.treize_rect.y = 497

                self.compteur += 1
                self.c1 = 13

                self.is_premier_pris = True

            if self.nombre.quatorze_rect.collidepoint(event.pos):
                self.nombre.quatorze_rect.x = 277
                self.nombre.quatorze_rect.y = 497

                self.compteur += 1
                self.c1 = 14

                self.is_premier_pris = True

            if self.nombre.quinze_rect.collidepoint(event.pos):
                self.nombre.quinze_rect.x = 277
                self.nombre.quinze_rect.y = 497

                self.compteur += 1
                self.c1 = 15

                self.is_premier_pris = True

            if self.nombre.seize_rect.collidepoint(event.pos):
                self.nombre.seize_rect.x = 277
                self.nombre.seize_rect.y = 497

                self.compteur += 1
                self.c1 = 16

                self.is_premier_pris = True

            if self.nombre.dixsept_rect.collidepoint(event.pos):
                self.nombre.dixsept_rect.x = 277
                self.nombre.dixsept_rect.y = 497

                self.compteur += 1
                self.c1 = 17

                self.is_premier_pris = True

            if self.nombre.dixhuit_rect.collidepoint(event.pos):
                self.nombre.dixhuit_rect.x = 277
                self.nombre.dixhuit_rect.y = 497

                self.compteur += 1
                self.c1 = 18

                self.is_premier_pris = True

            if self.nombre.dixneuf_rect.collidepoint(event.pos):
                self.nombre.dixneuf_rect.x = 277
                self.nombre.dixneuf_rect.y = 497

                self.compteur += 1
                self.c1 = 19

                self.is_premier_pris = True

            if self.nombre.vingt_rect.collidepoint(event.pos):
                self.nombre.vingt_rect.x = 278
                self.nombre.vingt_rect.y = 497

                self.compteur += 1
                self.c1 = 20

                self.is_premier_pris = True

        elif not self.is_deuxieme_pris:

            if self.nombre.un_rect.collidepoint(event.pos):
                self.nombre.un_rect.x = 384
                self.nombre.un_rect.y = 497

                self.compteur += 1
                self.c2 = 1

                self.is_deuxieme_pris = True

            if self.nombre.deux_rect.collidepoint(event.pos):
                self.nombre.deux_rect.x = 384
                self.nombre.deux_rect.y = 497

                self.compteur += 1
                self.c2 = 2

                self.is_deuxieme_pris = True

            if self.nombre.trois_rect.collidepoint(event.pos):
                self.nombre.trois_rect.x = 384
                self.nombre.trois_rect.y = 497

                self.compteur += 1
                self.c2 = 3

                self.is_deuxieme_pris = True

            if self.nombre.quatre_rect.collidepoint(event.pos):
                self.nombre.quatre_rect.x = 384
                self.nombre.quatre_rect.y = 497

                self.compteur += 1
                self.c2 = 4

                self.is_deuxieme_pris = True

            if self.nombre.cinq_rect.collidepoint(event.pos):
                self.nombre.cinq_rect.x = 384
                self.nombre.cinq_rect.y = 497

                self.compteur += 1
                self.c2 = 5

                self.is_deuxieme_pris = True

            if self.nombre.six_rect.collidepoint(event.pos):
                self.nombre.six_rect.x = 384
                self.nombre.six_rect.y = 497

                self.compteur += 1
                self.c2 = 6

                self.is_deuxieme_pris = True

            if self.nombre.sept_rect.collidepoint(event.pos):
                self.nombre.sept_rect.x = 384
                self.nombre.sept_rect.y = 497

                self.compteur += 1
                self.c2 = 7

                self.is_deuxieme_pris = True

            if self.nombre.huit_rect.collidepoint(event.pos):
                self.nombre.huit_rect.x = 384
                self.nombre.huit_rect.y = 497

                self.compteur += 1
                self.c2 = 8

                self.is_deuxieme_pris = True

            if self.nombre.neuf_rect.collidepoint(event.pos):
                self.nombre.neuf_rect.x = 384
                self.nombre.neuf_rect.y = 497

                self.compteur += 1
                self.c2 = 9

                self.is_deuxieme_pris = True

            if self.nombre.dix_rect.collidepoint(event.pos):
                self.nombre.dix_rect.x = 384
                self.nombre.dix_rect.y = 497

                self.compteur += 1
                self.c2 = 10

                self.is_deuxieme_pris = True

            if self.nombre.onze_rect.collidepoint(event.pos):
                self.nombre.onze_rect.x = 384
                self.nombre.onze_rect.y = 497

                self.compteur += 1
                self.c2 = 11

                self.is_deuxieme_pris = True

            if self.nombre.douze_rect.collidepoint(event.pos):
                self.nombre.douze_rect.x = 384
                self.nombre.douze_rect.y = 497

                self.compteur += 1
                self.c2 = 12

                self.is_deuxieme_pris = True

            if self.nombre.treize_rect.collidepoint(event.pos):
                self.nombre.treize_rect.x = 384
                self.nombre.treize_rect.y = 497

                self.compteur += 1
                self.c2 = 13

                self.is_deuxieme_pris = True

            if self.nombre.quatorze_rect.collidepoint(event.pos):
                self.nombre.quatorze_rect.x = 384
                self.nombre.quatorze_rect.y = 497

                self.compteur += 1
                self.c2 = 14

                self.is_deuxieme_pris = True

            if self.nombre.quinze_rect.collidepoint(event.pos):
                self.nombre.quinze_rect.x = 384
                self.nombre.quinze_rect.y = 497

                self.compteur += 1
                self.c2 = 15

                self.is_deuxieme_pris = True

            if self.nombre.seize_rect.collidepoint(event.pos):
                self.nombre.seize_rect.x = 384
                self.nombre.seize_rect.y = 497

                self.compteur += 1
                self.c2 = 16

                self.is_deuxieme_pris = True

            if self.nombre.dixsept_rect.collidepoint(event.pos):
                self.nombre.dixsept_rect.x = 384
                self.nombre.dixsept_rect.y = 497

                self.compteur += 1
                self.c2 = 17

                self.is_deuxieme_pris = True

            if self.nombre.dixhuit_rect.collidepoint(event.pos):
                self.nombre.dixhuit_rect.x = 384
                self.nombre.dixhuit_rect.y = 497

                self.compteur += 1
                self.c2 = 18
                self.is_deuxieme_pris = True

            if self.nombre.dixneuf_rect.collidepoint(event.pos):
                self.nombre.dixneuf_rect.x = 384
                self.nombre.dixneuf_rect.y = 497

                self.compteur += 1
                self.c2 = 19

                self.is_deuxieme_pris = True

            if self.nombre.vingt_rect.collidepoint(event.pos):
                self.nombre.vingt_rect.x = 384
                self.nombre.vingt_rect.y = 497

                self.compteur += 1
                self.c2 = 20

                self.is_deuxieme_pris = True

        elif not self.is_troisieme_pris:

            if self.nombre.un_rect.collidepoint(event.pos):
                self.nombre.un_rect.x = 489
                self.nombre.un_rect.y = 497

                self.compteur += 1
                self.c3 = 1

                self.is_troisieme_pris = True

            if self.nombre.deux_rect.collidepoint(event.pos):
                self.nombre.deux_rect.x = 489
                self.nombre.deux_rect.y = 497

                self.compteur += 1
                self.c3 = 2

                self.is_troisieme_pris = True

            if self.nombre.trois_rect.collidepoint(event.pos):
                self.nombre.trois_rect.x = 489
                self.nombre.trois_rect.y = 497

                self.compteur += 1
                self.c3 = 3

                self.is_troisieme_pris = True

            if self.nombre.quatre_rect.collidepoint(event.pos):
                self.nombre.quatre_rect.x = 489
                self.nombre.quatre_rect.y = 497

                self.compteur += 1
                self.c3 = 4

                self.is_troisieme_pris = True

            if self.nombre.cinq_rect.collidepoint(event.pos):
                self.nombre.cinq_rect.x = 489
                self.nombre.cinq_rect.y = 497

                self.compteur += 1
                self.c3 = 5

                self.is_troisieme_pris = True

            if self.nombre.six_rect.collidepoint(event.pos):
                self.nombre.six_rect.x = 489
                self.nombre.six_rect.y = 497

                self.compteur += 1
                self.c3 = 6

                self.is_troisieme_pris = True

            if self.nombre.sept_rect.collidepoint(event.pos):
                self.nombre.sept_rect.x = 489
                self.nombre.sept_rect.y = 497

                self.compteur += 1
                self.c3 = 7

                self.is_troisieme_pris = True

            if self.nombre.huit_rect.collidepoint(event.pos):
                self.nombre.huit_rect.x = 489
                self.nombre.huit_rect.y = 497

                self.compteur += 1
                self.c3 = 8

                self.is_troisieme_pris = True

            if self.nombre.neuf_rect.collidepoint(event.pos):
                self.nombre.neuf_rect.x = 489
                self.nombre.neuf_rect.y = 497

                self.compteur += 1
                self.c3 = 9

                self.is_troisieme_pris = True

            if self.nombre.dix_rect.collidepoint(event.pos):
                self.nombre.dix_rect.x = 489
                self.nombre.dix_rect.y = 497

                self.compteur += 1
                self.c3 = 10

                self.is_troisieme_pris = True

            if self.nombre.onze_rect.collidepoint(event.pos):
                self.nombre.onze_rect.x = 489
                self.nombre.onze_rect.y = 497

                self.compteur += 1
                self.c3 = 11

                self.is_troisieme_pris = True

            if self.nombre.douze_rect.collidepoint(event.pos):
                self.nombre.douze_rect.x = 489
                self.nombre.douze_rect.y = 497

                self.compteur += 1
                self.c3 = 12

                self.is_troisieme_pris = True

            if self.nombre.treize_rect.collidepoint(event.pos):
                self.nombre.treize_rect.x = 489
                self.nombre.treize_rect.y = 497

                self.compteur += 1
                self.c3 = 13

                self.is_troisieme_pris = True

            if self.nombre.quatorze_rect.collidepoint(event.pos):
                self.nombre.quatorze_rect.x = 489
                self.nombre.quatorze_rect.y = 497

                self.compteur += 1
                self.c3 = 14

                self.is_troisieme_pris = True

            if self.nombre.quinze_rect.collidepoint(event.pos):
                self.nombre.quinze_rect.x = 489
                self.nombre.quinze_rect.y = 497

                self.compteur += 1
                self.c3 = 15

                self.is_troisieme_pris = True

            if self.nombre.seize_rect.collidepoint(event.pos):
                self.nombre.seize_rect.x = 489
                self.nombre.seize_rect.y = 497

                self.compteur += 1
                self.c3 = 16

                self.is_troisieme_pris = True

            if self.nombre.dixsept_rect.collidepoint(event.pos):
                self.nombre.dixsept_rect.x = 489
                self.nombre.dixsept_rect.y = 497

                self.compteur += 1
                self.c3 = 17

                self.is_troisieme_pris = True

            if self.nombre.dixhuit_rect.collidepoint(event.pos):
                self.nombre.dixhuit_rect.x = 489
                self.nombre.dixhuit_rect.y = 497

                self.compteur += 1
                self.c3 = 18

                self.is_troisieme_pris = True

            if self.nombre.dixneuf_rect.collidepoint(event.pos):
                self.nombre.dixneuf_rect.x = 489
                self.nombre.dixneuf_rect.y = 497

                self.compteur += 1
                self.c3 = 19

                self.is_troisieme_pris = True

            if self.nombre.vingt_rect.collidepoint(event.pos):
                self.nombre.vingt_rect.x = 489
                self.nombre.vingt_rect.y = 497

                self.compteur += 1
                self.c3 = 20

                self.is_troisieme_pris = True

        elif not self.is_quatrieme_pris:

            if self.nombre.un_rect.collidepoint(event.pos):
                self.nombre.un_rect.x = 595
                self.nombre.un_rect.y = 497

                self.compteur += 1
                self.c4 = 1

                self.is_quatrieme_pris = True

            if self.nombre.deux_rect.collidepoint(event.pos):
                self.nombre.deux_rect.x = 595
                self.nombre.deux_rect.y = 497

                self.compteur += 1
                self.c4 = 2

                self.is_quatrieme_pris = True

            if self.nombre.trois_rect.collidepoint(event.pos):
                self.nombre.trois_rect.x = 595
                self.nombre.trois_rect.y = 497

                self.compteur += 1
                self.c4 = 3

                self.is_quatrieme_pris = True

            if self.nombre.quatre_rect.collidepoint(event.pos):
                self.nombre.quatre_rect.x = 595
                self.nombre.quatre_rect.y = 497

                self.compteur += 1
                self.c4 = 4

                self.is_quatrieme_pris = True

            if self.nombre.cinq_rect.collidepoint(event.pos):
                self.nombre.cinq_rect.x = 595
                self.nombre.cinq_rect.y = 497

                self.compteur += 1
                self.c4 = 5

                self.is_quatrieme_pris = True

            if self.nombre.six_rect.collidepoint(event.pos):
                self.nombre.six_rect.x = 595
                self.nombre.six_rect.y = 497

                self.compteur += 1
                self.c4 = 6

                self.is_quatrieme_pris = True

            if self.nombre.sept_rect.collidepoint(event.pos):
                self.nombre.sept_rect.x = 595
                self.nombre.sept_rect.y = 497

                self.compteur += 1
                self.c4 = 7

                self.is_quatrieme_pris = True

            if self.nombre.huit_rect.collidepoint(event.pos):
                self.nombre.huit_rect.x = 595
                self.nombre.huit_rect.y = 497

                self.compteur += 1
                self.c4 = 8

                self.is_quatrieme_pris = True

            if self.nombre.neuf_rect.collidepoint(event.pos):
                self.nombre.neuf_rect.x = 595
                self.nombre.neuf_rect.y = 497

                self.compteur += 1
                self.c4 = 9

                self.is_quatrieme_pris = True

            if self.nombre.dix_rect.collidepoint(event.pos):
                self.nombre.dix_rect.x = 595
                self.nombre.dix_rect.y = 497

                self.compteur += 1
                self.c4 = 10

                self.is_quatrieme_pris = True

            if self.nombre.onze_rect.collidepoint(event.pos):
                self.nombre.onze_rect.x = 595
                self.nombre.onze_rect.y = 497

                self.compteur += 1
                self.c4 = 11

                self.is_quatrieme_pris = True

            if self.nombre.douze_rect.collidepoint(event.pos):
                self.nombre.douze_rect.x = 595
                self.nombre.douze_rect.y = 497

                self.compteur += 1
                self.c4 = 12

                self.is_quatrieme_pris = True

            if self.nombre.treize_rect.collidepoint(event.pos):
                self.nombre.treize_rect.x = 595
                self.nombre.treize_rect.y = 497

                self.compteur += 1
                self.c4 = 13

                self.is_quatrieme_pris = True

            if self.nombre.quatorze_rect.collidepoint(event.pos):
                self.nombre.quatorze_rect.x = 595
                self.nombre.quatorze_rect.y = 497

                self.compteur += 1
                self.c4 = 14

                self.is_quatrieme_pris = True

            if self.nombre.quinze_rect.collidepoint(event.pos):
                self.nombre.quinze_rect.x = 595
                self.nombre.quinze_rect.y = 497

                self.compteur += 1
                self.c4 = 15

                self.is_quatrieme_pris = True

            if self.nombre.seize_rect.collidepoint(event.pos):
                self.nombre.seize_rect.x = 595
                self.nombre.seize_rect.y = 497

                self.compteur += 1
                self.c4 = 16

                self.is_quatrieme_pris = True

            if self.nombre.dixsept_rect.collidepoint(event.pos):
                self.nombre.dixsept_rect.x = 595
                self.nombre.dixsept_rect.y = 497

                self.compteur += 1
                self.c4 = 17

                self.is_quatrieme_pris = True

            if self.nombre.dixhuit_rect.collidepoint(event.pos):
                self.nombre.dixhuit_rect.x = 595
                self.nombre.dixhuit_rect.y = 497

                self.compteur += 1
                self.c4 = 18

                self.is_quatrieme_pris = True

            if self.nombre.dixneuf_rect.collidepoint(event.pos):
                self.nombre.dixneuf_rect.x = 595
                self.nombre.dixneuf_rect.y = 497

                self.compteur += 1
                self.c4 = 19

                self.is_quatrieme_pris = True

            if self.nombre.vingt_rect.collidepoint(event.pos):
                self.nombre.vingt_rect.x = 595
                self.nombre.vingt_rect.y = 497

                self.compteur += 1
                self.c4 = 20

                self.is_quatrieme_pris = True

        elif not self.is_cinqieme_pris:

            if self.nombre.un_rect.collidepoint(event.pos):
                self.nombre.un_rect.x = 702
                self.nombre.un_rect.y = 497

                self.compteur += 1
                self.c5 = 1

                self.is_cinqieme_pris = True

            if self.nombre.deux_rect.collidepoint(event.pos):
                self.nombre.deux_rect.x = 702
                self.nombre.deux_rect.y = 497

                self.compteur += 1
                self.c5 = 2

                self.is_cinqieme_pris = True

            if self.nombre.trois_rect.collidepoint(event.pos):
                self.nombre.trois_rect.x = 702
                self.nombre.trois_rect.y = 497

                self.compteur += 1
                self.c5 = 3

                self.is_cinqieme_pris = True

            if self.nombre.quatre_rect.collidepoint(event.pos):
                self.nombre.quatre_rect.x = 702
                self.nombre.quatre_rect.y = 497

                self.compteur += 1
                self.c5 = 4

                self.is_cinqieme_pris = True

            if self.nombre.cinq_rect.collidepoint(event.pos):
                self.nombre.cinq_rect.x = 702
                self.nombre.cinq_rect.y = 497

                self.compteur += 1
                self.c5 = 5

                self.is_cinqieme_pris = True

            if self.nombre.six_rect.collidepoint(event.pos):
                self.nombre.six_rect.x = 702
                self.nombre.six_rect.y = 497

                self.compteur += 1
                self.c5 = 6

                self.is_cinqieme_pris = True

            if self.nombre.sept_rect.collidepoint(event.pos):
                self.nombre.sept_rect.x = 702
                self.nombre.sept_rect.y = 497

                self.compteur += 1
                self.c5 = 7

                self.is_cinqieme_pris = True

            if self.nombre.huit_rect.collidepoint(event.pos):
                self.nombre.huit_rect.x = 702
                self.nombre.huit_rect.y = 497

                self.compteur += 1
                self.c5 = 8

                self.is_cinqieme_pris = True

            if self.nombre.neuf_rect.collidepoint(event.pos):
                self.nombre.neuf_rect.x = 702
                self.nombre.neuf_rect.y = 497

                self.compteur += 1
                self.c5 = 9

                self.is_cinqieme_pris = True

            if self.nombre.dix_rect.collidepoint(event.pos):
                self.nombre.dix_rect.x = 702
                self.nombre.dix_rect.y = 497

                self.compteur += 1
                self.c5 = 10

                self.is_cinqieme_pris = True

            if self.nombre.onze_rect.collidepoint(event.pos):
                self.nombre.onze_rect.x = 702
                self.nombre.onze_rect.y = 497

                self.compteur += 1
                self.c5 = 11

                self.is_cinqieme_pris = True

            if self.nombre.douze_rect.collidepoint(event.pos):
                self.nombre.douze_rect.x = 702
                self.nombre.douze_rect.y = 497

                self.compteur += 1
                self.c5 = 12

                self.is_cinqieme_pris = True

            if self.nombre.treize_rect.collidepoint(event.pos):
                self.nombre.treize_rect.x = 702
                self.nombre.treize_rect.y = 497

                self.compteur += 1
                self.c5 = 13

                self.is_cinqieme_pris = True

            if self.nombre.quatorze_rect.collidepoint(event.pos):
                self.nombre.quatorze_rect.x = 702
                self.nombre.quatorze_rect.y = 497

                self.compteur += 1
                self.c5 = 14

                self.is_cinqieme_pris = True

            if self.nombre.quinze_rect.collidepoint(event.pos):
                self.nombre.quinze_rect.x = 702
                self.nombre.quinze_rect.y = 497

                self.compteur += 1
                self.c5 = 15

                self.is_cinqieme_pris = True

            if self.nombre.seize_rect.collidepoint(event.pos):
                self.nombre.seize_rect.x = 702
                self.nombre.seize_rect.y = 497

                self.compteur += 1
                self.c5 = 16

                self.is_cinqieme_pris = True

            if self.nombre.dixsept_rect.collidepoint(event.pos):
                self.nombre.dixsept_rect.x = 702
                self.nombre.dixsept_rect.y = 497

                self.compteur += 1
                self.c5 = 17

                self.is_cinqieme_pris = True

            if self.nombre.dixhuit_rect.collidepoint(event.pos):
                self.nombre.dixhuit_rect.x = 702
                self.nombre.dixhuit_rect.y = 497

                self.compteur += 1
                self.c5 = 18

                self.is_cinqieme_pris = True

            if self.nombre.dixneuf_rect.collidepoint(event.pos):
                self.nombre.dixneuf_rect.x = 702
                self.nombre.dixneuf_rect.y = 497

                self.compteur += 1
                self.c5 = 19

                self.is_cinqieme_pris = True

            if self.nombre.vingt_rect.collidepoint(event.pos):
                self.nombre.vingt_rect.x = 702
                self.nombre.vingt_rect.y = 497

                self.compteur += 1
                self.c5 = 20

                self.is_cinqieme_pris = True

        if self.compteur == 5 and not self.is_validation and self.is_lunch:

            if self.confirm_image_rect.collidepoint(event.pos):

                if game.money >= 10:

                    self.is_lunch = False
                    self.is_validation = True
                    self.test_position(game)

                    game.money -= 10

                else:
                    self.t = True
                    self.z = 0

