"""Main module of pepugame
"""
import sys
from pepugame.game import game_loop

def main() -> str|None:
    """Main module of pepugame
    """
    return game_loop()

if __name__ == "__main__":
    sys.exit(main())
