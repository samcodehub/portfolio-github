# pip install psutil
# pip install plyer

import psutil
from plyer import notification
import time

def conversion(sec): # function to convert seconds to minutes or hour
    sec_value = sec%(24*3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min_value = sec_value// 60
    sec_value %= 60
    return hour_value, min_value

while True:
    battery = psutil.sensors_battery()
    h,m = conversion(battery.secsleft)
    notification.notify(
        title = "Battery Percentage",
        message =f'{h}Hr {m}Min {battery.percent}% remaining',
        timeout = 10 
    )
    time.sleep(60*60)  # notify after every 1 hour