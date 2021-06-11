# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:27:21 2021

@author: User
"""

"""dir is powerful python built-in function, that returns a valid list of all the attributes 
of the specified object. It returns all the properties, even built-in properties that are the 
default for all objects. """
class Student:
    name = "Joy",
    age = 16 , 
    rollNo = 25 , 
    
print(dir(Student)) 
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'rollNo']
