import pygame
from pygame.locals import *
import time
 
def main() :
    pygame.init()
 
    while True:
        pygame.joystick.init()
        joycnt = pygame.joystick.get_count()
        joysticks = []
        for i in range(joycnt):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[i].init()
        #joystick0 = pygame.joystick.Joystick(0)
        #joystick0.init()
        # コントローラーの操作を取得
        eventlist = pygame.event.get()
 
        # 操作の中からボタンを押したときだけに絞り込む
        #eventlist = filter(lambda e : e.type == pygame.locals.JOYBUTTONDOWN , eventlist)
 
        # ボタン入力の読み込みを表示
        #print map(lambda x : x.button,eventlist)
        '''
        
        print(eventlist)
        for e in eventlist:
            if e.type == 1538:
                print(e.get_axis(0))
        '''
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYAXISMOTION:
                for i in range(joycnt):
                    x, y = joysticks[i].get_axis(0), joysticks[i].get_axis(1)
                    print(str(i)+'axis x:' + str(x) + ' axis y:' + str(y))
            elif e.type == pygame.locals.JOYHATMOTION:
                for i in range(joycnt):
                    x, y = joysticks[i].get_hat(0)
                    print (str(i)+'hat x:' + str(x) + ' hat y:' + str(y))
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                but = e.button
                for i in range(joycnt):
                    if joysticks[i].get_button(but):
                        print (str(i)+'button:' + str(e.button))
 
        time.sleep(0.1)
 
if __name__ == '__main__':
    pygame.joystick.init()
    try:
        joys = pygame.joystick.Joystick(0)
        joys.init()
        main()
    except pygame.error:
        print ('error has occured')