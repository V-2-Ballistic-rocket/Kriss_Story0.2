import pygame

class DeathScreen:
    '''вывод экрана смерти'''
    def __init__(self, screen):
        self.screen = screen
        self.image_background = pygame.image.load('Sprites/death.png')
        self.rect_background = self.image_background.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect_background.centerx = self.screen_rect.centerx
        self.rect_background.centery = self.screen_rect.centery

        self.image_retry = [pygame.image.load('Sprites/Revenge_button.png'),
                            pygame.image.load('Sprites/Revenge_button1.png')]
        self.rect_retry = self.image_retry[0].get_rect()
        self.rect_retry.centerx = 400
        self.rect_retry.centery = 450

        self.rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 99, 99)
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        self.lClick = False

    def output(self):
        """рисование окна смерти"""
        self.screen.blit(self.image_background, self.rect_background)

        if self.rect_retry.colliderect(self.rect):
            self.screen.blit(self.image_retry[1], self.rect_retry)
        else:
            self.screen.blit(self.image_retry[0], self.rect_retry)

    def update(self, scene_selector):
        self.output()
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        if self.lClick and self.rect_retry.colliderect(self.rect):
            scene_selector.setNumberScene(1)


