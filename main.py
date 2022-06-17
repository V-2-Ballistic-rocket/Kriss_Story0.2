import pygame
import controls
from scene_reloader import SceneReloader
from hero import Hero
from pygame.sprite import Group
from scores import Scores
from stats import Stats
from death_screen import DeathScreen
from main_menu import MainMenu
from interface.fps_clock import FPSCounter
from menu import Menu
from scene_selector import SceneSelector


def run():
    pygame.display.set_caption("Kriss story!")
    pygame.init()
    screen_resolution = [500, 500]
    screen = pygame.display.set_mode(screen_resolution)
    bg_color = (98, 100, 85)
    text_color = (100, 0, 70)
    arrows = Group()
    hero = Hero(screen)
    urods = Group()
    controls.create_enemies(screen, urods)
    stats = Stats(screen)
    death_screen = DeathScreen(screen)
    scores = Scores(screen, stats)
    menu = Menu(screen, screen_resolution)
    scene_reloader = SceneReloader(screen)
    clock = pygame.time.Clock()
    started_timer = True
    fps_counter = FPSCounter(screen, clock, text_color, (40, 30))
    scene_selector = SceneSelector()
    main_menu = MainMenu(screen, screen_resolution)


    while True:
        clock.tick(144)
        print(scene_selector.getSceneNumber())
        controls.events(screen, hero, arrows, menu, main_menu, scene_selector, death_screen)
        controls.update_arrows(urods, arrows, stats, scores)
        controls.update(bg_color, screen, hero, urods, arrows, stats, death_screen, screen_resolution, menu, main_menu,
                        fps_counter, scene_reloader, started_timer, scores, scene_selector)


run()
