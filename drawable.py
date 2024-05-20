from typing import Protocol, Tuple

from pygame import Rect


class Drawable(Protocol):
    def draw(self, **kwargs) -> Rect | Tuple[Rect, ...]: ...
