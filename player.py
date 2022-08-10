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
        self.size = 30
        self.width = 30
        self.vely = 25
        self.velx = 25
        self.color = color
        self.pid = pid
        self.player_init()

    def player_init(self):
        """
        試合ごとの初期化
        """
        self.point = 0
        self.posy = WINDOW_HEIGHT // 2
        self.posx = None
        if self.pid == 0:
            self.posx = 0 + self.width
        elif self.pid == 1:
            self.posx = WINDOW_WIDTH - self.width
        self.vvy = 0
        self.vvx = 0

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
    
    def posxmin(self):
        """
        ラケットの左端の位置
        """
        return self.posx - self.size // 2

    def posxmax(self):
        """
        ラケットの右端の位置
        """
        return self.posx + self.size // 2

    def posxopposite(self):
        """
        ラケットのposxの反対位置
        """
        op = None
        if self.pid == 0:
            op = self.posx - self.width
        elif self.pid == 1:
            op = self.posx + self.width
        return op

    def up(self):
        """
        上端に達しない限り,対応キーに応じてラケットを上に移動
        またホッケートークンの移動速度を決めるパラーメタもここで決定
        """
        self.vvy = -5
        if self.vvx > 0:
            self.vvx = max(self.vvx-1,0)
        elif self.vvx < 0:
            self.vvx = min(self.vvx+1,0)
        self.posy = max(self.posy - self.vely, 0)

    def down(self):
        """
        下端に達しない限り,対応キーに応じてラケットを下に移動
        またホッケートークンの移動速度を決めるパラーメタもここで決定
        """
        self.vvy = 5
        if self.vvx > 0:
            self.vvx = max(self.vvx-1,0)
        elif self.vvx < 0:
            self.vvx = min(self.vvx+1,0)
        self.posy = min(self.posy + self.vely, WINDOW_HEIGHT)
    
    def left(self):
        """
        プレイヤーそれぞれの左端に達しない限り,対応キーに応じてラケットを左に移動
        またホッケートークンの移動速度を決めるパラーメタもここで決定
        """
        self.vvx = -5
        if self.vvy > 0:
            self.vvy = max(self.vvy-1,0)
        elif self.vvy < 0:
            self.vvy = min(self.vvy+1,0)
        
        if self.pid == 0:
            self.posx = max(self.posx - self.velx, self.width)
        elif self.pid == 1:
            self.posx = max(self.posx - self.velx, WINDOW_WIDTH//2)
    
    def right(self):
        """
        プレイヤーそれぞれの左端に達しない限り,対応キーに応じてラケットを左に移動
        またホッケートークンの移動速度を決めるパラーメタもここで決定
        """
        self.vvx = 5
        if self.vvy > 0:
            self.vvy = max(self.vvy-1,0)
        elif self.vvy < 0:
            self.vvy = min(self.vvy+1,0)

        if self.pid == 0:
            self.posx = min(self.posx + self.velx, WINDOW_WIDTH//2)
        elif self.pid == 1:
            self.posx = min(self.posx + self.velx, WINDOW_WIDTH - self.width)
    
    def circlein(self, x, y):
        '''
        x,yの座標がプレイヤーのサークル内にあるかどうかを判定
        主にballの当たり判定に使用
        '''
        r = self.size // 2
        return (self.posx-x)**2 + (self.posy-y)**2 < r*r

    def draw(self, canvas):
        """
        ラケットの描画
        """
        canvas.create_oval(
            self.posxmin(), self.posymin(),
            self.posxmax(), self.posymax(),
            fill=self.color)
