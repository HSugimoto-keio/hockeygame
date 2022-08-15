"""
画面管理マネージャscreenを作成
"""


from tkinter import Tk, Canvas
from const import GOAL_HEIGHT, GOAL_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT


class Screen:
    """
    画面作成に関わる操作を管理
    命名ルール:
    stateの画面→state名そのまま
    それ以外→draw_func
    """
    def __init__(self, gamename, presenter):
        """
        window:画面全体の管理
        canvas:中のメインの白画面を管理
        mtime:画面更新間隔(ms)
        """
        self.gamename = gamename
        self.presenter = presenter
        self.window = Tk()
        self.canvas = Canvas(
            self.window,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )
        self.mtime = 50

    def draw_display_point(self, gamemanager):
        """
        point表示のための文生成
        """
        p_1 = "Player1:" + str(gamemanager.player1.point)
        p_2 = "Player2:" + str(gamemanager.player2.point)
        return p_1 + "  " + p_2

    def draw_screen(self):
        """
        画面背景を描画
        """
        self.canvas.delete('all')
        self.canvas.create_rectangle(
            0, 0, WINDOW_WIDTH, WINDOW_HEIGHT,
            fill="white", width=0
        )

    def draw_court(self):
        """
        試合中の画面背景=ホッケーボードを描画
        """
        self.canvas.delete('all')
        self.canvas.create_rectangle(
            0, 0, WINDOW_WIDTH, WINDOW_HEIGHT,
            fill="white", width=0
        )

        gurard_color = "blue"
        
        self.canvas.create_rectangle(
            WINDOW_WIDTH // 2 - 5, 0, WINDOW_WIDTH // 2 + 5, WINDOW_HEIGHT,
            fill="pink", width=0
        )

        self.canvas.create_rectangle(
            0, 0, 0 + GOAL_WIDTH, WINDOW_HEIGHT//2 - GOAL_HEIGHT//2,
            fill=gurard_color, width=0
        )

        self.canvas.create_rectangle(
            0, WINDOW_HEIGHT//2 + GOAL_HEIGHT//2, 0 + GOAL_WIDTH, WINDOW_HEIGHT,
            fill=gurard_color, width=0
        )

        self.canvas.create_rectangle(
            WINDOW_WIDTH - GOAL_WIDTH, 0, WINDOW_WIDTH, WINDOW_HEIGHT//2 - GOAL_HEIGHT//2,
            fill=gurard_color, width=0
        )

        self.canvas.create_rectangle(
            WINDOW_WIDTH - GOAL_WIDTH, WINDOW_HEIGHT//2 + GOAL_HEIGHT//2, WINDOW_WIDTH, WINDOW_HEIGHT,
            fill=gurard_color, width=0
        )

    def draw_gameitem(self, gamemanager):
        """
        試合の描画機能をまとめた関数
        """
        self.draw_court()
        gamemanager.ball.draw(self.canvas)
        gamemanager.player1.draw(self.canvas)
        gamemanager.player2.draw(self.canvas)

    def draw_result(self, gamemanager):
        """
        結果の画面表示
        """
        point1 = gamemanager.player1.point
        point2 = gamemanager.player2.point
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100,
            text=str(point1)+"  -  "+str(point2),
            anchor="center", fill="black", font=("roman", 25)
        )

    def boot(self):
        """
        スタート画面
        """
        self.draw_screen()
        self.window.title("Let's start! Press X!")
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
            text=self.gamename,
            anchor="center", fill="blue", font=("roman", 40, "bold")
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100,
            text=self.presenter+" Presents",
            anchor="center", fill="red", font=("roman", 30, "italic")
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT//2 + 150,
            text="press X",
            anchor="center", fill="green", font=("roman", 25)
        )

    def select(self):
        """
        選択画面表示
        """
        self.draw_screen()
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100,
            text="VS CPU? -> SR",
            anchor="center", fill="black", font=("roman", 25)
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
            text="VS 2P? -> SL",
            anchor="center", fill="black", font=("roman", 25)
        )

    def game(self, gamemanager):
        """
        play中の表示形式
        主にwindowタイトルバーの表示
        """
        self.draw_gameitem(gamemanager)
        self.window.title(self.draw_display_point(gamemanager))

    def gameresult(self, gamemanager):
        """
        ゲーム結果画面
        """
        self.draw_result(gamemanager)
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
            text="Game Set!!",
            anchor="center", fill="orange", font=("roman", 25)
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100,
            text="New Game? -> Press X",
            anchor="center", fill="green", font=("roman", 15)
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 200,
            text="Return to Start screen? -> Press Home",
            anchor="center", fill="green", font=("roman", 15)
        )
        if gamemanager.judge.is_player_winner(gamemanager.player1, gamemanager.player2):
            self.window.title("Player1 Win!!: " + self.draw_display_point(gamemanager))
        elif gamemanager.judge.is_player_winner(gamemanager.player2, gamemanager.player1):
            self.window.title("Player2 Win!!: " + self.draw_display_point(gamemanager))
        else:
            # 生じないはずだがバグに備えて
            self.window.title("Draw: " + self.draw_display_point(gamemanager))

    def matchresult(self, gamemanager):
        """
        試合結果表示
        """
        self.draw_result(gamemanager)
        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100,
            text="Press X",
            anchor="center", fill="green", font=("roman", 15)
        )
        self.window.title(self.draw_display_point(gamemanager))
