import pygame
import pygame.mouse


class Arrow(pygame.sprite.Sprite):
    def __init__(self, screen, hero):
        '''создать полю'''
        super(Arrow, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 1, 6)

        self.color = 0, 0, 0
        self.speed = 5
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        self.y = float(self.rect.y)
        self.lClick = False

    def update(self):
        '''perem arrow vverh'''
        self.y -= self.speed
        self.rect.y = self.y
        print(pygame.mouse.get_pos())
        if self.lClick:
            print(pygame.mouse.get_pos())

    def drow_arrow(self):
        pygame.draw.rect(self.screen, self.color, self.rect)