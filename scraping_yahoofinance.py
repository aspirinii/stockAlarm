import requests
from bs4 import BeautifulSoup
import re
from log_log import logging_log


def remove_everything_exceptNumberAndDot(a): 
    b = re.sub("[^\d\.]", "", a)
    c =  float(b)
    return c


def scraping_price(ticker):
    # ticker = 'GOOGL'

    # url = 'https://finance.yahoo.com/quote/GOOGL?p=GOOGL'
    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'

    headers = {
        'User-agent': 'Mozilla/5.0',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    currentPrice = soup.find(
        'fin-streamer', {'data-symbol' : ticker, 'data-field' : 'regularMarketPrice'})

    PostPrice = soup.find(
        'fin-streamer', {'data-symbol' : ticker, 'data-field' : 'postMarketPrice'})
    
    PrePrice = soup.find(
    'fin-streamer', {'data-symbol' : ticker, 'data-field' : 'preMarketPrice'})

    try:
        floatPostPrice= remove_everything_exceptNumberAndDot(PostPrice.text)
        logging_log("Got Post Price")
        return floatPostPrice
    except:
        logging_log("don't have PostPrice")
        
    try:
        floatPrePrice= remove_everything_exceptNumberAndDot(PrePrice.text)
        logging_log("Got Pre Price")
        return floatPrePrice
    except:
        logging_log("don't have PrePrice")

    try:
        floatCurrentPrice= remove_everything_exceptNumberAndDot(currentPrice.text)
        logging_log("Got current Price")
        return floatCurrentPrice
    except:
        logging_log("don't have CurrentPrice")
        