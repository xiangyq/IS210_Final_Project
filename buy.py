#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Buy stocks module"""

import csv

STOCK_NAME = raw_input('What is the stock symbol you bought?').upper()
QUANTITY = int(raw_input('How much volume did you buy?'))
COST_PRICE = raw_input('What was the price?')
SDATE = raw_input('What date did you buy(please follow example: 20150612)?')
STOCK_INFOR = [STOCK_NAME, COST_PRICE, SDATE, str(QUANTITY)]
print 'this is your stock information:\n {}'.format(STOCK_INFOR)
ANSWER = raw_input('Confirmed: Yes or No?')
if ANSWER[:1].upper() == 'Y':
    OUTPUT_FILE = open('mystock.csv', 'a')
    OUTPUT = csv.writer(OUTPUT_FILE)
    OUTPUT.writerow([STOCK_NAME, COST_PRICE, SDATE, QUANTITY])
    OUTPUT_FILE.close()
    MESSAGE = 'Your stock was updated, and check mystock.csv for details!'
    print MESSAGE
else:
    print 'Try again!'
