# エアホッケーの使い方
## 1.ルール
上下に動くラケットを動かしてボールを跳ね返そう。相手のラケットより奥に行けば1ポイントGET!,自分のラケットよりも手前に行けば相手に1ポイント取られるよ。
3ポイント取ったほうが勝利！

## 2.操作方法
ゲームスタート方法

`python3 main.py`で起動するとスタート画面に行く

スペースキーで次のマッチが始まる

slect画面の指示に従いCPU対戦は1,2P対戦は2をおすと始まる。

ゲームオーバー時にスペースキーで次のゲームが始まる。

なお,ゲームオーバー時にReturnキーを押すとスタート画面に戻る

プレイヤー1(左ラケット):

wキー:ラケットが上方向に移動

sキー:ラケットが下方向に移動

aキー:ラケットが左方向に移動

dキー:ラケットが右方向に移動


プレイヤー2(右ラケット):

iキー:ラケットが上方向に移動

kキー:ラケットが下方向に移動

jキー:ラケットが左方向に移動

lキー:ラケットが右方向に移動

## 3.各ファイルの説明
共通構造
```html:File
    main.py
    game.py
    keyboard.py
```

main.py以外のこれらは継承前提で作られており,使用する際はそのゲームに特化した構造になるようにする。main.pyには遊びたいゲームを代入して起動する。

ゲーム基幹部分
```html:File
    airhockeygame.py
    airhockeykeyboard.py
    screen.py
    const.py
```

ゲーム内容部分
```html:File
    ball.py
    player.py
    cpuplayer.py
    judge.py
```

## 4.joyconについて
接続はpygameを使用

Linuxの場合はhttps://www.reddit.com/r/Stadia/comments/egcvpq/comment/fc5s7qm/
を参考にいじる必要あるかも。(udevについては各自で調べてください)