"""Module to create finish line sprite
"""
import pygame

class FinishLine(pygame.sprite.Sprite):
    """Finish line class
    """
    def __init__(self, groups: pygame.sprite.Group, pos: tuple, color:str) -> None:
        super().__init__(groups)
        self.image: pygame.surface.Surface = pygame.Surface((20,20))
        self.image.fill(color)
        self.rect: pygame.rect.Rect = self.image.get_rect(topleft=pos)
