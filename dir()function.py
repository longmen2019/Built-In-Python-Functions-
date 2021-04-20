# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:27:21 2021

@author: User
"""

#dir is powerful python built-in function, that returns a valid list of all the attributes 
#of the specified object. It returns all the properties, even built-in properties that are the 
#default for all objects. 
class Student:
    name = "Joy",
    age = 16 , 
    rollNo = 25 , 
    
print(dir(Student))