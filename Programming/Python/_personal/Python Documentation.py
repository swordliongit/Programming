


"""
How to turn your .py into .exe
"""

# pip install pyinstaller
# pyinstaller main.py --onefile

# Python major.minor.patch => Python 3.11.2

"""
You are correct that if not mlist: will not always work as expected. This is because in Python, an empty list is considered a "falsy" value, but there are other "falsy" values such as None, False, and the integer 0.

Therefore, if not mlist: will evaluate to True only if mlist is an empty list. If mlist is None, False, or 0, the condition will evaluate to False.

To properly check if a list is empty, you should use if len(mlist) == 0: or if not mlist:, but be aware that the latter will not work if the variable is None, False, or 0.
"""

dir(list)
dir(str)

help(str.capitalize())

"""
Shallow and Deep Copy
"""

list1 = [1, 2, 3]

list2 = list1

list2[0] = 4 # Also changes list1 - Shallow copy

------------

list2 = list1[:]

list2[0] = 4 # Doesn't change list1

#but if;
list1 = [1, 2, 3, [4, 5]]

list2 = list1[:]

list2[3][0] = 6 # Also changes list1's sublist

------------

from copy import deepcopy

list2 = deepcopy(list1)

list2[3][0] = 6 #Doesn't change list1's sublist now


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
# objects are passed as references(e.g. -> Queue() )

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

# XXX XXXXXXXXXXXXXXXXXXXXXXX
Dictionary Comprehension
# XXX XXXXXXXXXXXXXXXXXXXXXXX

dict = {key_expr:val_expr for item in iterable}
# XXX #

dict = {'key1' : 1, 'key2': 2, 'key3': 3}

key_list = ['key1', 'key2']

filtered_dict = {key: dict[key] for key in key_list} # creates a dictionary that's filtered by the key_list's items as keys
                                                     # and values as the dictionary's values which we want to filter

numbers = [1, 2, 3]

new_dict = {item: item**2 for item in numbers} # creates a dictionary that has value as square of items in the numbers list and keys
                                               # as those numbers in the list



"""
DICTIONARY METHODS
"""
dict.pop(__key)
dict.keys()
dict.values()
dict.clear()
dict.get(key)
dict.__reversed__()
dict.update(dict) # e.g. dict.update({k:v})

dict.items() -> dict_items([('key1', val1), ('key2', val2), ('key3', val3)])
for x in our_dict.items():
    print(x[0]) # x[0] == 'key1'  x[1] == val1


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
MULTI-THREADING
"""
import threading

def func():
    thread = threading.Thread(target=another_func args=(arg1,)) # calls another function while running this function
    thread.start()

# multi-threads

threads = []

for ip in ip_list: # call multiple versions of the function simultaneously
    t = threading.Thread(target=modem_login, args=(driver, ip, output))
    threads.append(t)
    t.start()
    
for t in threads: # wait for all threads to finish
    t.join()



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

#############################
MAP
#############################
map(func, *iterables)  # -> map object
# calls the function on each element of the iterable


def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))



#############################
FILTER
#############################

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

# Dictionary Filter

# Original dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Use filter() to filter out odd values
filtered_dict = dict(filter(lambda x: x[1] % 2 == 0, d.items()))


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
Useful Functions and Modules
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

#############################
TIME
#############################
import time
print(time.strftime("%Y")) #year format %A : current day - Thursday, a% - Thu 

#############################
GLOB
#############################
import glob
filepaths = glob.glob("*.txt") # --> a list containing all file names ending with .txt

#############################
JSON
#############################
import json                                                       #.json file, must enclose in [] or {}
with open("questions.json") as file:                                     [
                                                                             ...
    data = json.loads(file.read())      # --> list of the content        ]
    
    json.dump(data_list, file, indent=5) # --> write a list into a json file

#############################
CSV
#############################
import csv                                                              #.csv file
with open("weather.csv") as file:                                       "Antalya", "40"
                                                                        "Mersin", "38"
    data = list(csv.reader(file))     # --> list of lines as lists      "İstanbul", "30"   

#############################
BROWSER
#############################
import webbrowser
webbrowser.open("https://www.google.com/search?q=" + "steam") #searches "steam" on google

#############################
ZIP/ARCHIVE
#############################
import shutil
shutil.make_archive("output", "zip", "folder") #creates zip named "output" from the folder named "folder"


#############################
MATH
#############################
import math
rads = math.radians(degree)

#############################
RANDOM NUMBERS
#############################

import random
print(random.randint(a, b)) # --> random int


#############################
QUEUE
#############################

# Thread safe, dynamic

from queue import Queue

queue = Queue()

queue.put(obj)

print(queue.get())


"""
NETWORKING
"""
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



#general network scan ( scapy )

from scapy.all import ARP, Ether, srp
#target_ip = "192.168.5.0/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
# a list of clients, we will fill this in the upcoming loop
clients = []
for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})


"""
BASIC GUI
"""
import PySimpleGUI

label = PySimpleGUI.Text("Press Start")

window = PySimpleGUI.Window("Modem Config Engine", layout=[""])
window.read()
window.close()


"""
DIRECTORY
"""
def create_directory(filename): # create directory based on filename e.g. = "./hosts/"
    # Extract the directory name from the file path
    dirname = os.path.dirname(filename)
    
    # Create the directory if it does not exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)


"""
#///////////////////////////////
#///////////////////////////////
#///////////////////////////////
"""



