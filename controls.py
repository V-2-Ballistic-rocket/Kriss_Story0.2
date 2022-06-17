import pygame
import sys
from arrow import Arrow
from urod import Urod

import time


def events(screen, hero, arrows, menu, main_menu, scene_selector, death_screen):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.move_up_flag = True
            if event.key == pygame.K_s:
                hero.move_down_flag = True
            if event.key == pygame.K_d:
                hero.move_right_flag = True
            if event.key == pygame.K_a:
                hero.move_left_flag = True
            if event.key == pygame.K_SPACE:
                new_arrow = Arrow(screen, hero)
                arrows.add(new_arrow)
            if event.key == pygame.K_ESCAPE:
                if scene_selector.getSceneNumber() == 3:
                    scene_selector.setNumberScene(1)
                elif scene_selector.getSceneNumber() == 1:
                    scene_selector.setNumberScene(3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.move_up_flag = False
            if event.key == pygame.K_s:
                hero.move_down_flag = False
            if event.key == pygame.K_d:
                hero.move_right_flag = False
            if event.key == pygame.K_a:
                hero.move_left_flag = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_menu.lClick = True
                death_screen.lClick = True
                menu.lClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                main_menu.lClick = False
                death_screen.lClick = False
                menu.lClick = False


def update(bg_color, screen, hero, urods, arrows, stats, death_screen, screen_resolution, menu, main_menu,
                        fps_counter, scene_reloader, started_timer, scores, scene_selector):
    """обновление экрана"""
    if scene_selector.getSceneNumber() == 0:
        main_menu.update(scene_selector)
        print("start")
    elif scene_selector.getSceneNumber() == 1:
        scene_fight(bg_color, screen, hero, urods, arrows, stats, screen_resolution, scene_selector,
                fps_counter, scene_reloader, started_timer, scores)
    elif scene_selector.getSceneNumber() == 2:
        dead_menu(stats, death_screen, scene_selector)
    elif scene_selector.getSceneNumber() == 3:
        menu.update(scene_selector)
    fps_counter.update()
    pygame.display.flip()


def hero_death(stats, screen, urods, arrows, scene_selector):
    """столкновение героя с врагами"""
    if stats.heros_left > 2:
        stats.heros_left -= 3
        urods.empty()
        arrows.empty()
        create_enemies(screen, urods)
        time.sleep(1)
    else:
        scene_selector.setNumberScene(2)
        urods.empty()
        arrows.empty()


def update_arrows(urods, arrows, stats, scores):
    """обновление позиций пуль"""
    arrows.update()
    for arrow in arrows.copy():
        if arrow.rect.bottom <= 0:
            arrows.remove(arrow)
    collisions = pygame.sprite.groupcollide(arrows, urods, True, True)
    if collisions:
        stats.score += 1
        for urods in collisions.values():
            stats.score += 1 * (len(urods) - 1)
            check_high_score(stats, scores)
        scores.image_score()


def create_enemies(screen, urods):
    urod = Urod(screen)
    urod_width = urod.rect.width
    number_urod_x = int((500 - 2 * urod_width) / urod_width)

    for urod_number in range(number_urod_x):
        urod = Urod(screen)
        urod.x = (urod_width + urod_width * urod_number)
        urod.rect.x = urod.x*2
        urods.add(urod)


def check_high_score(stats, scores):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scores.image_high_score()


def scene_fight(bg_color, screen, hero, urods, arrows, stats, screen_resolution, scene_selector,
                fps_counter, scene_reloader, started_timer, scores):

    screen.fill(bg_color)

    for arrow in arrows.sprites():
        arrow.drow_arrow()

    hero.update(screen_resolution)

    hero.output()

    stats.output()
    scores.show_score()

    fps_counter.update()
    print(hero.getHeroX(), " ", hero.getHeroY())
    x = hero.getHeroX()
    y = hero.getHeroY()
    urods.draw(screen)

    if len(urods):
        # and started_timer:
        #  started_timer = False
        scene_reloader.started_time = pygame.time.get_ticks()

    scene_reloader.interval = (pygame.time.get_ticks() - scene_reloader.started_time) / 1000

    if scene_reloader.interval > 3 and len(urods) == 0:
        create_enemies(screen, urods)
        #  started_timer = True

    urods.update(hero)

    if pygame.sprite.spritecollideany(hero, urods):
        hero_death(stats, screen, urods, arrows, scene_selector)
        hero.create_hero()


def dead_menu(stats, death_screen, scene_selector):
    """death menu"""
    death_screen.update(scene_selector)
    stats.reset_stats()
