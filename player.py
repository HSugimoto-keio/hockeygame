"""
    Playerクラスを表現
"""
from const import WINDOW_HEIGHT, WINDOW_WIDTH


class Player:
    """
    Playerクラス
    こちらでは必要な変数名と操作を表現
    posymin:ラケットの上端
    posymax:ラケットの下端(ともに当たり判定で使用)
    up:対応するボタンが押された時にラケットを上側に移動
    down:対応するボタンが押された時にラケットを下側に移動
    """
    def __init__(self, pid, color):
        """
        初期化
        引数なし
        size:ラケットの長さ
        point:点数
        posy,posxはラケットの上端の位置
        width:幅
        rectleft:左端
        rectright:右端
        """
        self.size = 100
        self.width = 10
        self.vely = 25
        self.velx = 25
        self.color = color
        self.pid = pid
        if pid == 0:
            self.rectleft = 0
            self.posx = self.posxright()
        if pid == 1:
            self.rectleft = WINDOW_WIDTH - self.width
            self.posx = self.rectleft
        self.player_init()

    def player_init(self):
        """
        試合ごとの初期化
        """
        self.point = 0
        self.posy = WINDOW_HEIGHT // 2

    def posymin(self):
        """
        ラケットの上端の位置
        """
        return self.posy - self.size // 2

    def posymax(self):
        """
        ラケットの下端の位置
        """
        return self.posy + self.size // 2

    def posxright(self):
        """
        ラケットの右端の位置
        """
        return self.rectleft + self.width

    def up(self):
        """
        上端に達しない限り,対応キーに応じてラケットを上に移動
        """
        self.posy = max(self.posy - self.vely, 0)

    def down(self):
        """
        下端に達しない限り,対応キーに応じてラケットを下に移動
        """
        self.posy = min(self.posy + self.vely, WINDOW_HEIGHT)
    
    def left(self):
        if self.pid == 0:
            self.rectleft = max(self.rectleft - self.velx, 0)
        elif self.pid == 1:
            self.rectleft = max(self.rectleft - self.velx, WINDOW_WIDTH//2)
    
    def right(self):
        if self.pid == 0:
            self.rectleft = min(self.rectleft + self.velx, WINDOW_WIDTH//2)
        elif self.pid == 1:
            self.rectleft = min(self.rectleft + self.velx, WINDOW_WIDTH)

    def draw(self, canvas):
        """
        ラケットの描画
        """
        
        canvas.create_rectangle(
            self.rectleft, self.posymin(),
            self.posxright(), self.posymax(),
            fill=self.color
        )
        '''
        canvas.create_oval(
            self.left(), self.up(),
            self.right(), self.down(),
            fill=self.color
            )
        
        '''
        
