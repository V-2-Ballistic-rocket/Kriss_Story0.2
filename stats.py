import pygame, time

class Stats():
    '''ведение статистики'''

    def __init__(self, screen):
        """инициализация статистики"""
        self.screen = screen
        self.image = [pygame.image.load('Sprites/Hitpoint_bar_25_v2.png'),
                      pygame.image.load('Sprites/Hitpoint_bar_50_v2.png'),
                      pygame.image.load('Sprites/Hitpoint_bar_75_v2.png'),
                      pygame.image.load('Sprites/Hitpoint_bar_100_v2.png')]
        self.rect = self.image[0].get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.left + 30
        self.rect.centery = self.screen_rect.top + 10
        self.reset_stats()
        self.high_score = 0
        self.score = 0


    def output(self):
        """рисование окна стат"""
        if int(time.time()) % 4 == 0:
            self.screen.blit(self.image[3], self.rect)
        elif int(time.time()) % 4 == 1:
            self.screen.blit(self.image[2], self.rect)
        elif int(time.time()) % 4 == 2:
            self.screen.blit(self.image[1], self.rect)
        elif int(time.time()) % 4 == 3:
            self.screen.blit(self.image[0], self.rect)

    def reset_stats(self):
        """изменяющаяся статистика"""
        self.heros_left = 3
        self.score = 0