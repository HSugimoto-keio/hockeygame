import pygame
from pygame.locals import *

P1 = 0
P2 = 1
A = 0
X = 1
B = 2
Y = 3
SL = 4
SR = 5
MNS = 8
PLS = 9
LST = 10
RST = 11
HM = 12
PCT = 13
LR = 14
ZLR = 15

THX = 100
THY = 100

ACGY = 'gyro'


from pyjoycon import JoyCon, get_R_id, get_L_id

class JoyConController:

    def __init__(self):
        self.joycon_id = get_R_id()
        self.joycon = JoyCon(*self.joycon_id)
        self.joycon_id2 = get_L_id()
        self.joycon2 = JoyCon(*self.joycon_id2)
        self.operationset = {}
        self.pressed = {}
        self.get_statusinit()
        self.setst1 = self.now_status[ACGY]
        self.setst2 = self.now_status2[ACGY]
        self.setoperation("r" ,self.set_stat1)
        self.setoperation("l", self.set_stat2)

    def set_stat1(self):
        self.setst1 = self.now_status[ACGY]

    def set_stat2(self):
        self.setst2 = self.now_status2[ACGY]

    def get_statusinit(self):
        self.now_status = self.joycon.get_status()
        self.now_status2 = self.joycon2.get_status()
        #self.key_pressed()
        #self.key_released()
        print(self.now_status["accel"])
        print(self.now_status["gyro"])
    
    def get_status(self):
        self.now_status = self.joycon.get_status()
        self.now_status2 = self.joycon2.get_status()
        self.key_pressed()
        self.key_released()
        #print(self.now_status["accel"])
        #print(self.now_status["gyro"])
    
    def key_pressed(self):
        """
        keyが押されるとpressedの辞書に登録
        """
        
        for button in self.now_status['buttons']['right']:
            if self.now_status['buttons']['right'][button]!=0:
                self.pressed[button] = True
        for button in self.now_status['buttons']['shared']:
            if self.now_status['buttons']['shared'][button]!=0:
                self.pressed[button] = True
        #if self.now_status['analog-sticks']['right']['horizontal']<1600:
        if self.now_status[ACGY]['z'] - self.setst1['z'] < -THX:
            self.pressed["0Left"] = True
        #if self.now_status['analog-sticks']['right']['horizontal']>2400:
        if self.now_status[ACGY]['z'] - self.setst1['z'] > THX:
            self.pressed["0Right"] = True
        #if self.now_status['analog-sticks']['right']['vertical']<1600:
        if self.now_status[ACGY]['y'] - self.setst1['y'] < -THY:
            self.pressed["0Down"] = True
        #if self.now_status['analog-sticks']['right']['vertical']>2400:
        if self.now_status[ACGY]['y'] - self.setst1['y'] > THY:
            self.pressed["0Up"] = True
        if self.now_status2['analog-sticks']['left']['horizontal']<1600:
            self.pressed["1Left"] = True
        if self.now_status2['analog-sticks']['left']['horizontal']>2400:
            self.pressed["1Right"] = True
        if self.now_status2['analog-sticks']['left']['vertical']<1600:
            self.pressed["1Down"] = True
        if self.now_status2['analog-sticks']['left']['vertical']>2400:
            self.pressed["1Up"] = True

    def key_released(self):
        """
        keyが離されるとpressedの辞書から削除
        """
        #self.pressed.pop(event.keysym, None)
        for button in self.now_status['buttons']['right']:
            if self.now_status['buttons']['right'][button]==0:
                self.pressed.pop(button, None)
        for button in self.now_status['buttons']['shared']:
            if self.now_status['buttons']['shared'][button]==0:
                self.pressed.pop(button, None)
        #if self.now_status['analog-sticks']['right']['horizontal']<=2400 and \
            #self.now_status['analog-sticks']['right']['horizontal']>=1600:
        if self.now_status[ACGY]['z'] - self.setst1['z'] >= -THX and \
            self.now_status[ACGY]['z'] - self.setst1['z'] <= THX:
            self.pressed.pop("0Right", None)
            self.pressed.pop("0Left", None)
        #if self.now_status['analog-sticks']['right']['vertical']<=2400 and \
        #    self.now_status['analog-sticks']['right']['vertical']>=1600:
        if self.now_status[ACGY]['y'] - self.setst1['y'] >= -THY and \
            self.now_status[ACGY]['y'] - self.setst1['y'] <= THY:
            self.pressed.pop("0Down", None)
            self.pressed.pop("0Up", None)
        if self.now_status2['analog-sticks']['left']['horizontal']<=2400 and \
            self.now_status2['analog-sticks']['left']['horizontal']>=1600:
            self.pressed.pop("1Right", None)
            self.pressed.pop("1Left", None)
        if self.now_status2['analog-sticks']['left']['vertical']<=2400 and \
            self.now_status2['analog-sticks']['left']['vertical']>=1600:
            self.pressed.pop("1Down", None)
            self.pressed.pop("1Up", None)

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
