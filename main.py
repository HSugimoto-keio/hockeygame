"""
mainFile
使用しているGameをgameに代入してプレイ
"""
from tennisgame import TennisGame


def main():
    """
    game起動(gameに代入しているgameがスタートする)
    """
    game = TennisGame()
    game.state_boot()
    game.screen.window.mainloop()


if __name__ == "__main__":
    main()
