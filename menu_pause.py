import pygame, pygame.mouse, pygame.font, sys

class MenuPause():
    def __init__(self, screen, screen_resolution):
        #инициализация главного меню
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.background_image = pygame.image.load('Sprites/menu_background.png')
        self.rect_background = self.background_image.get_rect()
        self.rect_background.centerx = self.screen_rect.centerx
        self.rect_background.centery = self.screen_rect.centery

        self.to_main_image = [pygame.image.load('Sprites/main_menu_button.png'),
                              pygame.image.load('Sprites/main_menu_button1.png')]
        self.to_main_rect = self.to_main_image[0].get_rect()
        self.to_main_rect.centerx = screen_resolution[0] * 0.25
        self.to_main_rect.centery = screen_resolution[1] * 0.55

        self.resume_button_image = [pygame.image.load('Sprites/resume_button.png'),
                                    pygame.image.load('Sprites/resume_button1.png')]
        self.resume_button_rect = self.resume_button_image[0].get_rect()
        self.resume_button_rect.centerx = screen_resolution[0] * 0.25
        self.resume_button_rect.centery = screen_resolution[1] * 0.30

        self.exit_button_image = [pygame.image.load('Sprites/exit_button.png'),
                                  pygame.image.load('Sprites/exit_button.1.png')]
        self.exit_button_rect = self.exit_button_image[0].get_rect()
        self.exit_button_rect.centerx = screen_resolution[0] * 0.25
        self.exit_button_rect.centery = screen_resolution[1] * 0.80

        self.rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 30, 20)
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]

        self.lClick = False





    def bgoutput(self):

        #рисование карты

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


    def update(self, main_menu):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        if self.lClick and self.to_main_rect.colliderect(self.rect):
            main_menu.scene_flag = 0
            print("back main")
        if self.lClick and self.resume_button_rect.colliderect(self.rect):
            main_menu.scene_flag = 1
        if self.lClick and self.exit_button_rect.colliderect(self.rect):
            sys.exit()
