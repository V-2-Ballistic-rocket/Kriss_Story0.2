import pygame


class Hero:

    def __init__(self, screen):
        """инициализация героя"""
        self.screen = screen
        self.image = [pygame.image.load('Sprites/Hero_up.png'),
                      pygame.image.load('Sprites/Hero_down.png'),
                      pygame.image.load('Sprites/Hero_right.png'),
                      pygame.image.load('Sprites/Hero_left.png')]
        self.rect = self.image[1].get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  #
        self.rect.centery = self.screen_rect.centery
        self.float_centery = float(self.rect.centery)
        self.float_centerx = float(self.rect.centerx)  #
        #self.rect.bottom = self.screen_rect.bottom
        self.__speed = 50
        self.pull = False
        self.move_right_flag = False
        self.move_left_flag = False
        self.move_up_flag = False
        self.move_down_flag = False

    def output(self):

        if self.move_up_flag:
            self.screen.blit(self.image[0], self.rect)
        elif self.move_right_flag:
            self.screen.blit(self.image[2], self.rect)
        elif self.move_left_flag:
            self.screen.blit(self.image[3], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)

    def update(self, screen_resolution):
        if self.move_right_flag and self.rect.centerx < screen_resolution[0]:
            self.float_centerx += 0.1 * self.__speed  # move right
        if self.move_left_flag and self.rect.centerx > 0:
            self.float_centerx -= 0.1 * self.__speed  # move left
        if self.move_up_flag and self.rect.centery > 0:
            self.float_centery -= 0.1 * self.__speed  # move up
        if self.move_down_flag and self.rect.centery < screen_resolution[1]:
            self.float_centery += 0.1 * self.__speed  # move down
            ''''''
        self.rect.centerx = self.float_centerx
        self.rect.centery = self.float_centery
        #print(self.screen_rect.centerx, " rect: ", self.rect.centerx)

    def create_hero(self):
        '''возрождает героя в центре экрана'''
        self.float_centery = self.screen_rect.centery
        self.float_centerx = self.screen_rect.centerx

    def getHeroX(self):
        return self.float_centerx

    def getHeroY(self):
        return self.float_centery

