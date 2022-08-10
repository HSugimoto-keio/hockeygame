"""
汎用Game用基本パーツ
各ゲームはこれを継承する
"""
from screen import Screen


class Game:
    """
    汎用パーツを定義
    Screen動作と状態遷移の基本動作を定義
    """

    def __init__(self,gamename = "Game",presenter = "God"):
        """
        初期化
        """
        self.gamename = gamename
        self.presenter = presenter
        self.screen = Screen(self.gamename, self.presenter)
        self.screen.canvas.pack()

    def nextstate(self, statedict, nowstate):
        """
        statedictに用意されている行き先に遷移する。
        条件が揃わないとnowstateのまま
        """
        for key, nextstate in statedict.items():
            if key:
                self.screen.window.after(self.screen.mtime, nextstate)
                return
        self.screen.window.after(self.screen.mtime, nowstate)
        return
