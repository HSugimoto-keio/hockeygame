from pyjoycon import JoyCon, get_R_id
from joyconcontroller import JoyConController
from player import Player

class AirHockeyJoyConController(JoyConController):

    def __init__(self):
        super.__init__()

    def setplayer(self, player1, player2):
        """
        playerのメソッドにキーを紐付
        """
        if type(player1) is Player:
            self.setoperation("y", player1.up)
            self.setoperation("a", player1.down)
            self.setoperation("b", player1.left)
            self.setoperation("x", player1.right)
        '''
        if type(player2) is Player:
            self.setoperation("i", player2.up)
            self.setoperation("k", player2.down)
            self.setoperation("j", player2.left)
            self.setoperation("l", player2.right)
        '''

    def boot(self):
        """
        boot画面への遷移
        """
        return self.is_pressed("sl")
    
    def select(self):
        """
        select画面への遷移
        """
        return self.is_pressed("sr")

    def vs_CPU(self):
        """
        CPU対戦選択
        """
        return self.is_pressed("sr")

    def vs_2P(self):
        """
        CPU対戦選択
        """
        return self.is_pressed("sl")

    def nextmatch(self):
        """
        次マッチ画面への遷移
        """
        return self.is_pressed("sr")
    
    def nextgame(self):
        """
        次ゲーム画面への遷移
        """
        return self.is_pressed("sr")

    def resetmatch(self):
        """
        マッチリセットのためのフラグ
        """
        return self.is_pressed("sr")