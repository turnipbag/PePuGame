"""Module for storing game and menu loops
"""
import logging
import pygame
from pepugame.player import Player
from pepugame.settings import WINDOW_WIDTH, WINDOW_HEIGHT, color_list
from pepugame.finish_line import FinishLine

logger: logging.Logger  = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)-15s] %(levelname)s: %(message)s",
                        level="INFO"
    )

class Game():
    """Game class
    """
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        pygame.init()
        #pylint:disable=no-member
        pygame.display.set_caption("PePu Game")
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def start(self) -> str|None:
        """Initialize pepugame
        """
        return self.main_menu()

    def game_loop(self) -> str|None:
        """Game loop logic
        """
        all_sprites = pygame.sprite.Group()
        self.setup_finishline(all_sprites, 20)
        players: int = 10
        spacing: float = WINDOW_HEIGHT / (players + 1)
        for p in range(players):
            x = 50
            y = (p+1)*spacing
            color = color_list.pop()
            Player(all_sprites, (x,y), color)

        running = True
        try:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        logger.info("Exited game.")
                        pygame.quit()
                        return None

                dt: float = self.clock.tick() / 1000

                self.display_surface.fill((0,0,0))

                all_sprites.update(dt)
                all_sprites.draw(self.display_surface)

                pygame.display.update()

        except KeyboardInterrupt:
            logger.warning("Interrupted by keyboard.")
        except: #pylint:disable=bare-except
            logger.error("Unhandled exception occurred - please contact developers.\n",
            exc_info=True)
            return "Stopped due to an exception."
        return None

    def main_menu(self) -> str|None:
        """Main menu loop of pepugame
        """


        pygame.init()
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        logger.info("Exited game.")
                        pygame.quit()
                        return None

                self.display_surface.fill((0,0,0))

                pygame.display.update()

        except KeyboardInterrupt:
            logger.warning("Interrupted by keyboard.")
        except: #pylint:disable=bare-except
            logger.error("Unhandled exception occurred - please contact developers.\n",
            exc_info=True)
            return "Stopped due to an exception."
        return None


    def setup_finishline(self, groups: pygame.sprite.Group, box_width: int) -> None:
        """Create objects that represent the finishline
        """
        count: int = WINDOW_HEIGHT // box_width
        for pos in range(count):
            x: int = WINDOW_WIDTH - 100
            if pos % 2 != 0:
                x = WINDOW_WIDTH - 80
            y: int = box_width * pos
            FinishLine(groups, (x,y), "white")

    def check_win_condition(self) -> None:
        """Checks whether one of the players c
        rossed the finish line
        """
    