# Libraries
from ctypes import resize
import random
from enum import Enum
from functools import reduce
from typing import overload
import contextlib



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

# Elegant loops
count = 0
while count <= 3: print(count); count += 1

# While loops: lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0
#Your code below: 
while index < length:
  print('I am learning about', python_topics[index])
  index += 1

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

class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

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

class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  number_of_sides = 3
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
    else:
      return False

my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

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
def hello1():
    print('hello, world!')

hello1()


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
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]


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

# Secret
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
print (garbled[::-2])

# Bitwise operators
# The base 2 number system 
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)

# Left Bit Shift (<<)  
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print (bin(shift_right))
print (bin(shift_left))

# some operations
print (bin(0b1110 & 0b101))
print (bin(0b1110 | 0b101))
print (bin(0b1110 ^ 0b101)) 
print (~123)

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

a = 0b10111011
mask = 0b100
desired = a | mask
print (bin(desired))

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

# File input/output
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

# Some interesting functions
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index] 
  new_lst.append(lst[index]*2)
  new_lst = new_lst + lst[index+1:]
  return new_lst

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

# Advanced functions
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

# Advanced loops

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for lst in lst1:
    sum1 += lst
  for lst in lst2:
    sum2 += lst
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

def over_nine_thousand(lst):
  sum1 = 0
  for number in lst:
    sum1 += number
    if sum1 > 9000: # could be dynamic (not only 9000)
      break
  return sum1

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)
    
# print(solution(sentence1))
# print(solution(sentence2))

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

# Approach 1: 
def solution(num1,num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))
            
print(solution(num1,num2))

#Approach2 
#Given a string of length one, the ord() function returns an integer representing the Unicode code point of the character 
#when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10        

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)
print(solution(num1, num2))


def real_matr(A, R):
    lis = sorted( list(A) )
    matr = []
    for i in range( len(lis) ):
        row = []
        for j in range( len(lis) ):
            row.append( R( lis[i], lis[j] ) )
        matr.append(row)
    return matr

def refl(matr):
    for x in range( len(matr) ):
        if not matr[x][x]:
            return False
    return True

def antisymm(matr):
    for x in range( len(matr) ):
        for y in range( x, len(matr) ):
            if matr[x][y] and matr[y][x]:
                if x != y:
                    return False
    return True

# Nested comprehension:
values = [[y*3 for y in range(x)] for x in range(10)]

values = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y*3)
    values.append(inner)


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise

# Operator overloading

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)

print('\n\n')

# reversed tree
rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('   ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')
