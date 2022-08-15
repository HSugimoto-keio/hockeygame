#from pyjoycon import JoyCon, get_R_id
from joyconcontroller2 import JoyConController
from player import Player

P1 = "0"
P2 = "1"
A = "a"
X = "x"
B = "b"
Y = "y"
SL = "sl"
SR = "sr"
MNS = "8"
PLS = "plus"
LST = "10"
RST = "11"
HM = "home"
PCT = "13"
LR = "r"
ZLR = "zr"

class AirHockeyJoyConController(JoyConController):

    #def __init__(self):
        #super.__init__()

    def setplayer(self, player1, player2):
        """
        playerのメソッドにキーを紐付
        """
        if type(player1) is Player:
            self.setoperation(P1+"Up", player1.up)
            self.setoperation(P1+"Down", player1.down)
            self.setoperation(P1+"Left", player1.left)
            self.setoperation(P1+"Right", player1.right)
        
        if type(player2) is Player:
            self.setoperation(P2+"Up", player2.up)
            self.setoperation(P2+"Down", player2.down)
            self.setoperation(P2+"Left", player2.left)
            self.setoperation(P2+"Right", player2.right)
        

    def boot(self):
        """
        boot画面への遷移
        """
        return self.is_pressed(HM)
    
    def select(self):
        """
        select画面への遷移
        """
        return self.is_pressed(X)

    def vs_CPU(self):
        """
        CPU対戦選択
        """
        return self.is_pressed(SR)

    def vs_2P(self):
        """
        CPU対戦選択
        """
        return self.is_pressed(SL)

    def nextmatch(self):
        """
        次マッチ画面への遷移
        """
        return self.is_pressed(X)
    
    def nextgame(self):
        """
        次ゲーム画面への遷移
        """
        return self.is_pressed(X)

    def resetmatch(self):
        """
        マッチリセットのためのフラグ
        """
        return self.is_pressed(B)