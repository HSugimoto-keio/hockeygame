"""
keyboardの管理を担当
"""


class KeyBoard:
    """
    キーボード操作を管理
    """
    def __init__(self):
        """
        keyboard管理を初期化
        主に辞書の作成
        """
        self.pressed = {}
        self.operationset = {}

    def key_pressed(self, event):
        """
        keyが押されるとpressedの辞書に登録
        """
        self.pressed[event.keysym] = True

    def key_released(self, event):
        """
        keyが離されるとpressedの辞書から削除
        """
        self.pressed.pop(event.keysym, None)

    def is_pressed(self, key):
        """
        keyが押されているかどうかのboot値
        """
        return key in self.pressed

    def setoperation(self, key, action):
        """
        辞書にkeyと対応する操作を設定
        """
        self.operationset[key] = action

    def movekey(self):
        """
        辞書を見てキーが今押されているかを確認し次の動作を決定
        """
        for key, ope in self.operationset.items():
            if self.is_pressed(key):
                ope()
