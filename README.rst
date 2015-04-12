==========================
 All-in-one stock account
==========================
Most people have more than one account for stock trading, such as individual account, retirement account. Retirement account has different types, such as Traditional RIA, Roth RIA, 403b, 401k, etc. For different reasons, people may also have different accounts at different brokers. So, self-managment of stock tading accounts could be a big challenge. In addition, stock imformation at most brokers are delayed. For example, stock information at Fidelity personal account is delayed for around 20mins. When people want to trade their stocks based on yield or overall return, they will have to calculate the numbers one by one on real time. This time issue adds more challenge on efficiently managing accounts. This project is trying to develop a software which can build an all-in-one account and update information once trade happens and even calculate yield and overall return on real-time.

Personas
=========

Fiona
--------------
Fiona is a 38 years old scientist. She has been working for more than 10 years and already saved some money for her retirement. She has  a few different retirement accounts at different brokers. She believes people can manage their own retirement accounts and people should take their own responsibility for their own future. However, she is quite busy everyday, and need to spend a lot of time on research. So, how to efficiently manage her own retirement accounts is always a big challenge for her.

May
--------------
May is Fiona's young friend, a college student, BS Major in computer science. Although May just started to learn Python programming language, she wants to help her friend and meanwhile gain some first hand experience on project. Fiona and May decide to work together and find a way to improve the management of multiple retirement accounts.


Problem Scenarios
===================
Fiona worked for a few different employers during the past 10 years and then has two different retirement accounts, 401K at Fidelity and 403b at Vanguard. She believe diversity is very important and so she keeps both of them and doesn't want to roll over one into another.In addition, she opened a Roth RIA account at Fidelity. Since she is a big saver, she also opened an individual account at E*TRADE. 

Recently she felt it was overwhelmed. Everytime when she wants to check her stocks, she has to open her accounts one by one. And she loves to check the yield and overall return of her stocks and then decide what to do next. For all of her accounts, there are information regarding to yield and overall return for every stock. However, the information is time-delayed. Like Fidelity, it is 20 minutes delayed. So, she has to calculate the numbers one by one if she need to evaluate her stocks carefully. It is too much work to do. 

For Fiona, she really need a tool, which enable to check her stocks without openning her accounts and update stock information after trade happenes. This tool will be more useful if she can use it to calcualte yield and overall return on real time. 

User Stories
============
As a student, it is a huge task for May to solve Fiona's problems all at once. 
So May came up a strategy to divide the whole project into four parts:

    Part1: Fiona should be able to create the dataset of all of her stocks and information should include: the name
    of stock, the volume of stock, purchase date, purchase price, the name of broker.
    
    Part2: Fiona should be able to create the dataset of the real-time prices of her stocks.
    
    Part3: together with Part 1 and Part 2, Fiona can calcualte real-time yield and overall return for all the stocks or
    one stock.
    
    Part4: All stocks information with yeild and overall return can be saved in CSV file so Fiona can do further
    analysis. 
    
As long as May can successfully finish one part, she could make Fiona's life a bit easier. And if May could finish the whole project at the end, more people like Fiona will benefit from this project.