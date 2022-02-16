import requests
from bs4 import BeautifulSoup
import re


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

    try:
        floatPostPrice= remove_everything_exceptNumberAndDot(PostPrice.text)
        return floatPostPrice
    except:
        print("don't have CurrentPrice")


    try:
        floatCurrentPrice= remove_everything_exceptNumberAndDot(currentPrice.text)
        return floatCurrentPrice
    except:
        print("don't have PostPrice")
        