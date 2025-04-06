#!/usr/bin/env python3
import os
import sys
import time
#os.system("pip install requests")
import requests
from bs4 import BeautifulSoup

def parcing(ticker, field):
    url = f"https://finance.yahoo.com/quote/{ticker.upper()}/financials/?p={ticker.lower()}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    if page.status_code != 200:
        raise Exception(f"Сервис недоступен, ошибка {page.status_code}")
    soup = BeautifulSoup(page.text, "html.parser")
    if soup.title.string == "Symbol Lookup from Yahoo Finance":
        raise Exception("Неправильный тикер")
    temp = soup.findAll(attrs = {"class":"column sticky yf-t22klz"})
    breakdowns = [i.get_text().strip() for i in temp]
    temp = soup.findAll(attrs = {"class":"row lv-0 yf-t22klz"})
    lines = [i.get_text().strip() for i in temp]
    if not(field in breakdowns):
        raise Exception("Неправильное поле таблицы")
    res = lines[breakdowns.index(field)]
    return tuple(res.split())


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ticker = sys.argv[1]
        field = sys.argv[2]
        print(parcing(ticker, field))