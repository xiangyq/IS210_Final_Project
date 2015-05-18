#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sell stocks module"""

import csv

INPUT_FILE = open("mystock.csv", "r")
MYSTOCK = csv.reader(INPUT_FILE)
MYSTOCKS = []
for row in MYSTOCK:
    MYSTOCKS.append(row)
SYMBOL = raw_input('What is the symbol of stock you sold?').upper()
PRICE = raw_input('What was the price when you bougth?')
DATE = raw_input('When did you buy the stock? Follow the example: 20140214\n')
VOLUME1 = int(raw_input('How much was the volume before selling?'))
VOLUME2 = int(raw_input('How much of volume did you sell this time?'))
MYSTOCK = [SYMBOL, PRICE, DATE, str(VOLUME1), str(VOLUME2)]
print 'Check the information you put in:\n{}'.format(MYSTOCK)
ANSWER = raw_input('Are they correct: Yes or No?')
if ANSWER[:1].upper() == 'Y':
    MYOLDSTOCK = [SYMBOL, PRICE, DATE, str(VOLUME1)]
    if VOLUME1 == VOLUME2:
        MYSTOCKS.remove(MYOLDSTOCK)
    else:
        MYSTOCKS.remove(MYOLDSTOCK)
        MYSTOCK_NOW = [SYMBOL, PRICE, DATE, str(VOLUME1 - VOLUME2)]
        MYSTOCKS.append(MYSTOCK_NOW)
    print 'Your stocks information updated, and check mystock.csv for details!'
else:
    print 'Please try again!'
INPUT_FILE.close()
OUTPUT_FILE = open('mystock.csv', 'w')
OUTPUT = csv.writer(OUTPUT_FILE)
OUTPUT.writerows(MYSTOCKS)
OUTPUT_FILE.close()
