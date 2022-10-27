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

#pylint:disable=no-member
pygame.display.set_caption("PePu peli")
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()
pygame.init()

def draw_text(text: str, color: str, surface: pygame.surface.Surface, x: int, y: int) -> None:#pylint:disable=invalid-name
    """function to draw text on screen
    """
    font = pygame.font.SysFont("Arial", 25)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def game(players: list) -> None:
    """Gameloop of pepugame
    """
    running: bool = True
    winner = ""
    player_spacing: int = WINDOW_HEIGHT // (len(players) + 1)

    #respace players and blit them
    for index, player in enumerate(players):
        player.set_spacing(player_spacing * (index + 1))

    finish_surf = pygame.Surface((40,720))
    finish_rect = finish_surf.get_rect(center = (1200, 360))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    #pylint:enable=no-member
        finish_surf.fill(("white"))


        display_surface.fill("black")
        display_surface.blit(finish_surf, finish_rect)

        #respace players and blit them
        if winner == "":
            for player in players:
                display_surface.blit(player.player_surf,player.player_rect)
                display_surface.blit(player.text_surf,player.text_rect)
                player.player_rect.x += random.randint(0,9)
                player.text_rect.x = player.player_rect.x

                if player.player_rect.colliderect(finish_rect):
                    winner = player.name
                    break
        else:
            for player in players:
                display_surface.blit(player.player_surf,player.player_rect)
                display_surface.blit(player.text_surf,player.text_rect)
                draw_text("Voittaja: " + winner, "white", display_surface, WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 100)

        clock.tick(60)
        pygame.display.update()


def main() -> str|None:
    """Main module of pepugame
    """
    logging.basicConfig(format="[%(asctime)-15s] %(levelname)s: %(message)s",
                            level="INFO"
        )
    click: bool = False

    players: list = []
    colors: list = ["red", "green", "yellow", "orange", "violet", "blue", "cyan", "darksalmon", "bisque", "snow4"]

    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('cyan')
    color = color_inactive
    active: bool = False
    text: str = ''
    font = pygame.font.Font(None, 32)

    try:
        while True:
            display_surface.fill("black")
            draw_text("Main Menu", "white", display_surface, 10, 10)
            draw_text("Player list:", "white", display_surface, 1000, 10)

            mx, my = pygame.mouse.get_pos()#pylint:disable=invalid-name

            start_button = pygame.Rect(WINDOW_WIDTH / 2 - 90, 620, 200, 50)

            if start_button.collidepoint((mx, my)):
                if click:
                    game(players)
                    #reset lists
                    players = []
                    colors = ["red", "green", "yellow", "orange", "violet", "blue", "cyan", "darksalmon", "bisque", "snow4"]

            pygame.draw.rect(display_surface, (255,0,0), start_button)
            draw_text("START", "white", display_surface, WINDOW_WIDTH // 2 - 20, 630)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    LOGGER.info("Exited game.")
                    pygame.quit()
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                #input box logic
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint((mx, my)):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if len(players) < 10:
                                players.append(Player(text,colors.pop()))
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            name_txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, name_txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            display_surface.blit(name_txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(display_surface, color, input_box, 2)

            for index, player in enumerate(players):
                draw_text(str(index + 1) + ": " + player.name, "white", display_surface, 1000, (index + 1) * 40)

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
