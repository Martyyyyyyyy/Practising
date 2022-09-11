# Libraries
from ctypes import resize
import random
from enum import Enum
from functools import reduce
import re
from typing import overload



# Dictionaries
dict = {'name': 'Tim', 'color': 'red', 'age': 25}


# Lists
food = ['pizza', 'carrots', 'eggs']
dinner = random.choice(food)


# Data Types
name = 'Martin'
print(isinstance(name, str))
age = int('20') # some casting
print(isinstance(age, int))


# Ternary operator
def is_adult(age):
    return True if age > 18 else False


# Strings
# concatenation
name = 'Martin' + ' is my name'
# some casting 
age = str(25) 
"""
another comment but a verrrryyyyyyyyyyyyyyyyyyy 
looooooooooooooooooooooonnnnnnnnnnngggggggggggggggggggggggggg
"""


# Strings methods
new_name = name.upper()
print(new_name)
print('david malan'.title()) 
check_1 = name.isalpha()
check_2 = name.isalnum()
print(len(name)) 
print('tin' in name)


# Escaping characters
name = 'Mar\'tin'
print(name)


# Complex number
num1 = 2 + 3j
num2 = complex(2, 3)
print(num2.real, num2.imag)


# Buit-in functions
abs(-5.4)
round(3.571)


# Enums
class State(Enum):
    # Capitalized bcs value is constant
    INACTIVE = 0 
    ACTIVE = 1

print(State.ACTIVE.value)
print(list(State))


# Lists
names = ['Martin', 23, 'Syd', True, 'Quincy', 7]
# changing item in the list by index
names[2] = 'Beau'
# append for adding items
names.append('Judah')
# extend (or just +=) for adding a whole list to existed
names.extend(['John', 23, 'green'])
names += ['x', 'y']
# removing exect item
names.remove('Quincy')
# removing last item 
names.pop()
# add item in exact place, where you want, by indicating index
names.insert(3, 'Text')
# or
names[1:1] = ['Test1', 'Test2']
# sorting list (could be sort with one data type in the list)
numbers = [23, 12, 5, 0, 45, -3, 16]
numbers.sort() 
names1 = ['Roger', 'Bob', 'Martin', 'Quincy']
names1.sort()
#sorting by lowercase (could be vice versa)
names1.sort(key=str.lower)
# or we can sort with buit-in function
sorted(names1, key=str.lower)
#copying ([:] - means a whole list)
numbers_copy = numbers[:]
# fun way to add characters in the list
alphabet = []
alphabet += 'abcdefghijklmnopqrtsuvwxyz'
print(alphabet)


# Tuples
dogs = ('Roger', 'Syd', 'Beau')
# find out what index has item
dogs.index('Roger')
# some common methods that we can use everywhere
len(dogs)
print('Syd' in dogs)
sorted(dogs)
# also a one more for concatenatig tuples
new_dogs = dogs + ('Barny', 'Tina')


# Dictionaries
dog = {'name': 'Roger', 'age': 8, 'color': 'brown'}
# changing value in key 'name'
dog['name'] = 'Syd'
print(dog)
print(dog.get('name'))
# deleting items
dog.pop('age')
# deleting last key-value pair
dog.popitem()
# same buit-in functions for all types
print('color' in dog)
print(len(dog))
del dog['name']
dog_copy = dog.copy()
# getting key, values, items (could also convert into lists)
dog.keys()
list(dog.values())
list(dog.items())
# adding a key-value pair
dog['favorite food'] = 'Meat'
print(dog)


# Sets (set cannot have duplicates)
set1 = {'Martin', 'Violetta', 'Brenda'}
set2 = {'Brenda'}
set3 = {'Valerie'}
intersect = set1 & set2
print(intersect)
union = set1 | set3
print(union)
mod = set1 - set3
print(mod)
print(list(set1))


# Functions
def hello(x):
    print('hello!')
    
def change(value):
    value['name'] = 'Syd'

val = {'name': 'Beau'}
change(val)
print(val)

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I'm gonna buy this milk")

# outer function
def counter():
    count = 0

    # inner function
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()

print(increment())
print(increment())
print(increment())


print('-----------------------------------------------------------')


# Objects
age = 7
print(age.real)
print(age.imag)
print(age.bit_length)
items = [1, 2]
items.append(3)
items.pop()
print(id(items))


# Loops
# actually infinite loop
"""
condition = True
while(condition):
   print('infinite loop')
"""
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print('index:', index, '-', 'value:', item)

for i in range(3):
    for j in range(3):
        print('#', end='')
    print()


# Break and continue
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 2:
        continue
    print(item)

print('-------------------------------------')

for item in items:
    if item == 3:
        break
    print(item)    


# Classes
class Animal:
    def walk(self):
        print('Just walking...')

# inheritance
class Dog(Animal):
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('woof!')

roger = Dog('Roger', 5)
print(type(roger))
print(roger.name, roger.age)
roger.bark()
roger.walk()


# Modules (every python file)
import dog

dog.barking()

# or (same)
from dog import barking

barking()

# some python libraries
"""
math, re, json, datetime, sqlite3, os, random, statistics, requests, http, urllib
"""


# Accepting arguments
"""
just command line arguments
"""


# Lambda function
n = lambda n: n ** 2
print(n(3))
multiply = lambda a, b: a * b
print(multiply(2,4))


# Functions map(), filter(), reduce()
num = [1, 2, 3]

def double(x):
    return x * 2

rez = map(double, num)
print(num)
print('new list:', list(rez))

# also same with lambda

rez1 = map(lambda x: x * 2, num)
print('same with lambda:', list(rez1))

rez2 = filter(lambda x: x % 2 == 0, num)
print(list(rez2))

expenses = [
    ('Martin', 23),
    ('Beau', 20)
]
sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)

# or 

sum = reduce(lambda x, y: x[1] + y[1], expenses)
print(sum)


# Recursion
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)

print(factorial(5))   

print('--------------------------------------')


# Decorators
def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@logtime
def hello():
    print('hello, world!')

hello()


# Docstrings
"""
Just this thing, like a looong comment
"""


# Annotation
def incrementing(n: int) -> int:
    return n + 1

annotation: int = 1


# Exceptions
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result)


# With
"""
filename = '/Programmin/Python/Practising/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
"""


# pip (python package index)


# List compressions
num = [1, 2, 3, 4, 5]
num_pow = [n ** 2 for n in num]
print(num_pow)


# Polymorphism
class Cat:
    def eat(self):
        print('Eating cat food')

class Fish:
    def eat(self):
        print('Eating fish food')

animal_1 = Cat()
animal_2 = Fish()

animal_1.eat()
animal_2.eat()


# Operator overloading
class Overloading:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Overloading('Roger', 5)
syd = Overloading('Syd', 7)
print(roger > syd)