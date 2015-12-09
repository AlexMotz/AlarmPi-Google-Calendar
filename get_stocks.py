#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import decimal
import ConfigParser
import better_spoken_numbers as bsn
from pprint import pprint
from math import floor

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

tickers=Config.get('stocks','tickers').split(',')

stocks='Stock update: '
stocks_display='markets: '

for ticker in tickers:
  try: 
    api = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%27'+ticker+'%27)%20&format=json&env=store://datatables.org/alltableswithkeys', timeout=4)
    response = api.read()
    response_dictionary = json.loads(response)

    #print response_dictionary
    stock_name = response_dictionary['query']['results']['quote']['Name'].replace("Common Stock", '').replace(' Inc','').replace(',','').replace('.','').replace('(NS) O','')
    symbol = response_dictionary['query']['results']['quote']['symbol']
    
    # get the price
    stock_price = response_dictionary['query']['results']['quote']['LastTradePriceOnly']
    # trim it to something sane
    stock_price = round(decimal.Decimal(stock_price),2)

    #find the change
    stock_change = response_dictionary['query']['results']['quote']['Change']
    # trim it to something sane
    stock_change = round(decimal.Decimal(stock_change),2)
    stock_change = str(stock_change)
    stock_change = stock_change.replace("-",'▼').replace("+",'▲').strip()
#    print stock_change


    #other stuff in case I ever want it
    stock_high = response_dictionary['query']['results']['quote']['DaysHigh']
    stock_high = round(decimal.Decimal(stock_high),2)
    stock_low = response_dictionary['query']['results']['quote']['DaysLow']
    stock_low = round(decimal.Decimal(stock_low),2)
    market_cap = response_dictionary['query']['results']['quote']['MarketCapitalization']

    whole_price = floor(stock_price)
    decimal_price = floor((stock_price - whole_price)*100)
    stock_price_spoken = bsn.n2w(int(whole_price)) + ' dollars'
    if decimal_price > 0:
      stock_price_spoken += ' and ' + bsn.n2w(int(decimal_price)) + ' cents'
    
    stocks += stock_name + ' is trading at ' + stock_price_spoken + '.  '
    stocks_display += str(symbol) + ' ' + str(stock_price) + str(stock_change) + ', '


  except Exception:
    stocks = 'Failed to connect to Yahoo Finance.  '

if Config.get('main','debug') == str(1):
  print stocks
  print stocks_display

