
import pygame as pg
from pygame.math import Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('Sprites/Hero_up.png')
        '''self.image = pg.Surface((30, 30))  #создание модельки персонажа
        self.image.fill(pg.Color('dodgerblue1'))
        self.rect = self.image.get_rect(center=pos)'''
        self.rect = self.image.get_rect()
        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                self.vel.x = 5
            elif event.key == pg.K_a:
                self.vel.x = -5
            elif event.key == pg.K_w:
                self.vel.y = -5
            elif event.key == pg.K_s:
                self.vel.y = 5
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d and self.vel.x > 0:
                self.vel.x = 0
            elif event.key == pg.K_a and self.vel.x < 0:
                self.vel.x = 0
            elif event.key == pg.K_w:
                self.vel.y = 0
            elif event.key == pg.K_s:
                self.vel.y = 0

    def update(self):
        # Move the player.
        self.pos += self.vel
        self.rect.center = self.pos
