import pygame
import time
import pygame.mouse
import pygame.font
import sys
from scene_selector import SceneSelector


class MainMenu:
    def __init__(self, screen, screen_resolution):
        #  инициализация главного меню
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.background_image = [pygame.image.load('Sprites/main_menu_background_0.png'),
                                 pygame.image.load('Sprites/main_menu_background_1.png'),
                                 pygame.image.load('Sprites/main_menu_background_2.png'),
                                 pygame.image.load('Sprites/main_menu_background_3.png')]
        self.rect_background = self.background_image[0].get_rect()
        self.rect_background.centerx = self.screen_rect.centerx
        self.rect_background.centery = self.screen_rect.centery

        self.start_button_image = [pygame.image.load('Sprites/start_button_v1.png'),
                                   pygame.image.load('Sprites/start_button_v1.1.png')]
        self.start_button_rect = self.start_button_image[0].get_rect()
        self.start_button_rect.centerx = screen_resolution[0] * 0.25
        self.start_button_rect.centery = screen_resolution[1] * 0.55

        self.exit_button_image = [pygame.image.load('Sprites/exit_button.png'),
                                  pygame.image.load('Sprites/exit_button.1.png')]
        self.exit_button_rect = self.exit_button_image[0].get_rect()
        self.exit_button_rect.centerx = screen_resolution[0] * 0.25
        self.exit_button_rect.centery = screen_resolution[1] * 0.80

        self.rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 30, 20)
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]

        self.lClick = False

    def output(self):

        #  рисование карты
        if int(time.time()) % 4 == 0:
            self.screen.blit(self.background_image[0], self.rect_background)
        elif int(time.time()) % 4 == 1:
            self.screen.blit(self.background_image[1], self.rect_background)
        elif int(time.time()) % 4 == 2:
            self.screen.blit(self.background_image[2], self.rect_background)
        elif int(time.time()) % 4 == 3:
            self.screen.blit(self.background_image[3], self.rect_background)

        if self.start_button_rect.colliderect(self.rect):
            self.screen.blit(self.start_button_image[1], self.start_button_rect)
        else:
            self.screen.blit(self.start_button_image[0], self.start_button_rect)

        if self.exit_button_rect.colliderect(self.rect):
            self.screen.blit(self.exit_button_image[1], self.exit_button_rect)
        else:
            self.screen.blit(self.exit_button_image[0], self.exit_button_rect)

    def update(self, scene_selector):
        self.output()
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        if self.lClick and self.start_button_rect.colliderect(self.rect):
            scene_selector.setNumberScene(1)
        if self.lClick and self.exit_button_rect.colliderect(self.rect):
            sys.exit()
