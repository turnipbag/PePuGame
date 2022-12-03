"""Module for storing game and menu loops
"""
import logging
import pygame
from pepugame.player import Player
from pepugame.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from pepugame.finish_line import FinishLine

def game_loop() -> str|None:
    """Game loop logic
    """
    logger: logging.Logger  = logging.getLogger(__name__)

    #pylint:disable=no-member
    pygame.display.set_caption("PePu Game")
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    pygame.init()

    all_sprites = pygame.sprite.Group()
    setup_finishline(all_sprites, 20)
    Player(all_sprites, "green")

    logging.basicConfig(format="[%(asctime)-15s] %(levelname)s: %(message)s",
                            level="INFO"
        )
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info("Exited game.")
                    pygame.quit()
                    return None

            dt: float = clock.tick() / 1000

            display_surface.fill((0,0,0))

            all_sprites.update(dt)
            all_sprites.draw(display_surface)

            pygame.display.update()

    except KeyboardInterrupt:
        logger.warning("Interrupted by keyboard.")
    except: #pylint:disable=bare-except
        logger.error("Unhandled exception occurred - please contact developers.\n",exc_info=True)
        return "Stopped due to an exception."
    return None

def setup_finishline(groups: pygame.sprite.Group, box_width: int) -> None:
    """Create objects that represent the finishline
    """
    count: int = WINDOW_HEIGHT // box_width
    for pos in range(count):
        x: int = WINDOW_WIDTH - 100
        if pos % 2 != 0:
            x = WINDOW_WIDTH - 80
        y: int = box_width * pos
        FinishLine(groups, (x,y), "white")
    