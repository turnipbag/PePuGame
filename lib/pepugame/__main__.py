"""Main module of pepugame
"""
import logging
import sys
import pygame
from .settings import WINDOW_WIDTH, WINDOW_HEIGHT

logger: logging.Logger  = logging.getLogger(__name__)

#pylint:disable=no-member
pygame.display.set_caption("PePu peli")
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()
pygame.init()

def main() -> str|None:
    """Main module of pepugame
    """
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
            pygame.display.update()
    except KeyboardInterrupt:
        logger.warning("Interrupted by keyboard.")
    except: #pylint:disable=bare-except
        logger.error("Unhandled exception occurred - please contact developers.\n",exc_info=True)
        return "Stopped due to an exception."
    return None

if __name__ == "__main__":
    sys.exit(main())
