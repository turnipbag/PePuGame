"""Main module of pepugame
"""
import logging
import random
import sys
from typing import Final

import pygame

from .player import Player

LOGGER: Final = logging.getLogger(__name__)
WINDOW_WIDTH: Final = 1280
WINDOW_HEIGHT: Final = 720

def main() -> str|None:
    """Main module of pepugame
    """
    logging.basicConfig(format="[%(asctime)-15s] %(levelname)s: %(message)s",
                            level="INFO"
        )
    try:
        #pylint:disable=no-member
        display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

        pygame.display.set_caption("PePu peli")

        player_spacing: int = WINDOW_HEIGHT // 3


        clock = pygame.time.Clock()
        pygame.init()

        #p1
        player1 = Player("tapsa","red",player_spacing)

        #p2
        player2 = Player("mikko","blue",player_spacing * 2)

        finish_surf = pygame.Surface((40,720))
        finish_rect = finish_surf.get_rect(center = (1200, 360))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    LOGGER.info("Exited game.")
                    pygame.quit()
                    return None
        #pylint:enable=no-member
            finish_surf.fill(("white"))
            player1.player_surf.fill((player1.color))
            player2.player_surf.fill((player2.color))

            display_surface.fill("black")
            display_surface.blit(finish_surf, finish_rect)

            display_surface.blit(player1.player_surf,player1.player_rect)
            display_surface.blit(player2.player_surf,player2.player_rect)
            display_surface.blit(player1.text_surf,player1.text_rect)
            display_surface.blit(player2.text_surf,player2.text_rect)

            if not player1.player_rect.colliderect(finish_rect):
                player1.player_rect.x += random.randint(0,12)
                player1.text_rect.x = player1.player_rect.x

            clock.tick(60)

            pygame.display.update()

    except KeyboardInterrupt:
        LOGGER.warning("Interrupted by keyboard.")
    except: #pylint:disable=bare-except
        LOGGER.error("Unhandled exception occurred - please contact developers.\n",exc_info=True)
        return "Stopped due to an exception."
    return None


if __name__ == "__main__":
    sys.exit(main())
