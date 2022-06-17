import pygame
import pygame.font

class FPSCounter:
    def __init__(self, screen, clock, text_color, pos):
        self.__screen = screen
        self.__font = pygame.font.Font(None, 30)
        self.__clock = clock
        self.__pos = pos
        self.__color = text_color

        self.fps_text = self.__font.render(str(int(self.__clock.get_fps())) + "FPS", False, self.__color)
        self.fps_text_rect = self.fps_text.get_rect()

        self.show_fps = True

    def __render(self):
        if self.show_fps:
            self.__screen.blit(self.fps_text, self.fps_text_rect)

    def update(self):
        self.__render()
        self.fps_text = self.__font.render(f"{self.__clock.get_fps():2.0f} FPS", False, self.__color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.__pos[0], self.__pos[1]))