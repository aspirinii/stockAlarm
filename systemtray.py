from pystray import MenuItem as item
import pystray
from PIL import Image
import schedule
import time
import datetime
import threading

def action():
    pass

def job():
    print("I'm working...",datetime.datetime.now())


def scheduleTest():
    schedule.every(2).seconds.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


image = Image.open("stockAlarm/paw.png")
menu = (item('Start', lambda : scheduleTest()), item('Test', lambda : print("test")), item('Stop', lambda : icon.stop()))
icon = pystray.Icon("What", image, "Cat", menu)
icon.run()




def ten_counter():
    for i in range(10):
        time.sleep(1)
        print('----',i)
        # if i>3 :
        #     timer.cancel()

def elev_counter():
    for i in range(10):
        time.sleep(1)
        print('++++',i)
        # if i>5 :
        #     timer2.cancel()

# ten_counter()
timer = threading.Thread(target=ten_counter)
timer2 = threading.Thread(target=elev_counter)
timer.daemon = True
timer2.daemon = True

timer.start()
timer2.start()


def do_work(id, stop):
    print("I am thread", id)
    while True:
        print("I am thread {} doing something".format(id))
        if stop():
            print("  Exiting loop.")
            break
    print("Thread {}, signing off".format(id))


def main():
    stop_threads = False
    image = Image.open("stockAlarm/paw.png")
    menu = (item('Start', lambda : scheduleTest()), item('Test', lambda : print("test")), item('Stop', lambda : icon.stop()))
    icon = pystray.Icon("What", image, "Cat", menu)
    icon.run()
    WorkList = []
    workers = []
    for id, iw in range(1,2), WorkList:
        tmp = threading.Thread(target=iw, args=(id, lambda: stop_threads))
        workers.append(tmp)
        tmp.start()

    stop_threads = True
    for worker in workers:
        worker.join()
    print('Finish.')

if __name__ == '__main__':
    main()