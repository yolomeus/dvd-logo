from typing import Tuple

from pygame import Surface, Vector2
from pygame.font import SysFont

from dvd_logo import DVDLogo


class HUD:
    def __init__(self, screen: Surface, dvd_logo: DVDLogo, corners: Tuple[Vector2, ...]):
        self.dvd_logo = dvd_logo
        self.screen = screen
        self.corners = corners

    def draw(self, fps: float):
        closest_corner = sorted(self.corners, key=lambda x: x.distance_to(self.dvd_logo.position))[0]
        dist = self.dvd_logo.position.distance_to(closest_corner) - self.dvd_logo.radius

        font = (SysFont('JetBrains Mono', 19)
                .render(f'fps: {int(fps)}, dist: {int(dist)}', True, 'white'))

        text = self.screen.blit(font, (0, 0))
        return text
