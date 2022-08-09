"""
試合状態の判定担当者Judge
"""


class Judge:
    """
    ゲーム,マッチの状態を判定する
    """
    def __init__(self):
        """
        Judgeの初期化
        """
        self.is_gameover = False
        self.is_matchover = False
        self.gamepoint = 3

    def is_player_winner(self, player, enemy):
        """
        playerが勝利条件をみたし,enemyに勝ったかどうかを判定
        """
        return player.point >= self.gamepoint and player.point > enemy.point

    def check_gameover(self, player_a, player_b):
        """
        gameoverを判定
        条件を満たせばis_gameoverをset
        """
        if self.is_matchover is False:
            pass
        if self.is_player_winner(player_a, player_b) or self.is_player_winner(player_b, player_a):
            self.gameset()

    def gameset(self):
        """
        is_gameoverをset
        """
        self.is_gameover = True

    def matchset(self):
        """
        is_matchoverをset
        """
        self.is_matchover = True

    def gamereset(self):
        """
        is_gameoverをreset
        """
        self.is_gameover = False

    def matchreset(self):
        """
        is_matchoverをreset
        """
        self.is_matchover = False
