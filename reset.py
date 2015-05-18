#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A test module"""

import csv

MYSTOCKS = [['stock symbol', 'purchase price', 'purchase date', 'volume']]
OUTPUT_FILE1 = open('mystock.csv', 'w')
OUTPUT1 = csv.writer(OUTPUT_FILE1)
OUTPUT1.writerows(MYSTOCKS)
OUTPUT_FILE1.close()

MYRESULT = [['stock symbol', 'purchase price', 'purchase date',
             'volume', 'return', 'yield']]
OUTPUT_FILE2 = open('myresult.csv', 'w')
OUTPUT2 = csv.writer(OUTPUT_FILE2)
OUTPUT2.writerows(MYRESULT)
OUTPUT_FILE2.close()

print "Everything reset!"
