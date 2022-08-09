"""
Ballクラスを表現
"""
import random
from const import WINDOW_HEIGHT, WINDOW_WIDTH


class Ball:
    """
    Ballクラス
    テニスボール
    ゲームの判定に関わる動作
    left:ボールの左端を表現
    right:ボールの右端を表現
    up:ボールの上端を表現
    down:ボールの下端を表現
    nextposy:次のフレームでの高さの位置を表現
    nextposx:次のフレームでの横方向の位置を表現
    move_ball:ボールの動きを表現&マッチレベルの判定
    """
    def __init__(self):
        """
        初期化
        サーブ権はランダム
        velx,vely:速度
        posx,posy:位置
        size:ボールのサイズ
        """
        self.ball_init()
        self.size = 10

    def ball_init(self):
        """
        マッチ毎の初期化
        サーブ権はランダム
        velx,vely:速度
        posx,posy:位置
        size:ボールのサイズ
        """
        if random.randint(0, 1) == 0:
            self.posx = 0
            self.velx = 15
        else:
            self.posx = WINDOW_WIDTH - 1
            self.velx = -15
        self.posy = 250
        self.vely = -15

    def left(self):
        """
        ボールの左端を表現
        """
        return self.posx - self.size

    def right(self):
        """
        ボールの右端を表現
        """
        return self.posx + self.size

    def up(self):
        """
        ボールの上端を表現
        """
        return self.posy - self.size

    def down(self):
        """
        ボールの下端を表現
        """
        return self.posy + self.size

    def nextposy(self):
        """
        次のフレームのボールの高さを表現
        """
        return self.posy + self.vely

    def nextposx(self):
        """
        次のフレームのボールの横方向の位置を表現
        """
        return self.posx + self.velx

    def move_ball(self, gamemaster, player1, player2):
        """
        引数:gamemaster = main,player1,player2
        matchが終われば速さ=0
        ボールが画面上端,下端に当たれば同じ速度で跳ね返る
        ボールがラケットに当たれば同じ速度で跳ね返るが,ランダムで上下が逆転
        ラケットにあたっておらず右端(左端)に行けばmatchが終わり,プレイヤー1(プレイヤー2)の点数を1追加
        以上の特殊なことがなければ次の位置と予測できる位置にボールを移動
        """
        if gamemaster.judge.is_matchover:
            self.velx = 0
            self.vely = 0

        if self.nextposy() < 0 or self.nextposy() > WINDOW_HEIGHT:
            self.vely *= -1

        if self.nextposx() > WINDOW_WIDTH and\
            (player2.posymin() <= self.nextposy() and\
                self.nextposy() <= player2.posymax()):
            self.velx *= -1
            if random.randint(0, 1) == 0:
                self.vely *= -1

        if self.nextposx() < 0 and\
            (player1.posymin() <= self.nextposy() and\
                self.nextposy() <= player1.posymax()):
            self.velx *= -1
            if random.randint(0, 1) == 0:
                self.vely *= -1

        if self.nextposx() < 0:
            player2.point += 1
            gamemaster.judge.matchset()

        if self.nextposx() > WINDOW_WIDTH:
            player1.point += 1
            gamemaster.judge.matchset()

        if self.nextposy() >= 0 and self.nextposy() <= WINDOW_HEIGHT:
            self.posy = self.nextposy()

        if self.nextposx() >= 0 and self.nextposx() <= WINDOW_WIDTH:
            self.posx = self.nextposx()

    def draw(self, canvas):
        """
        ボールの描画
        """
        canvas.create_oval(
            self.left(), self.up(),
            self.right(), self.down(),
            fill="yellow")
