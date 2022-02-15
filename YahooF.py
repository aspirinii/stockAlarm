from selenium import webdriver
from bs4 import BeautifulSoup

import yfinance as yf


msft = yf.Ticker("MSFT")

# get stock info
msft.info