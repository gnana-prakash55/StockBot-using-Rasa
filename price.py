#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:58:25 2020

@author: sanjay
"""
import requests
from bs4 import BeautifulSoup
#_____Scraping Stock Price from Yahoofinance
def give_stockprice(stock):
    url='https://in.finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    company=soup.find('h1',{'class':'D(ib) Fz(16px) Lh(18px)'}).get_text()
    company=company.split()
    company=company[2:]
    company=" ".join([str(elem) for elem in company])
    print(company)
    print(str(company[2:]))
    price=soup.find('span',{'class':'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}).get_text()
    find_market_currency=soup.find('div',{'class':'C($tertiaryColor) Fz(12px)'}).get_text()
    print(find_market_currency)
    find_market_currency=find_market_currency.split()
    currency=find_market_currency[-1]
    market=find_market_currency[0]
    stock_price=price+' '+currency
    print(stock_price,market)
    return stock_price,market,company
#give_stockprice(('FB'))