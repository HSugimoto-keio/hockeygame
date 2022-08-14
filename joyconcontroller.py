import pygame
from pygame.locals import *

A = 0
X = 1
B = 2
Y = 3
SL = 4
SR = 5


class JoyConController:
    def __init__(self):
        pygame.joystick.init()
        self.joys = pygame.joystick.Joystick(0)
        self.joys.init()
        pygame.init()
        self.operationset = {}
        self.pressed = {}
        self.sticks = {}
        self.now_status = self.get_status()
    
    def get_status(self):
        self.now_status_event = pygame.event.get()
        self.now_status = []
        
        for e in self.now_status_event:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYAXISMOTION:
                x, y = self.joys.get_axis(0), self.joys.get_axis(1)
                print('axis x:' + str(x) + ' axis y:' + str(y))
            elif e.type == pygame.locals.JOYHATMOTION:
                x, y = self.joys.get_hat(0)
                self.sticks['x'] = x
                self.sticks['y'] = y
                if x == 1:
                    self.pressed['Right'] = True
                elif x == -1:
                    self.pressed['Left'] = True
                elif x == 0:
                    self.pressed.pop('Right', None)
                    self.pressed.pop('Left', None)

                if y == 1:
                    self.pressed['Up'] = True
                elif y == -1:
                    self.pressed['Down'] = True
                elif y == 0:
                    self.pressed.pop('Up', None)
                    self.pressed.pop('Down', None)
                
                #print ('hat x:' + str(x) + ' hat y:' + str(y))
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                self.pressed[e.button] = True
                #print ('button:' + str(e.button))
            elif e.type == pygame.locals.JOYBUTTONUP:
                #self.pressed[e.button] = True
                self.pressed.pop(e.button, None)
                #print ('button:' + str(e.button))

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
    
    def is_pressed(self, key):
        """
        keyが押されているかどうかのboot値
        """
        return key in self.pressed

if __name__ == '__main__':
    try:
        joycont = JoyConController()
        while True:
            eventlist = pygame.event.get()
            for e in eventlist:
                

                if e.type == pygame.locals.JOYAXISMOTION:
                    x, y = joycont.joys.get_axis(0), joycont.joys.get_axis(1)
                    print('axis x:' + str(x) + ' axis y:' + str(y))
                elif e.type == pygame.locals.JOYHATMOTION:
                    x, y = joycont.joys.get_hat(0)
                    print ('hat x:' + str(x) + ' hat y:' + str(y))
                elif e.type == pygame.locals.JOYBUTTONDOWN:
                    print ('button:' + str(e.button))
        
    except pygame.error:
        print('error')






'''
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
'''