==========================
 All-in-one stock account
==========================
People could have more than one account for stock trading, such as individual account, retirement account. Retirement account has a several different types, such as Traditional RIA, Roth RIA, 403b, 401k, etc. For different reasons, people may also have different accounts at different brokers. So, self-managment of stock tading accounts could be a big challenge. In addition, stock imformation at most brokers are delayed. For example, stock information at Fidelity personal account is delayed for around 20mins. When people want to trade their stocks based on yield or overall return, they will have to calculate the numbers one by one on real time. This time issue adds more challenge on efficiently managing accounts. This project is trying to develop a software which can build an all-in-one account and update information once trade happens and even calculate yield and overall return on real-time.

Personas
=========

Fiona
--------------
Fiona is a scientist and has been working for more than 10 years. She has  one retirement account at Fidelity and another one at Vanguard. Since she is a big saver, she also has an individual account at E*TRADE. She believes people can manage their own retirement accounts and people should take their own responsibility for their own future. However, she is quite busy everyday, and need to spend a lot of time on research. So, how to efficiently manage her own retirement accounts is always a big challenge for her.

Problem Scenarios
===================

When time goes, Fiona's accounts are becoming bigger and bigger. Recently she felt it was overwhelmed to manage her accounts.

Current Alternatives
----------------------------------------
She opens her accounts one by one whenever she wants to check them. And she calculates the yield and overall return by herself in order to get real-time information. 

Value Proposition
--------------------------------------
The purpose of building a software is to help Fiona to quickly update her accounts and calculate the yield and overall return for her. By using this software, she will be able to check all of her accounts with much less time and get the yield and overall return with no manual calculation.

User Stories
============

For Fiona, she really need a tool, which enable to check her stocks without openning her accounts and update stock information after trade happenes. This tool will be perferct for her if she can use it to calcualte yield and overall return on real time. With this tool, she will be able to manage her accounts easliy and efficiently. 

Acceptance Stories
==================

Scenario 1: Inputting stock information
--------------------------------------------------------------------
::

    Given that I buy a new stock
    And I would like to update it into a program
    When I click the Buy button
    Then I will be taken to a screen to input stock information by filling in symbol,
    the number of volume, the price, the date
    And screen shows the output of stock information

Scenario 2: Deleting a stock
-----------------------------------------------
::

    Given that I sell a stock
    And I would like to delete it from a program
    When I click sell buttion
    Then I will be taken to a screen to input stock information by filling in symbol
    And screen shows the output of left stocks information

Scenario 3: Calculating yield and overall return of stocks
-----------------------------------------------------------------------------------------------
::

    Given that I have the current prices of my stocks
    And I would like to calculate yield and overall return of my stocks
    When I click the calculate button
    Then I will be taken to a screen to input the prices
    And screen shows the output of stocks information with symbol, yield, overall return