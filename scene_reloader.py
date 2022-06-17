import pygame
import pygame.font


class SceneReloader:
    """ведение статистики"""

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.pos = [40, 30]
        self.color = (100, 0, 70)
        self.started_time = pygame.time.get_ticks()
        self.interval = 0
        self.text_interval = self.font.render(str(int(pygame.time.get_ticks() - self.started_time) / 1000),
                                              False, self.color)

        self.text_interval_rect = self.text_interval.get_rect()
        self.text_interval_rect.centerx = 10
        self.text_interval_rect.centery = 50

    def show_timer(self):
        self.screen.blit(self.text_interval, self.text_interval_rect)

    def update(self):
        self.interval = 0
        self.started_time = pygame.time.get_ticks()
        while int(pygame.time.get_ticks() - self.started_time) / 1000 < 3:
            print(int(pygame.time.get_ticks() - self.started_time) / 1000)
            self.text_interval = self.font.render(str(int(pygame.time.get_ticks() - self.started_time) / 1000),
                                                  False, self.color)
