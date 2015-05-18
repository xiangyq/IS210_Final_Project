#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate stock return and yield module"""

import datetime
import csv


def calculate(stocks, stock_market_price):
    """Do some math and return stocks information
       including return and yield.

    Args:
       stocks(list): a list with lists nested.
       stock_market_price(dict): a dictionary with stock symbol as key and
       stock price as value.

    Returns:
        create a myresult.csv file with all the information;
        print out message: 'Check the result in myresult.csv!'

    Examples:

        stocks = [
        ['stock symbol', 'purchase price', 'purchase date', 'volume'],
        ['C', '56', '20120324', '25'],
        ['C', '53.12', '20140325', '100'],
        ['JPM', '45.3', '20130427', '100'],
        ['APPL', '103.23', '20150125', '20']
        ]
        stock_market_price = {'C': 67.0, 'APPL': 103.0, 'JPM': 87.0}
        >>> calculate(stocks, stock_market_price)
        Check the result in myresult.csv!
    """
    result = [['stock symbol', 'purchase price', 'purchase date',
               'volume', 'total return', 'annual yield']]
    counter = 1
    while counter < len(stocks):
        sym = stocks[counter][0]
        pdate = stocks[counter][2]
        vol = stocks[counter][3]
        price1 = stocks[counter][1]
        price2 = stock_market_price[sym]
        myreturn = (float(price2) - float(price1)) * int(stocks[counter][3])
        myreturn = round(myreturn, 1)
        c_date = datetime.date.today()
        p_date = datetime.datetime.strptime(pdate, '%Y%m%d').date()
        h_days = (c_date - p_date).days
        myinvest = round(float(stocks[counter][1]) * int(stocks[counter][3]), 1)
        myyield = round((myreturn / myinvest) * 365 / h_days * 100, 2)
        newinfor = [sym, price1, pdate, vol, '${}'.format(myreturn),
                    '{}%'.format(myyield)]
        result.append(newinfor)
        counter += 1
    output_file = open('myresult.csv', 'w')
    output = csv.writer(output_file)
    output.writerows(result)
    output_file.close()
    print 'Check the result in myresult.csv!'

INPUT_FILE = open('mystock.csv', 'r')
MYSTOCKS = csv.reader(INPUT_FILE)
STOCK_SYMBOL_LIST = []
STOCKS = []
for row in MYSTOCKS:
    STOCKS.append(row)
    if row[0] != 'stock symbol'and row[0] not in STOCK_SYMBOL_LIST:
        STOCK_SYMBOL_LIST.append(row[0])
INPUT_FILE.close()

STOCK_MARKET_PRICE = {}
for STOCK in STOCK_SYMBOL_LIST:
    STOCK_PRICE = float(raw_input('What is the price of {} now?'.format(STOCK)))
    STOCK_INFOR = {STOCK: STOCK_PRICE}
    STOCK_MARKET_PRICE.update(STOCK_INFOR)

print STOCK_MARKET_PRICE

ANSWER = raw_input('Check the prices: are they correct, yes or no?')
if ANSWER[:1].upper() == 'Y':
    calculate(STOCKS, STOCK_MARKET_PRICE)
else:
    print "Try again!"
