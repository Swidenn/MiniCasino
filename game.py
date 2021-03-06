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


class NoMoney(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.game = Game()

        self.color = (191, 54, 12)
        self.font = pygame.font.SysFont("Showcard Gothic", 30)
        self.message = self.font.render("Not enough money", 1, self.color)

        self.rect = self.message.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def affichage_nomoney(self, screen, pos_x, pos_y, taille=30):

        self.font = pygame.font.SysFont("Showcard Gothic", taille)
        self.message = self.font.render("Not enough money", 1, self.color)

        self.rect.x = pos_x
        self.rect.y = pos_y

        screen.blit(self.message, self.rect)


class Game:
    """
    Class: Du jeu en lui même (dédié que
    pour ça) il permet en t'autre de changer globalement
    tous ce qui a un rapport avec le jeu.
    """

    def __init__(self):

        self.press = {}
        self.money = 15

        self.color = (191, 191, 190)
        self.font = pygame.font.SysFont("Showcard Gothic", 30)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = 995 - self.t_money_rect.width
        self.t_money_rect.y = 38

        # 1- Ici j'initialise tous ce qui il y'aura pour le menu du début.
        self.menu_image = pygame.image.load("assets/png/background.png")
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.x = 0
        self.menu_rect.y = 0

        self.play_button_image = pygame.image.load("assets/png/play_button.png")
        self.play_button_image_rect = self.play_button_image.get_rect()
        self.play_button_image_rect.x = 1080 / 2 - self.play_button_image_rect.width / 2
        self.play_button_image_rect.y = 590

        # 1- Ici j'initialise tous ce qui il y'aura pour le menu pause.
        self.pause_image = pygame.image.load("assets/png/pause_background.png")
        self.pause_image_rect = self.pause_image.get_rect()
        self.pause_image_rect.x = 0
        self.pause_image_rect.y = 0

        self.pause_play_image = pygame.image.load("assets/png/play_pause.png")
        self.pause_play_image_rect = self.pause_play_image.get_rect()
        self.pause_play_image_rect.x = 1080 / 2 - self.pause_play_image_rect.width
        self.pause_play_image_rect.y = 490

        self.menu_button_image = pygame.image.load("assets/png/menu_button.png")
        self.pause_menu_button_image_rect = self.menu_button_image.get_rect()
        self.pause_menu_button_image_rect.x = 1080 / 2
        self.pause_menu_button_image_rect.y = 490

        self.quit_button_image = pygame.image.load("assets/png/quit_button.png")
        self.quit_button_image_rect = self.quit_button_image.get_rect()
        self.quit_button_image_rect.x = 1080 / 2 - self.quit_button_image_rect.width / 2
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
        self.choix_milieu_image_rect.x = 1080 / 2 - self.choix_milieu_image_rect.width / 2
        self.choix_milieu_image_rect.y = 105

        self.choix_gauche_image = pygame.image.load("assets/png/choose_left.png")
        self.choix_gauche_image_rect = self.choix_gauche_image.get_rect()
        self.choix_gauche_image_rect.x = 19
        self.choix_gauche_image_rect.y = 105

        self.choix_droit_image = pygame.image.load("assets/png/choose_right.png")
        self.choix_droit_image_rect = self.choix_droit_image.get_rect()
        self.choix_droit_image_rect.x = 715
        self.choix_droit_image_rect.y = 105

        self.prochainement = pygame.image.load("assets/png/prochainement.png")
        self.prochainement_rect = self.prochainement.get_rect()
        self.prochainement_rect.x = 715
        self.prochainement_rect.y = 105

        # 3- Ici c'est les booléens qui indiqueront l'état dans lequel le jeu se trouve
        self.is_menu = True
        self.is_choose_menu = False
        self.is_paused = False
        self.is_game = False
        self.is_course_epique = False

    def pos_money(self, screen, pos_x, pos_y):

        self.coins_image_rect.x = pos_x
        self.coins_image_rect.y = pos_y - 18

        screen.blit(self.coins_image, self.coins_image_rect)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = pos_x - 5 - self.t_money_rect.width
        self.t_money_rect.y = pos_y

        screen.blit(self.t_money, self.t_money_rect)

    def game_start(self, screen, course, mt):

        if self.is_menu:
            self.game_menu(screen)

        elif self.is_game:

            if self.is_choose_menu:
                self.choose(screen)

            elif course.is_rules and not self.is_choose_menu and course.is_lunch:
                course.rule(screen)

            elif course.is_lunch and self.is_game and not course.is_validation:
                course.lunch(screen, self)

            elif self.is_game and course.is_validation:
                course.validation(screen)

            elif mt.machine_is_lunch and self.is_game:

                mt.start_machine(screen, self)
                mt.emplacements.draw(screen)

        elif self.is_paused:
            self.paused(screen)

    def game_button(self, event, course, mt):

        if self.is_paused:

            if self.quit_button_image_rect.collidepoint(event.pos):
                run = False
                pygame.quit()

            elif self.pause_play_image_rect.collidepoint(event.pos):
                self.is_paused = False
                self.is_game = True

            elif self.pause_menu_button_image_rect.collidepoint(event.pos):
                self.game_over(course, mt)

        if self.is_menu:

            if self.play_button_image_rect.collidepoint(event.pos):
                self.is_menu = False
                self.is_choose_menu = True
                self.is_game = True

        if self.is_game and not self.is_paused:

            if self.choix_milieu_image_rect.collidepoint(event.pos) and not course.is_lunch and not mt.machine_is_lunch:
                self.is_choose_menu = False
                course.is_lunch = True

            elif self.choix_gauche_image_rect.collidepoint(event.pos) and not mt.machine_is_lunch and not course.is_lunch:
                self.is_choose_menu = False
                mt.machine_is_lunch = True

            if course.ok_image_rect.collidepoint(event.pos) and course.is_lunch:
                course.is_rules = False

            course.grille_selection(event, self)

            if course.is_validation and course.cheval.fin:

                if course.quit_img_rect.collidepoint(event.pos):
                    run = False
                    pygame.quit()

                elif course.retry_image_rect.collidepoint(event.pos):
                    self.game_over(course, mt)

    def game_over(self, course, mt):

        self.is_menu = True
        self.is_choose_menu = False
        self.is_paused = False
        self.is_game = False
        self.is_course_epique = False

        course.is_rules = True
        course.is_lunch = False
        course.is_validation = False

        mt.machine_is_lunch = False

    def game_menu(self, screen):

        screen.blit(self.menu_image, self.menu_rect)
        screen.blit(self.play_button_image, self.play_button_image_rect)

    def paused(self, screen):
        """
        Fonction d'affichage du menu pause

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

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

    def choose(self, screen):
        """
        Fonction d'affichage du menu choose

        :param screen:
        screen est la surface sur lequel paused s'affichera

        :return:
        """

        self.is_menu = False

        screen.blit(self.choix_milieu_image, self.choix_milieu_image_rect)
        screen.blit(self.choix_gauche_image, self.choix_gauche_image_rect)
        screen.blit(self.choix_droit_image, self.choix_droit_image_rect)
        screen.blit(self.prochainement, self.prochainement_rect)
        screen.blit(self.choose_image, self.choose_image_rect)

        screen.blit(self.coins_image, self.coins_image_rect)

        self.t_money = self.font.render(str(self.money), 1, self.color)
        self.t_money_rect = self.t_money.get_rect()
        self.t_money_rect.x = 995 - self.t_money_rect.width
        self.t_money_rect.y = 38

        screen.blit(self.t_money, self.t_money_rect)
