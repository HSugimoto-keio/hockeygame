"""
keyboardの管理を担当
"""

from keyboard import KeyBoard
from player import Player


class AirHockeyKeyBoard(KeyBoard):
    """
    キーボード操作を管理
    """
    def __init__(self,screen):
        """
        keyboard管理を初期化
        主に辞書の作成
        """
        super().__init__(screen)

    def setplayer(self, player1, player2):
        """
        playerのメソッドにキーを紐付
        """
        if type(player1) is Player:
            self.setoperation("w", player1.up)
            self.setoperation("s", player1.down)
            self.setoperation("a", player1.left)
            self.setoperation("d", player1.right)
        if type(player2) is Player:
            self.setoperation("i", player2.up)
            self.setoperation("k", player2.down)
            self.setoperation("j", player2.left)
            self.setoperation("l", player2.right)
    
    def boot(self):
        """
        boot画面への遷移
        """
        return self.is_pressed("Return")
    
    def select(self):
        """
        select画面への遷移
        """
        return self.is_pressed("space")

    def vs_CPU(self):
        """
        CPU対戦選択
        """
        return self.is_pressed("1")

    def vs_2P(self):
        """
        CPU対戦選択
        """
        return self.is_pressed("2")

    def nextmatch(self):
        """
        次マッチ画面への遷移
        """
        return self.is_pressed("space")
    
    def nextgame(self):
        """
        次ゲーム画面への遷移
        """
        return self.is_pressed("space")

    def resetmatch(self):
        """
        マッチリセットのためのフラグ
        """
        return self.is_pressed("space")
