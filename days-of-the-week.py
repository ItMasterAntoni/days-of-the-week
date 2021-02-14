#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#RSA in Python by Antoni Szymanski 2021
#License: Freeware
#**************************************

def leap_years(rok):
    if ((rok % 4 == 0) and (rok % 100 != 0)) or (rok % 400 == 0) and (rok % 4000 == 0):
        return True
    else:
        return False

def day_of_the_week(day,month,year):
    months = {1 : 31,
               2 : 28,
               3 : 31,
               4 : 30,
               5 : 31,
               6 : 30,
               7 : 31,
               8 : 31,
               9 : 30,
               10 : 31,
               11 : 30,
               12 : 31}
    R = year
    if R == 0:
        R = 1
    YY = (R - 1) % 100
    C = (R - 1) - YY
    G = YY + YY // 4
    january1 = (((((C // 100) % 4) * 5) + G) % 7)
    M = month
    D = day
    if M < 1 or M > 12:
        if M < 1:
            M = 1
        else:
            M = 12
    if D > months[M] or D < 1:
        if D > months[M]:
            D = months[M]
        else:
            D = 1
    days_of_the_year = {1 : 0,
                2 : 31,
                3 : 59,
                4 : 90,
                5 : 120,
                6 : 151,
                7 : 181,
                8 : 212,
                9 : 243,
                10 : 273,
                11 : 304,
                12 : 334}
    day_of_the_year = days_of_the_year[M] + D
    czyprzestepny = leap_years(R)
    if czyprzestepny == True and month > 2:
        day_of_the_year = day_of_the_year + 1
    day_of_the_week = (january1 + day_of_the_year - 1) % 7
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    print(str(M)+'/'+str(D)+'/'+str(R)+' is '+days_of_the_week[day_of_the_week])

def main():
    print('Days of the week by Antoni Szymanski 2021')
    print('License: Freeware')
    print('**************************************')
    day = int(input('Enter the day '))
    month = int(input('Enter the month '))
    year = int(input('Enter the year '))
    print('Date:',str(month)+'/'+str(day)+'/'+str(year))
    day_of_the_week(day,month,year)
    print('\n**************************************')
    print('Thanks for using my script')
    print('The next ones are coming soon')

main()

