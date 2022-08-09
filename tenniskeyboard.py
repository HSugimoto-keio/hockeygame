"""
keyboardの管理を担当
"""

from keyboard import KeyBoard
from player import Player


class TennisKeyBoard(KeyBoard):
    """
    キーボード操作を管理
    """
    def __init__(self):
        """
        keyboard管理を初期化
        主に辞書の作成
        """
        super().__init__()

    def setplayer(self, player1, player2):
        """
        playerのメソッドにキーを紐付
        """
        if type(player1) is Player:
            self.setoperation("w", player1.up)
            self.setoperation("s", player1.down)
        if type(player2) is Player:
            self.setoperation("i", player2.up)
            self.setoperation("k", player2.down)
