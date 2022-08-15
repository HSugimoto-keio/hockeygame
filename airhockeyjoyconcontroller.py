#from pyjoycon import JoyCon, get_R_id
from joyconcontroller import JoyConController
from player import Player

P1 = "0"
P2 = "1"
A = "0"
X = "1"
B = "2"
Y = "3"
SL = "4"
SR = "5"
MNS = "8"
PLS = "9"
LST = "10"
RST = "11"
HM = "12"
PCT = "13"
LR = "14"
ZLR = "15"

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
        return self.is_pressed(P1+HM)
    
    def select(self):
        """
        select画面への遷移
        """
        return self.is_pressed(P1+X)

    def vs_CPU(self):
        """
        CPU対戦選択
        """
        return self.is_pressed(P1+SR)

    def vs_2P(self):
        """
        CPU対戦選択
        """
        return self.is_pressed(P1+SL)

    def nextmatch(self):
        """
        次マッチ画面への遷移
        """
        return self.is_pressed(P1+X)
    
    def nextgame(self):
        """
        次ゲーム画面への遷移
        """
        return self.is_pressed(P1+X)

    def resetmatch(self):
        """
        マッチリセットのためのフラグ
        """
        return self.is_pressed(P1+B)