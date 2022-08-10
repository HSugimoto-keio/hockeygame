"""
mainFile
使用しているGameをgameに代入してプレイ
"""
from airhockeygame import AirhockeyGame


def main():
    """
    game起動(gameに代入しているgameがスタートする)
    """
    game = AirhockeyGame()
    game.state_boot()
    game.screen.window.mainloop()


if __name__ == "__main__":
    main()
