from pystray import MenuItem as item
import pystray
from PIL import Image
import schedule
import time
import datetime

def action():
    pass

def job():
    print("I'm working...",datetime.datetime.now())


def scheduleTest():
    schedule.every(2).seconds.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


image = Image.open("cat.png")
menu = (item('Start', lambda : scheduleTest()), item('Test', lambda : print("test")), item('Stop', lambda : icon.stop()))
icon = pystray.Icon("What", image, "Cat", menu)
icon.run()






