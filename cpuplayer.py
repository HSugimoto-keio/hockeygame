"""
CPU動作を定義
Player継承
"""
import random
from player import Player


class CPUPlayer(Player):
    """
    親:Player
    CPU用の動きを管理
    """
    def __init__(self, pid, color):
        """
        初期化:
        現状はplayerと同じ
        """
        super().__init__(pid, color)

    def move(self):
        """
        CPUの行動を管理
        主にCPUPlayer.up,CPUPlayer.downの動きを決定
        """
        rand = random.randint(-1, 1)
        if rand == -1:
            self.up()
        elif rand == 1:
            self.down()
        
        rand = random.randint(-1, 1)
        if rand == -1:
            self.left()
        elif rand == 1:
            self.right()
