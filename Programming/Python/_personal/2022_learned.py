


###########################
# How to turn your .py into .exe
###########################

# pip install pyinstaller
# pyinstaller main.py --onefile

# Python major.minor.patch => Python 3.11.2

dir(list)
dir(str)

help(str.capitalize())



"""
######################################
Built in arsenal
######################################
"""
# whitespace counts as a character inside strings
# empty string = False
# for a and b    -> if a is False then b won't be evaluated
# for a or b     -> if a is True then b won't be evaluated
# in = containment test operator
# *arg -> variable argument

None # null
...  # -> means we don't know what to come
pass # empty code

"""
STRINGS
"""

"""
Multiline Strings
"""
_str = """
sdasds
asdsasa
asdasdsadsadsa
asdsadsa
"""

"""
Formatted Strings
"""
varfetch = 5
print(f"bla bla bla {varfetch}")

"""
String Methods
"""

str.split("@") # -> list
str.index("kcl_")
str.find("abc)
str.strip("ch to strip from")
str.title()
str.capitalize()
str.replace(".", "-" ,...)
str.join(["item1", "item2"])
str.replace("str to be replaced", "str to replace")
str.startswith("str to find") # -> returns True/False
str.endswith("str to find") # -> returns True/False
str.upper()
str.lower()
str.isdigit() # if all chars are digit, True



"""
MODULES
"""

#module:            #main                       #alternative
def func():         from module import func     import module       #executes functions definitions and function calls
    print("")       func()                      module.func()


#module

if __name__ == "__main__":    # if module is ran, its __name__ is __main__, if the module is imported and executed from,
    print("ran from here")  # somewhere else, then __name__ is name of the module itself.

#directory access

#testD/test.py        #main

def func():         from testD.test import func
    print("")       func()


#constants

CONST = 100 #all capital letters to define a constant

dir(module_name) # -> CONST will show up here



"""
LIST
"""
nlist = [1, 2, [3, 4]]

"""
List Comprehensions
"""
x = [i for i in range(5) if i > 1] # assigns [2, 3, 4] to x variable

"""
List Methods
"""

list.sort()
list.clear()
list.pop()
list.remove()
list.__setitem(1, "house")__
list.__getitem(1)__
list.count(obj)  # -> returns number of occurrences of obj
list.append(obj)


"""
TUPLE
"""
# immutable list

ntuple = (1, 2, 3)

"""
DICTIONARY
"""
# "in" operator checks for keys in a dictionary, not values

ndict = {'key1' : 1, 'key2': 2, 'key3': [3, 4, 5]}

"""
DICTIONARY METHODS
"""
dict.pop(__key)
dict.keys()
dict.values()
dict.clear()
dict.get(key)
dict.__reversed__()

"""
TERNARY
"""
x = 1 if ... else

"""
MATCH - CASE
"""
while True:
    inp = input()

    match inp:
        case 1:
            ...
        case 2:
            ...
        case default:
            break

"""
TRY - EXCEPT - FINALLY
"""
try:
    ...
except ...: # Catch all exceptions if empty
    ...
finally:
    ...

"""
WITH CONTEXT MANAGER
"""
# built in exception handling, no need to close files
with open(..., "w") as file:
    file.read()

"""
FUNCTIONS
"""

"""
Function type hint
"""
def func(word: str)  -> str: # argument hint and return type hint
    return word

"""
Function return multiple
"""

def func(var1, var2)
    return var1, var2 # --> (var1, var2)


"""
LAMBDA
"""
# lambdas can't contain statements

func_name = lambda arg: arg*arg  #  func_name is now a function returning arg and can be called like func_name(3)
multiparam = lambda x, y: x*y
###########################
# lambda list comprehension
###########################

is_even_list = [lambda arg = x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

"""
DECORATORS
"""
# In short, decorators are useful when you have behavior which you want to apply to one or more functions,
# without having to modify the function directly. It allows for cleaner and more compact code.
# good for function testing

def caller(func):
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper


def printer(): # ->   same  as    @caller
    print("hello")              # def printer():


printer = caller(printer)       #   print("hello")
printer()

###########################
How to use parameters with decorator
###########################

def caller(func):
    def wrapper(*args, **kwargs):
        print("========")
        func(*args, **kwargs)
        print("========")
    return wrapper


@caller
def adder(x, y):
    print(x+y)


adder(2, 3)

"""
GENERATORS
"""
# Used when we want to fetch elements from a large list, useful for performance,
#           * Don't use for small files/data,
#           * Called only once, will provide 0 if called again

def generator():
    for i in range(10):
        yield i ** 2    # Returns 1 item at a time when it's called


for i in generator(): # Can be used in loops like an iterable
    print(i)


gen = (i for i in range(10)) # same thing, () creates generator expressions



"""
WHILE
"""
while True:
    ...

"""
FOR
"""
for item in range(10):
    ...

"""
Loop Operations - Enumerate(), Zip()
"""
for index, item in enumerate(['a', 'b', 'c']):
    #1 a  -> index = 1    item = a
    #2 b
    #3 c

for list1_items, list2_items in zip(list1, list2)
    #list1_items = list1[0]
    #list2_items = list2[0]


"""
#///////////////////////////////
#///////////////////////////////
#///////////////////////////////
"""

"""
######################################
METHODS & FUNCTIONS
######################################
"""

"""
MAP
"""
map(func, *iterables)  # -> map object
# calls the function on each element of the iterable


def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

"""
FILTER
"""
filter(function or None, iterable) # --> filter object
#  Return an iterator yielding those items of iterable for which function(item)
#  is true. If function is None, return the items that are true.

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))




"""
File Operations
"""

file.readlines() # -> list
file.read() # -> string --- Places the cursor at the end after executing
file = open("storage.txt", 'w') # -> open() has default "r" already
file = open(r"C\Users\Downloads\st.txt", "w") # -> r to bypass special characters
file = open("../files/doc.txt", "w") # -> .. goes up 1 directory
file.writelines(str(list)) # -> list
file.write("txt") # -> string

#############################
How to check if a file is empty
#############################

import os

if os.stat("total amount.txt").st_size == 0: # if empty


"""
Useful Functions
"""

input() # --> str
len()
isinstance(item, type)
type(item)
round(float, digit)
Counter(iterable) # from collections import Counter
sum(iterable)
print()
exit("msg") # shows red text
help(func_name)
all(iterable) # --> True if all elements are True or the list is empty

import time
print(time.strftime("%Y")) #year format %A : current day - Thursday, a% - Thu 

import glob
filepaths = glob.glob("*.txt") # --> a list containing all file names ending with .txt

import json                                                       #.json file, must enclose in [] or {}
with open("questions.json") as file:                                     [
                                                                             ...
    data = json.loads(file.read())      # --> list of the content        ]
    
    
import csv                                                              #.csv file
with open("weather.csv") as file:                                       "Antalya", "40"
                                                                        "Mersin", "38"
    data = list(csv.reader(file))     # --> list of lines as lists      "İstanbul", "30"   


import webbrowser
webbrowser.open("https://www.google.com/search?q=" + "steam") #searches "steam" on google


import shutil
shutil.make_archive("output", "zip", "folder") #creates zip named "output" from the folder named "folder"


import math
rads = math.radians(degree)

import random
print(random.randint(a, b)) # --> random int

##################
NETWORKING
##################
# Local
#ip addresses
import netifaces

netifaces.interfaces() # -> Obtain a list of the interfaces available on this machine. (cryptic names)

netifaces.ifaddresses(interface)[netifaces.AF_INET] # -> Obtain information about the specified network interface.
# Returns a dict whose keys are equal to the address family constants,
# e.g. netifaces.AF_INET, and whose values are a list of addresses in
# that family that are attached to the network interface. e.g:
for interface in netifaces.interfaces():
    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
        print(link['addr']) # prints all ipv4 addresses

# gateways
import netifaces
netifaces.gateways()["default"][netifaces.AF_INET]


"""
#///////////////////////////////
#///////////////////////////////
#///////////////////////////////
"""



