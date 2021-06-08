# -*- coding: utf-8 -*-
"""
Reference : https://docs.python.org/3/tutorial/controlflow.html#if-statements
Created on Mon May 31 23:13:00 2021

@author: men_l
"""
"""if statement """
x = int (input("Please enter an integer: "))
# Please enter an integer : 42
if x < 0:
    x = 0
    print("Negative changed to zero")
# There can be zero or more elif parts, and the else part is optional
# The keyword "elif" is short for "else if"
# If...elif...elif squence is a substitute for the switch or case statements found in other languages
elif x == 0:
    print("Zero")
elif x == 1:
    print('Single')
else:
    print ("More")

"""Measure some strings:"""
words = ["Cat" , "Window" , "Defenstrate"]
#Python's for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
for w in words:
    print(w, len(w))

"""Strategy : Iterate over a copy"""
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
"""Strategy: Create a new collection"""
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status


"""The range () function
The given end point is never part of the generated sequence"""
for i in range (5):
    print(i)

for i in range (5,10):
    print(i)

for i in range (0,10,3):
    print(i)
    
for i in range (-10, -100, -30):
    print(i)

"""To iterage over the indices of a sequence, you can combine range () and len() as follows:"""
a = ['Mary' , 'had' , 'a' , 'little' , 'lamb']
for i in range (len(a)):
    print(i, a [i])

"""we say such an object is iterable, that is, suitable as a target for functions and constructs that expect
something from which they can obtain successive items until the supply is exhausted. We have seen that the 
for statement is such a construct, while an example of a function that takes an iterable is sum():"""

  
print(sum (range(4))) #1+2+3  

"""How to get a list from a range"""
print(list (range (4)))

""" The break statement, like in C, break out of the innermost enclosing for or while loop
loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable
 (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
  This is an exemplified by the following loop, which searches for prime numbers:"""
    
for n in range (2,10):
    for i in range (2,n):
        if n % i == 0:
            print (n , 'equal' , i , ' *',  n//i)
            break
"""The else clause belongs to the for loop, not the if statement
when used with a loop, the else clause has more in common with the else clause of a try statement than it does with 
does with of if statements: a try statement's else clause runs when no exception occurs, and a loop's else clause
runs when no break occurs. """
        else:
            # loop fell through without finding a factor
            print(n , " is a prime number")


# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range (2,10):
    if num % 2 == 0:
        print ("Found an even number: ", num)
        continue
    print("Found an odd number: ", num)

"""The pass statement does nothing. It can be used when a statement is required syntactically 
but the program requires no action."""

while True:
    # Busy-wait for keyboard interrup (Ctrl + C)
    pass

# This is commonly used for creating minimal classes:
class MyEmptyClass:
    pass

"""Another place pass can be used is as a place-holder for a function or conditional body when you are
working on new code, allowing you to keep thinking at a more abstract level. This pass is silently ingored:"""

def initlog (*args):
# Remember to implement this!    
    pass 

"""Defining Functions 
We create a function that writes the Fibonacci series to an arbitrary boundary"""

"""The keyword def introduces a function definition. It must be followed by the function name 
and the parenthesized list of formal parameters.
The statements that form the body of the function start at the next line, and must be indented"""
def fib(n):
"""the first statement of the function body can optionally be a string literal; this string is the function's documentation string, or docstring."""
    """ Print a Fibonacci series up to n."""
"""The execution of the function introduces a new symbol table used for the local variables of the function.
More precisely, all variable assignments in a function store the value in the local symbol table; whereas
variable references first look in the local symbol table, then in the local symbol tables of enclosing 
functions, then in the global symbol table, and finally in the table of built-in name.
Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function
(unless, for global variables, named in a global statement, or , for variales of enclosing functions, named
in a nonlocal statement), although they may be refernced """
    a, b = 0,1
    while a < n:
        print (a, end =  ' ')
        a, b = b , a + b
    print()
    #Now call the function we just defined:
print(fib (2000))

"""a function definition associates the function name with the function object in the current symbol table.
The interpreter recognizes the object pointed to by that name as a user-defined function. Other names
can also point to that same function object and can also be used to access the function"""
f = fib
f(100)

"""Even functions without a return statement do return a value, albeit a rather boring one
This value is called None (it's built-in name).
Writing the value None is normally suppressed by the interpreter if it would be only value  written.
You can see it if you really want to using print():"""
fib(0)
print(fib(0))

"""It's simple to write a function that returns a list of the numbers of the Fibonacci series, instead of print it
Return Fibonacci series up to n."""
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0,1
    while a < n:
        result.append(a)
        #see below
        a, b = b, a+b
    return result
f100 = fib2(100)
print(f100)


"""coming from other languages, you might think that fib is not a function but a procedure since it 
does not return a value. in fact, even functions without a return statement do return a value, albeit a rather 
boring one. Thsi value is called None (it's a built-in name'). Writing the value None is normally suppressed
by the interpreter if it would be only value written."""

fib(0)
print(fib(0))


"""It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
return Fibonacci series up to n"""
def fib2(n):
    """ Return a list containing the Fibonacci series up to n."""
    # The return statement returns with a value from a function. return without an expression argument
    # returns None. Falling off the end of a function also returns None.
    
    result = []
    a, b = 0,1
    while a < n:
        # The statement return.append(a)  calls a method of the list object result. A method is function
        # that 'belongs' to an object and is named obj.methodname, where obj is some object (this may be an expression),
        # and methodname is the name of a method that is defined by the object's type.
        result.append(a)
        a , b = b , a +b
    return result
f100 = fib2(100)
print(f100)

""" Default Argument Values"""
""" 
The most useful form is to specify a default value for one or more argumentss
This create a function that can be called with fewer arguments than it is 
defined to allow
"""

"""
This example also introduces the in keyword. This tests whether or not a sequence contains a certain value
"""
def ask_ok(prompt, retries = 4, reminder = "Please try again!"):
    while True:
        ok = input (prompt)
        if ok in ('y' , 'ye' , 'yes'):
            return True
        if ok in ('n' , 'no' , 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise  ValueError ('invalid user reponse')
        print (reminder)

"""
This function can be called in several ways:
    1. giving only the mandatory arguments:
        ask_ok("Do you really want to quit?")
"""
ask_ok("Do you really want to quit?")

"""
Giving one of the optional arguments : ask_ok ('Ok to overwrite the file?', 2)
"""

ask_ok('Ok to overwrite the file?' , 2)

"""
or even giving all arguments : ask_ok("OK to overwrite the file?" , 2 , "Come on, only yes or no!")
"""

ask_ok("OK to overwrite the file?" , 2 , "Come on, only yes or no!")

"""
The default values are evaluated at the point of function definition in the defining scope, so that
"""
i = 5
def f(arg=i):
    print(arg)
i = 6
f() # Will print 5

"""
Important Warning:
    The default value is evaluated only once. This makes a difference when the default
    is a mutable object as list, dictionary, or instances of most classes. For example,
    the following function accumulates the arguments passed to it on subsequent calls
"""

def f(a , L = []):
    L.append(a)
    return L
print (f(1)) #This will print [1]
print(f(2)) #This will print [1, 2]
print(f(3)) #This will print [1, 2, 3]

"""
If you don't want the default to be shared between subsequent calls, you can
write the function like this instead:
"""

def f(a , L = None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1)) # This will print [1]
print(f(2)) # This will print [2]
print(f(3)) # This will print [3]

""" 4.7.2 Keyword Arguments """
""" 
Functions can also be called using keywords arguments of the form kwarg = value.
For instance, the following function:
"""

def parrot (voltage , state = 'a stiff' , action = 'voom' , type = 'Norwegian Blue'):
    print("--This parrot wouldn't", action , end = ' '  )
    print("if you put" , voltage , "volts through it. ")
    print("-- Lovely plumage, the", type)
    print("-- It's" , state, "!")
"""
accepts one required argument (voltage) and three optional arguments (state, action, and type).
This function can be called in any of the following ways:
"""

parrot(1000) # 1 positional argument

parrot(voltage = 1000) #1 keyword argument

parrot(voltage = 1000000 , action = "VOOOOOM") #2 keyword argument

parrot(action = 'VOOOOOM' , voltage = 1000000) #2 keyword argument

parrot('a million' , 'bereft of life' , 'jump') #3 positional argument

parrot('a thousand' , state = 'pushing up the daisies') #1 positional, 1 keyword

""" but all the following calls would be invalid:"""
parrot() #required argument missing
parrot(voltage = 5.0 , 'dead') #non-keyword argument after a keyword argument
parrot(110, voltage =220) #duplicate value for the same argument
parrot(actor = "John Cleese") #unknown keyword argument

"""
# In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must
# match one of the arguments accepted by the function (e.g., actor is not a valid argument for the parrot function),
# and their order is not important. This also includes non-optional arguments (e.g., parrot (voltage=1000) is valid too).
# No argument may receive a value more than once. Here is an example that fails to this restriction:

"""

def function(a):
    pass
function (0 , a =0)



"""
When a final formal parameter of the form **name is present, it receives a dictionary 
containing all keyword arguments except for those corresponding to a formal parameter. 
This may be combined with a formal parameters of the form *name (described in the text subsection) 
which receives a tuple containing the positional arguments beyond the formal parameters list.
(*name must occur before **name.) For example, if we define a function like this:
"""

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any " , kind, "?")
    print("--I'm sorry, we're all out of" , kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw, ":" , keywords[kw])
"""It could be called like this: """
cheeseshop("Limburger" , "It's very runny, sir",
            "It's really very, VERY runny, sir",
            shopkeeper = "Michael Palin",
            client = "John Cleese",
            sketch = "Cheese Shop Sketch")

"""4.7.3.4. Function Examples"""

""" Consider the following example function definitions paying close attention to the markers / and *"""
def standard_arg (arg):
    print(arg)
def pos_only_arg(arg , /):
    print(arg)
def kwd_only(*, arg):
    print(arg)
def combined_example(pos_only, / , standard , * , kwd_only):
    print(pos_only, standard, kwd_only)

"""The first function definition, standard_arg, the most familiar form, places no restriction on 
the calling convention and arguments may be passed by position or keyword:"""

standard_arg(2)

standard_arg(arg=2)

""" 
The second function pos_only_arg is restricted to only use positonal parameters as there is a / in 
the function definition:
"""

pos_only_arg(1)

# pos_only_arg(arg=1) # This will print " TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'"

"""The third function kwd_only_args only allows keyword arguments as indicated by a * in teh function definition:"""
# kwd_only_arg(3) #   pos_only_arg(arg=1) # This will print " TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'"

#TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

"""
And the last uses all three calling conventions in the same function definition:
"""

combined_example(1,2,3)

"""File "C:\Users\men_l\Documents\Python Scripts\More_Control_Over_Flow_Tools.py", line 367, in <module>
    pos_only_arg(arg=1) # This will print " TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'"

TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
"""

combined_example(1,2,kwd_only =3) # this print "1 2 3"

combined_example(1, standard = 2 , kwd_only = 3) # this print "1 2 3"

combined_example(pos_only=1, standard =2 , kwd_only = 3)

  File "C:\Users\men_l\Documents\Python Scripts\More_Control_Over_Flow_Tools.py", line 390, in <module>
    combined_example(pos_only=1, standard =2 , kwd_only = 3)

TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

"""
Finally, consider this function definition which has a pontential collision between the positional argument
name and **kwds which has name as a key:
"""

def foo (name, **kwds):
    return 'name' in kwds

"""
There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter.
For example:
"""

foo(1, **{'name' : 2})

Traceback (most recent call last):

  File "C:\Users\men_l\Documents\Python Scripts\More_Control_Over_Flow_Tools.py", line 410, in <module>
    foo(1, **{'name' : 2})

TypeError: foo() got multiple values for argument 'name'

"""
But using / (positonal only arguments), it is possible since it allows name as a positoinal argument and 
'name' as a key in the keyword arguments:
"""

def foo (name,/, **kwds):
    return 'name' in kwds

print(foo(1, **{'name': 2})) #This print "True"

"""In other words, the names of positional-only parameters can be used in **kwds without ambiguity"""

""" 4.7.4 Arbitrary Argument Lists"""
"""
Finally, the least frequently used option is to specify that a function can be called with an arbitrary number
of arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more 
normal arguments may occur.
"""

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth" , "mars" , "venus")) #earth/mars/venus

print(concat("earth" , "mars" , "venus" , sep="."))

"""4.7.5. Unpacking Argument Lists"""
"""
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a 
function call requiring separate positoinal arguments. 
For instance, the built-in range() function expects separate start and stop arguments. If they are not available
separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:
"""
print(list (range(3,6))) #normal call with separate argument: [3, 4, 5]

args = [3,6]
print(list(range(*args))) #call with arguments unpacked from a lit : [3, 4, 5]

"""In the same fashion, dictionaries can deliver keyword arguments with the **-operator"""
def parrot (voltage, state = 'a stiff' , action = 'voom'):
    print("--This parrot wouldn't" , action, end = ' ')
    print("if you put" , voltage, "volts through it." , end= ' ')
    print("E's" , state, "!")
d = {"voltage" : "four million" , "state": "bleedin' demised" , "action": "VOOM"}
parrot(**d)

"""4.7.6 Lambda Expressions
Small anonymous function can be created with the lambda keyword. This function returns the sum of its two arguments:
labda a,b: a + b. Labda functions can be used wherever function objects are required. They are syntactically restricted to a single expression.
Sematically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables 
from the containing scope:
"""
def make_incrementor(n):
    return lambda x: x + n 
f = make_incrementor (42)
print(f(0)) #42
print(f(1)) #43

"""The above example uses a lambda expression to return a function.
 Another use is to pass a small function as an argument"""

pairs = [(1, 'one') , (2, 'two') , (3, 'three') , (4, 'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs) # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
