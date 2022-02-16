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


def job():
    print("I'm working...",datetime.datetime.now())
    reissuance() #테스트할땐 잠깐 홀딩
    ticker = "GOOGL"
    price = scraping_price(ticker)
    if price > thresholdPrice:
        text = f"{ticker} is {price}"
        send_message(text)
    else:
        logging_log("it is not over but working now")
    

def do_work():
    schedule.every().day.at("17:30").do(job)
    schedule.every().day.at("8:30").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def test_app():
    print("testing")
    send_message("@@Message Test!! ")


def main():

    stockAlram=threading.Thread(target=do_work,daemon=True,)
    test_trd=threading.Thread(target=test_app,daemon=True,)
    image = Image.open("paw.png")
    menu = (item('Start', lambda : stockAlram.start()),
    # item('Stop Working', lambda : x=True, stop_threads ),
    item('Message Test', lambda : test_trd.start()), 
    item('Stop', lambda : icon.stop()))
    icon = pystray.Icon("What", image, "Cat", menu)
    icon.run()




if __name__ == '__main__':
    try:
        main()
    finally:
        print("error")