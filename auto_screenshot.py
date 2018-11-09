'''
Purpose: To take screenshots after specific time interval and save it
By: Shivanshu
'''

from threading import Timer
import pyautogui
import random

def auto():
    t_obj=Timer(2,auto)
    t_obj.start()
    pic = pyautogui.screenshot()
    name='Screenshot_'+str(random.randint(0,4))+'_.png'
    pic.save(name)


cnt=0
while cnt<6:
    auto()
    print cnt
    if cnt==5:
        break
    cnt+=1

