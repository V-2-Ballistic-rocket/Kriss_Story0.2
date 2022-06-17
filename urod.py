import pygame


class Urod(pygame.sprite.Sprite):
    """класс одного врага"""
    def __init__(self, screen):
        super(Urod, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Sprites/urod_left.png')
        self.image_right = pygame.image.load('Sprites/urod_right.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.vector_x = False
        self.speed = 7

    def draw(self):
        """вывод на экран врага"""
        if self.vector_x:
            self.screen.blit(self.image_right, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def update(self, hero):
        """обновление врага на экране"""
        if hero.rect.centerx > self.x:
            self.x += 0.03 * self.speed
            self.vector_x = True
        if hero.rect.centerx < self.x:
            self.x -= 0.03 * self.speed
            self.vector_x = False

        if hero.rect.centery > self.y:
            self.y += 0.03 * self.speed
        if hero.rect.centery < self.y:
            self.y -= 0.03 * self.speed
        self.rect.x = self.x
        self.rect.y = self.y
