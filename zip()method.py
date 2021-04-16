# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:26:11 2021

@author: User
"""

number = [4,5,6,7,8]
letters = ['four' , 'five' , 'six' , 'seven' , 'eight']

result = zip(number, letters)

#converting values to print as set 
result = set(result)
print('The zipped result is: ' , result)