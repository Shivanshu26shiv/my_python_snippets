
'''
This code will notify user is battery goes beyond certain level
Purpose: Currently my notebook shuts down abnormally after 50% battery,
Hence I have created a script that will notify me as soon as battery charge reaches 55%
Later I converted this file to exe using "pyinstaller -w scriptname.py command",
then pushed the executable into Windows startup.
By: Shivanshu
'''


import time
import psutil
import winsound
import os
#Below notification module is commented since it was giving issues with pyinstaller while py->exe
#from plyer import notification

while(1):
    battery = psutil.sensors_battery()
    print battery
    if battery[0]<55 and battery[2]==False:
        os.system("start cmd")
        winsound.Beep(200,1000)
    #Below code works if we dont have the need to convert py->exe
    '''
        notification.notify(
            title='Battery status!',
            message='Current battery: '+str(battery[0])+'%',
            app_name='Alert!'
            #app_icon='path/to/the/icon.png'
            )
    '''
    time.sleep(30)
