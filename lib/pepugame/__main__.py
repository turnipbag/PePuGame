"""Main module of pepugame
"""
import sys
from pepugame.game import Game

def main() -> str|None:
    """Main module of pepugame
    """
    game = Game()
    return game.start()

if __name__ == "__main__":
    sys.exit(main())
