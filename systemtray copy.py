from pystray import MenuItem as item
import pystray
from PIL import Image
import schedule
import time
import datetime
import threading

def job():
    print("I'm working...",datetime.datetime.now())

def do_work():
    print("I am thread")
    schedule.every(2).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
        # if stop():
        #     print("  Exiting loop.")
        #     break
    print("Thread, signing off")

# def finish_work(thr):
#     global stockAlarm = True
#     thr.join()
#     print('Finish.')


def main():
    stop_threads = False
    stockAlram=threading.Thread(target=do_work,daemon=True,)
    image = Image.open("paw.png")
    menu = (item('Start', lambda : stockAlram.start()),
    # item('Stop Working', lambda : x=True, stop_threads ),
    item('interve Test', lambda : print('iterve test work')), 
    item('Stop', lambda : icon.stop()))
    icon = pystray.Icon("What", image, "Cat", menu)
    icon.run()




if __name__ == '__main__':
    main()