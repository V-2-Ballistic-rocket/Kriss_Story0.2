import pygame
import pygame.mouse
import pygame.font
import sys


class Menu:
    def __init__(self, screen, screen_resolution):
        #  инициализация главного меню
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.background_image = pygame.image.load('Sprites/menu_background.png')
        self.rect_background = self.background_image.get_rect()
        self.rect_background.centerx = self.screen_rect.centerx
        self.rect_background.centery = screen_resolution[0] * 0.55

        self.to_main_image = [pygame.image.load('Sprites/menu_to_main.png'),
                              pygame.image.load('Sprites/menu_to_main1.png')]
        self.to_main_rect = self.to_main_image[0].get_rect()
        self.to_main_rect.centerx = screen_resolution[0] * 0.5
        self.to_main_rect.centery = screen_resolution[1] * 0.55

        self.resume_button_image = [pygame.image.load('Sprites/menu_resume.png'),
                                    pygame.image.load('Sprites/menu_resume1.png')]
        self.resume_button_rect = self.resume_button_image[0].get_rect()
        self.resume_button_rect.centerx = screen_resolution[0] * 0.5
        self.resume_button_rect.centery = screen_resolution[1] * 0.30

        self.exit_button_image = [pygame.image.load('Sprites/menu_exit.png'),
                                  pygame.image.load('Sprites/menu_exit1.png')]
        self.exit_button_rect = self.exit_button_image[0].get_rect()
        self.exit_button_rect.centerx = screen_resolution[0] * 0.5
        self.exit_button_rect.centery = screen_resolution[1] * 0.80

        self.rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 30, 20)
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]

        self.lClick = False

        self.to_main_menu_flag = False

    def output(self):
        #  рисование карты

        self.screen.blit(self.background_image, self.rect_background)
        if self.to_main_rect.colliderect(self.rect):
            self.screen.blit(self.to_main_image[1], self.to_main_rect)
        else:
            self.screen.blit(self.to_main_image[0], self.to_main_rect)
        if self.exit_button_rect.colliderect(self.rect):
            self.screen.blit(self.exit_button_image[1], self.exit_button_rect)
        else:
            self.screen.blit(self.exit_button_image[0], self.exit_button_rect)
        if self.resume_button_rect.colliderect(self.rect):
            self.screen.blit(self.resume_button_image[1], self.resume_button_rect)
        else:
            self.screen.blit(self.resume_button_image[0], self.resume_button_rect)

    def update(self, scene_selector):
        self.output()
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        if self.lClick and self.to_main_rect.colliderect(self.rect):
            print()
            scene_selector.setNumberScene(0)
            print()
        if self.lClick and self.resume_button_rect.colliderect(self.rect):
            scene_selector.setNumberScene(1)
        if self.lClick and self.exit_button_rect.colliderect(self.rect):
            sys.exit()
