from typing import Tuple

import pygame
from pygame import Surface, Vector2, Rect


class DVDLogo:
    def __init__(self,
                 screen: Surface,
                 starting_position: Vector2,
                 velocity: Vector2,
                 radius: int):
        self.screen = screen
        self.position = starting_position
        self.radius = radius
        self.velocity = velocity

    def move(self, time_delta: int):
        height, width = self.screen.get_height(), self.screen.get_width()
        r = self.radius
        velocity = self.velocity

        next_pos = self.position + velocity * time_delta

        if next_pos.y + r >= height:
            next_pos.y = height - r
            velocity.y *= -1

        if next_pos.x + r >= width:
            next_pos.x = width - r
            velocity.x *= -1

        if next_pos.x - r <= 0:
            next_pos.x = 0 + r
            velocity.x *= -1

        if next_pos.y - r <= 0:
            next_pos.y = 0 + r
            velocity.y *= -1

        self.position = next_pos

    def draw(self) -> Tuple[Rect, ...]:
        circle = pygame.draw.circle(self.screen, "purple", self.position, self.radius)

        font = (pygame.font.SysFont('JetBrains Mono', 35, True)
                .render(f'DVD', True, 'white'))

        text = self.screen.blit(font, self.position - Vector2(self.radius * .6, self.radius * .4))

        return circle, text

    def is_close_to(self, position: Vector2):
        diff = (self.position - position)
        threshold = 1 + self.radius
        return abs(diff.x) <= threshold and abs(diff.y) <= threshold
