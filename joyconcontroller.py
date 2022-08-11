from pyjoycon import JoyCon, get_R_id

class JoyConController:

    def __init__(self):
        self.joycon_id = get_R_id()
        self.joycon = JoyCon(*self.joycon_id)
        self.operationset = {}
        self.pressed = {}
        self.now_status = self.get_status()
    
    def get_status(self):
        self.now_status = self.joycon.get_status()
    
    def key_pressed(self):
        """
        keyが押されるとpressedの辞書に登録
        """
        for button in self.now_status['buttons']['right']:
            if self.now_status['buttons']['right'][button]!=0:
                self.pressed[button] = True

    def key_released(self):
        """
        keyが離されるとpressedの辞書から削除
        """
        #self.pressed.pop(event.keysym, None)
        for button in self.now_status['buttons']['right']:
            if self.now_status['buttons']['right'][button]==0:
                self.pressed.pop(button, None)

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