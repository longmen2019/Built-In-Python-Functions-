# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:56:33 2021

@author: User
"""

#Split () method returns a list of the string after splitting the given string by 
#the specified separator. 

txt1 = "apple#banana#cherry#orange"
txt2 = "Hello how are you"

result1 = txt1.split("#")
result2 = txt2.split(" ")

print(result1) #['apple', 'banana', 'cherry', 'orange']
print(result2) #['Hello', 'how', 'are', 'you']
