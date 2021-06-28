# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:58:03 2021

# @author: men_l
# """

"""Reference: https://docs.python.org/3/tutorial/datastructures.html"""

"""5.1. More on Lists"""

"""count(x)
return the number of times x appears in the list"""


fruits = ['orange' , 'apple' , 'pear' , 'banana' , 'kiwi' , 'apple' , 'banana']
print(fruits.count('apple'))
# output: 2

print(fruits.count('tangerine'))
# output: 0

"""
index(x[, start[,end]])
Return zero-based  index in the list of the first item whose value is equal to x. Raise
a ValueError if there is no such item.
"""
print(fruits.index('banana'))
# output: 3

print(fruits.index('banana' , 4)) #Find next banana starting a position 4
# output: 6

"""
reverse ()
Reverse the elements of the list in place.
"""
fruits.reverse()
print(fruits)
# output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

"""
append(x)
Add an item to the end of the list. Equivalent to a [len(a:)] = [x]
"""
fruits.append('grape')
print(fruits)
# output : ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']


"""
sort(*, key=None, reverse = False)
Sort the items of the list in place (the arguments can be used for sort customization)
"""
fruits.sort()
print(fruits)
# output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

"""
pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes
and returns the last item in the list. (The square brackets around the i in the method signature denote that the 
parameter is optional, not that you should type square brackets at that position)
"""
fruits.pop()
print(fruits)

"""5.2 Using Lists as Stacks
The list methods make it very easy to use a list as a stack, where the last element added is the first element 
retrieved ("last-in, first-out"). To add an item to the top of the stack, use append(). To retrieve an item from
the top of the stack, use pop() without an explicit index.
"""

stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
# output: [3, 4, 5, 6, 7]

# stack.pop()
# print(stack)

# stack.pop()
# print(stack)

# stack.pop()
# print(stack)

"""
5.1.2 Using Lists as Queues 
It is also possible to use a list as a queue, where the first element added is the first element retrieved
 ("first-in, first-out"); however, lists are not efficient for this purpose. While appends and pops from the end
 of list are fast, doing inserts or pops from the beginning of a list is slow( because all of the other 
  elements have to be shifted by one)

"""
from collections import deque
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
queue = deque (["Eric" , "John" , "Michael"])
print(queue)
# deque(['Eric', 'John', 'Michael'])
queue.append("Terry")
print(queue)
# deque(['Eric', 'John', 'Michael', 'Terry'])
queue.append("Graham")
print(queue)
# deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print(queue)
# deque(['John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print(queue)
# deque(['Michael', 'Terry', 'Graham'])


"""5.1.3 List Comprehensions
List comprehensions provide a concise  way to create lists. Common applications are to make new lists where each element
is the result of some operations applied to each member of another sequence or iterable, or to create a sequence of those
elements that satisfy a certain condition.
"""

squares = []
for x in range (10):
    squares.append(x**2)
    
print(squares)


"""Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate
the list of squares without any side effects using:"""
squares = list (map(lambda x : x**2, range (10)))
print(squares)

"""or, equivalently"""

squares = [x**2 for x in range (10)]
print(squares)

"""
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or 
if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if
clauses which follow it. For example, this listcomp combines the elements of two lits if they are not equal:
"""

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

"""and it's equivalent to:"""

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
            
combs #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

"""Note how the order of the for and if statements is the same in both snippets
If the expression is a tuple (e.g. the (x,y) in the previous example) ,it must be parenthesized.
"""

vec = [-4,-2,0,2,4]
# create a new list with the value doubled
print([x*2 for x in vec])
# [-8, -4, 0, 4, 8]


# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# [0, 2, 4]

# apply a function to all the elements
print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = [' banana' , ' loganberry' , 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])
#['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
tuple = [(x, x**2) for x in range (6)]
print(tuple)
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3] , [4,5,6] , [7,8,9]]
listcomp = [num for elem in vec for num in elem]
print(listcomp)

"""List Comprehensions can contain complex expression and nested functions"""
from math import pi
string = [str(round(pi, i)) for i in range (1,6)]
print(string)

"""
5.1.4. Nested List Comprehensions
The initial expression in a list comprehension ca be any arbitrary expression, including another list comprehension.
Consider the following example of 3x4 matrix implemented as a list of 3 lists of length 4:
"""

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]
""" The following list comprehension will transpose rows and columns"""
matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
"""As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it, so
this example is equivalent to"""

tranposed = []
for i in range (4):
    tranposed.append([row[i] for row in matrix])
print (tranposed)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

"""which, in turn, is the same as """
tranposed = []
for i in range (4):
    # the following 3 lines implement the nested listcomp
    tranposed_row = []
    for row in matrix:
        tranposed_row.append(row[i])
    tranposed.append(tranposed_row)
print(tranposed)

"""In the real world, you should prefer built-in functions to complex flow statement. The zip() function do a great job
for this use case:"""

zip = list(zip(*matrix))
print(zip)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

"""
5.2. The del Statement  

There is a way to remove an item from a list given its index instead of its value:the del statement. This differs from the 
pop () method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list. For example 
"""

a = [-1,1,66.25,333,1234.5]
del a [0]
print(a)
# [1, 66.25, 333, 1234.5]

del a[2:4]
print (a)
# [1, 66.25]
del a[:]
print(a)
# []

"""del can also be used to delete entire variables"""
del a
# print(a)
# NameError: name 'a' is not defined

"""Referencing the name a hereafter is an error (at least until another value is assigned to it). 
We will find other uses for del later."""

"""
Tuples and Sequence
We saw that lists and strings have many common properties, such as indexing and slicing operations. There are two examples 
of sequnce data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence
data types may be added. There is also another standard sequence data type: the tuple. 
A tuple consists of a number of values separated by commmas, for instance:
"""

t = 12345, 54321 ,'hello!'
print(t[0])
# 12345
print(t)
# (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1,2,3,4,5)
print(u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# tuples are immutable:
# t[0] = 88888

#   File "C:\Users\men_l\Documents\Python Scripts\Data Structures.py", line 282, in <module>
#     t[0] = 88888

# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1,2,3] , [3,2,1])
print(v)
([1, 2, 3], [3, 2, 1])

"""
As you see, on output tuples are always enclosed in paretheses, so that nested tuples are interpreted correctly;
they may be input with or without surrounding parentheses, although often parentheses are necessary anyway 
(if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it
is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similary to lists, they are often used in different situations and for different purposes. Tuples
are immutable, and usually contain a heterogenous sequence of elements that are accessed via unpacking or indexing
(or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogenous and accessed
by iterating over list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accomodate 
these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following
a value with a comma (it is not sufficient to enclose a single value in parenteses). Ugly, but effecitve. For example:
"""

empty = ()
singleton = 'hello', #<-- trailing comma
print(len(empty))
#0
print(len(singleton))
print(singleton)


"""
The statement t = 12345, 54321, "hello!" is an example of tuple packing: the values 12345, 54321, and 'hello!' are packed
together in a tuple. The reverse operation is also possible:
"""
t = 12345, 54321, "hello!" 
x,y,z =t
print(t)
#(12345, 54321, 'hello!')


"""
5.4 Sets

Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses
include membership testing and eliminating duplicate entries. Set object also support mathematical operation like union,
intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set (), not {};
the latter creates an empty dictionary.

Here is a brief demonstration
"""
basket = {'apple' , 'orange' , 'apple' , 'pear' , 'orange' , 'banana'}
print(basket)
# {'orange', 'banana', 'apple', 'pear'}
# show that duplicates has been removed
print('orange' in basket)
#True
print('crabgrass' in basket)
#False

"""Demonstrate that operations on unique letters from two words """
a = set ('abracadabra')
b = set ('alacazam')
print(a)
# {'c', 'r', 'b', 'd', 'a'} 
# unique letters in a
print(b)
# {'l', 'c', 'm', 'a', 'z'}
print(a -b) # letters in a but not in b
# {'r', 'b', 'd'}
print(a|b) #letters in a or b or both
# {'l', 'c', 'm', 'r', 'b', 'd', 'a', 'z'}
print(a&b) #letters in both a and b
# {'a', 'c'}
print(a^b) #letters in a or b but not both
# {'r', 'l', 'b', 'z', 'd', 'm'}

"""Similary to list comprehensions, set comprehensions are also supported"""
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}

"""5.5 Dictionaries
Another useful data type built into Python is the dictionary. Dictionaries are sometimes found in other languages as 
"associative memories" or "associative arrays." Unlike sequences, which are indexed by a range of numbers, dictionaries 
are indexed by keys, which can be any immutable type; strings and number can always be keys. Tuples can be used as keys 
if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly,
it cannot be used as a key. You can't use lists as keys, since lists can be modified in place using index assignments,
silce assignments, or methods like append() and extend(). 
It is best to think of dictionary as a set of key: value pairs, with the requirement that they keys are unique 
(with one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key: value pairs within
the brace adds initial key: value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. it
is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated
with that key is forgotten. It is an error to extract a value using a non-existent key.

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order 
(if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.
Here is a small example using a dictionary:
 """
 
tel = {'jack' : 4098, 'sap' : 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sap': 4139, 'guido': 4127}

print(tel['jack'])
# 4098

del tel['sap']
print(tel)
# {'jack': 4098, 'guido': 4127}

tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

print(list(tel))
# ['jack', 'guido', 'irv']

print(sorted(tel))
# ['guido', 'irv', 'jack']

print('guido' in tel)
# True

print('jack' not in tel)
# False

"""
The dict() constructor builds dictionaries directly from sequences of key-value pairs:
"""

print(dict([('sape', 4139) , ('guido', 4127), ('jack' , 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

"""Looping Techniques
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using
the items() method
"""
knights = {'gallahad': 'the purpose' , 'robin' : 'the brave'}
for k , v in knights.items():
    print(k,v)
# gallahad the purpose
# robin the brave

"""When looping through a sequence, the position index and correponding value can be retrieved at the same time
using the enumerate() function."""

for i, v in enumerate(['tic' , 'tac' , 'toe']):
    print(i,v)

# 0 tic
# 1 tac
# 2 toe
 
"""
To loop over two or more sequences at the same time, the entries can be paired with the zip() function
"""
# questions = ['name' , 'quest' , 'favorite color']
# answers = ['lancelot' , 'the holy grail' , 'blue']
# for q, a in zip (questions, answers):
#     print('What is your {0}? It is {1}.'.format(q,a))
# What is your name? It is lancelot.
# What is your quest? It is the holy grail.
# What is your favorite color? It is blue.

"""
To loop over a sequence in reverse, first specify the sequnce in a forward direction and then call the 
reversed () function
"""

for i in reversed (range (1,10,2)):
    print(i)

"""To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving 
the source unaltered."""

basket = ['apple' , 'orange' , 'apple' , 'pear' , 'orange' , 'banana']
for i in sorted (basket):
    print(i)
    
# apple
# apple
# banana
# orange
# orange
# pear

"""
Using set() on a sequence eliminates duplicate elements. The use of sorted () in combination with set() over a sequence
is an idiomatic way to loop over unique elements of the sequence in sorted order.
"""

basket = ['apple' , 'orange' , 'apple' , 'pear' , 'orange' , 'banana']
for f in sorted (set(basket)):
    print(f)
# apple
# banana
# orange
# pear

""" It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer 
to create a new list instead."""

import math
raw_data = [56.2, float ('NaN') , 51.7 , 55.3 , 52.5 , float('NaN') , 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
# [56.2, 51.7, 55.3, 52.5, 47.8]

"""
5.7. More on Conditions
The conditions used in while and if statements can contain any operators, not just comparisons.

The comparison operators 'in' and 'not in' check whether a value occurs (does not occur) in a sequence. The 
operator 'is' and 'is not' compare whether two objects are really the same object. All comparison operators have 
the same priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, a < b == c tests whether 'a' is less than 'b' and moreover 'b' equals 'c'.
Comparisons may be combined using the Boolean operators 'and ' and 'or', and the outcome of a comparison 
(or of any other Boolean expression) may be negated with 'no'. These have lower priorities than comparison operators;
between them, 'not' has the highest priority and 'or' the lowest, so that 'A' and 'Not B or C' is equivalent to 
'(A and (not B)) or C'. As always, parentheses can be used to express the desired composition. 

The Boolean operatos 'and' and 'or' are so-called short-circuit operators: Their arugments are evaluated from left to 
rifht, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C
does not evaluate the expression C. When used as general value and not as a Boolean, the return value of a short-circuit
operator is the last evaluated argument. 

It is possible to assign the result of a corporation or other Boolean expression to a variable. For example

"""
string1, string2, string3 = '' , 'Trondheim' , 'Hammer Dance'
non_null = string1  or string2 or string3 
print (non_null)
# Trondheim
"""Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus oerator ':='.
This avoids a common class of problem encountered in C programs: trying '=' in an expression when '==' was intended  """

"""
5.8. Comparing Sequences and Other Types
Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering
: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next 
two items are compared, and so on, until either sequence is exhausted. if two items to be compared are themselves sequences
of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the 
sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser)
one. Lexicographical ordering for strings uses the Unicode point number to order individual characters. Some examples of comparisons between
sequences of the same type:
"""

