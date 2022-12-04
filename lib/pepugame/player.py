"""Player module for pepugame
"""
from random import randint
import pygame

class Player(pygame.sprite.Sprite):
    """player class
    """
    def __init__(self, groups: pygame.sprite.Group, pos: tuple, color: str) -> None:
        super().__init__(groups)
        self.image: pygame.surface.Surface = pygame.Surface((20,20))
        self.image.fill(color)
        self.rect: pygame.rect.Rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1,0)
        self.speed = randint(100,250)

    def move(self, dt: float) -> None:
        """Moves player forward
        """
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.center = (round(self.pos.x),round(self.pos.y))

    def update(self, dt: float) -> None:
        """Sprite update overridden
        """
        self.move(dt)
