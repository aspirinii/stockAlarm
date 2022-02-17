from pystray import MenuItem as item
import pystray
from PIL import Image
import schedule
import time
import datetime
import threading
from send_kakao_message import send_message
from reretrieve_token import reissuance
from scraping_yahoofinance import scraping_price
from log_log import logging_log

thresholdPrice = 3000
ticker = "GOOGL"

def job():
    price = scraping_price(ticker)
    if price > thresholdPrice:
        reissuance() #테스트할땐 잠깐 홀딩
        text = f"{ticker} is {price}"
        send_message(text)
    else:
        logging_log("Value is not over but App is working now")
    

def do_work():
    reissuance()
    send_message("--Start threading--")
    schedule.every().day.at("17:30").do(job)
    schedule.every().day.at("08:30").do(job)
    schedule.every(30).minutes.do(job)
    # schedule.every(10).seconds.do(job) #test function

    while True:
        schedule.run_pending()
        time.sleep(1)

def test_app():
    send_message("--Message Test--")


def make_wintray():
    stockAlram=threading.Thread(target=do_work,daemon=True,)
    test_trd=threading.Thread(target=test_app,daemon=True,)
    image = Image.open("paw.png")
    menu = (item('Start', lambda : stockAlram.start()),
    # item('Stop Working', lambda : x=True, stop_threads ),
    item('Message Test', lambda : test_trd.start()), 
    item('Stop', lambda : icon.stop()))
    icon = pystray.Icon("What", image, "Cat", menu)
    icon.run()




