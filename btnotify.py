'''
This code will notify user is battery goes beyond certain level
By: Shivanshu
Purpose: Currently my notebook shuts down abnormally after 50% battery,
Hence I have created a script that will notify me as soon as battery charge reaches 55%
Later I converted this file to exe using "pyinstaller -w scriptname.py command",
then pushed the executable into Windows startup.
'''


import time
import psutil
import winsound
import os
#from plyer import notification

while(1):
    battery = psutil.sensors_battery()
    print battery
    if battery[0]<55 and battery[2]==False:
        os.system("start cmd")
        winsound.Beep(200,1000)
    '''
        notification.notify(
            title='Battery status!',
            message='Current battery: '+str(battery[0])+'%',
            app_name='Alert!'
            #app_icon='path/to/the/icon.png'
            )
    '''
    time.sleep(30)
