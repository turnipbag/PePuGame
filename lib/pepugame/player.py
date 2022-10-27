"""this module contains definitions for player objects
"""
import pygame

class Player:
    """Player object for pepugame
    """
    def __init__(self, name:str, color:str, spacing:int = 50) -> None:
        font = pygame.font.SysFont("Arial", 15)
        self.name = name
        self.color = color
        self.spacing = spacing
        self.player_surf = pygame.Surface((20,20))
        self.player_surf.fill(color)
        self.player_rect = self.player_surf.get_rect(center = (20, self.spacing))
        self.text_surf = font.render(name,True,color)
        self.text_rect = self.text_surf.get_rect(bottomleft = (self.player_rect.x, self.spacing - 10))

    def set_spacing(self, spacing: int) -> None:
        """Set spacing for player object
        """
        self.spacing = spacing
        self.player_rect = self.player_surf.get_rect(center = (20, self.spacing))
        self.text_rect = self.text_surf.get_rect(bottomleft = (self.player_rect.x, self.spacing - 10))
