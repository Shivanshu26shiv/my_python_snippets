'''
This code will notify user is battery goes beyond certain level
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
