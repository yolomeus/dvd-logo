import random

import pygame as pg
from pygame import Vector2
from pygame.time import Clock

from dvd_logo import DVDLogo
from hud import HUD


def random_velocity() -> Vector2:
    return Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()


def main():
    width, height = (1280, 720)

    # pygame setup
    pg.init()
    screen = pg.display.set_mode((width, height), vsync=True)
    clock = Clock()
    running = True

    top_left = Vector2(0, 0)
    bottom_left = Vector2(0, height)
    top_right = Vector2(width, 0)
    bottom_right = Vector2(width, height)

    corners = (top_left,
               top_right,
               bottom_left,
               bottom_right)

    speed = .2
    center = Vector2(width, height) / 2
    starting_velocity = random_velocity() * speed
    dvd_logo = DVDLogo(screen,
                       starting_position=center,
                       velocity=starting_velocity,
                       radius=50)

    hud = HUD(screen, dvd_logo, corners)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        time_delta = clock.tick(60)
        # update game state
        if not any([dvd_logo.is_close_to(pos) for pos in corners]):
            dvd_logo.move(time_delta)

        # render
        background = screen.fill('black')
        hud_rect = hud.draw(clock.get_fps())
        dvd_logo_rects = dvd_logo.draw()

        pg.display.update([background, *dvd_logo_rects, hud_rect])

    pg.quit()


if __name__ == '__main__':
    main()
