"""
gameのメイン
python3 main.pyでGUIが起動
音ならすにはpip install pygame が必要
"""
from game import Game
# import pygame.mixer
from ball import Ball
from player import Player
from cpuplayer import CPUPlayer
from airhockeykeyboard import AirHockeyKeyBoard
from judge import Judge
from airhockeyjoyconcontroller import AirHockeyJoyConController

class AirhockeyGame(Game):
    """
    TennisGameクラス
    ゲーム本体でありマネージャ
    命名ルール
    state名→state_状態名
    stateの処理→proc_状態名
    ある程度まとまった共通処理→subproc_func
    """
    def __init__(self):
        """
        初期化
        windowはTk,canvasはCanvas
        キーボード操作はkeyboardに専任
        ゲーム,マッチの初期化を行い,ゲームを実行
        """
        self.gamename = "AirHockey"
        self.presenter = "Urayama"
        super().__init__(self.gamename, self.presenter)
        #self.controller = AirHockeyKeyBoard(self.screen)
        self.controller = AirHockeyJoyConController()
        self.judge = Judge()
        self.ball = Ball()
        # pygame.mixer.init()
        # pygame.mixer.music.load("./wakakichi.wav")
        self.player1 = Player(0, "red")
        self.player2 = Player(1, "cyan")  # Playerなら操作,CPUならランダム
        self.nextgame = False
        self.nextmatch = False
        self.player2selected = False

    def state_boot(self):
        """
        スタート画面
        →select
        """
        self.proc_boot()
        self.screen.boot()
        chstate = {self.controller.select(): self.state_select}
        self.nextstate(chstate, self.state_boot)

    def state_select(self):
        """
        CPUor2P選択
        →state_game
        """
        self.proc_select()
        self.screen.select()
        chstate = {
            self.player2selected: self.state_game
        }
        self.nextstate(chstate, self.state_select)

    def state_game(self):
        """
        game中
        →boot,gameresult,matchresult
        """
        self.proc_game()
        self.screen.game(self)
        chstate = {
            self.controller.boot(): self.state_boot,
            self.judge.is_gameover: self.state_gameresult,
            (not self.judge.is_gameover) and self.judge.is_matchover: self.state_matchresult
        }
        self.nextstate(chstate, self.state_game)

    def state_gameresult(self):
        """
        ゲーム結果画面
        →game, boot
        """
        self.proc_gameresult()
        self.screen.gameresult(self)
        chstate = {
            self.nextgame: self.state_game,
            self.controller.boot(): self.state_boot
        }
        self.nextstate(chstate, self.state_gameresult)

    def state_matchresult(self):
        """
        試合結果表示画面
        →game, boot
        """
        self.proc_matchresult()
        self.screen.matchresult(self)
        chstate = {
            self.nextmatch: self.state_game,
            self.controller.boot(): self.state_boot
        }
        self.nextstate(chstate, self.state_matchresult)

    def subproc_gameinit(self):
        """
        ゲームの初期化
        ゲームの終了判定フラグ→False
        ラケットの初期化
        """
        self.judge.gamereset()
        self.player1.player_init()
        self.player2.player_init()
        self.controller.setplayer(self.player1, self.player2)
        self.screen.draw_screen()
        self.player1.draw(self.screen.canvas)
        self.player2.draw(self.screen.canvas)
        self.subproc_matchinit()

    def subproc_matchinit(self):
        """
        マッチの初期化
        マッチの終了判定のみFalseにし,ボールの初期化
        """
        self.judge.matchreset()
        self.ball.ball_init()

    def proc_boot(self):
        """
        boot処理
        """
        # pygame.mixer.music.stop()
        self.subproc_gameinit()

    def proc_select(self):
        """
        select処理
        """
        self.player2selected = False
        if self.controller.vs_CPU():
            self.player2 = CPUPlayer(1, "violet")
            self.player2selected = True
            self.subproc_gameinit()
        elif self.controller.vs_2P():
            self.player2 = Player(1, "cyan")
            self.player2selected = True
            self.subproc_gameinit()

    def proc_game(self):
        """
        game処理
        """
        self.controller.movekey()
        if type(self.player1) is CPUPlayer:
            self.player1.move()
        if type(self.player2) is CPUPlayer:
            self.player2.move()
        self.ball.move_ball(self, self.player1, self.player2)
        self.player1.downaccl()
        self.player2.downaccl()
        self.judge.check_gameover(self.player1, self.player2)

        if self.controller.resetmatch():
            self.subproc_matchinit()

    def proc_gameresult(self):
        """
        gameresult処理
        """
        self.nextgame = False
        # pygame.mixer.music.stop()
        if self.controller.nextgame():
            self.subproc_gameinit()
            self.nextgame = True

    def proc_matchresult(self):
        """
        matchresult処理
        """
        self.nextmatch = False
        if self.controller.nextmatch():
            self.subproc_matchinit()
            self.nextmatch = True
