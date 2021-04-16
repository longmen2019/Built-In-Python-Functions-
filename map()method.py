# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:03:35 2021

@author: User
"""

def quartic(n):
    return n*n*n*n

num_list = [4,5,6,7]
result = map(quartic, num_list)

print('Mapped result is: ', list(result))