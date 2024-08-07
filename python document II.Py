Functions, Scoping, Data Collections 1 & List Comprehensions
Tasks Today:
Monday Additions (or, and ... if statements)

String Manipulation
     a) strip()
     b) title()
Working With Lists
     a) min()
     b) max()
     c) sum()
     d) sort()
     e) Copying a List
     f) 'in' keyword
     g) 'not in' keyword
     i) Checking an Empty List
     j) Removing Instances with a Loop
List Comprehensions
Tuples
     a) sorted()
Functions
     a) User-Defined vs. Built-In Functions
     b) Accepting Parameters
     c) Default Parameters
     d) Making an Argument Optional
     e) Keyword Arguments
     f) Returning Values
     g) *args
     h) Docstring
     i) Using a User Function in a Loop
Scope
String Manipulation
.lstrip()
# string.lstrip()
name = "          hJohn Smith"
stripped_name = name.lstrip(" " "h")
print(stripped_name)
#or print(name.lstrip(" " "h"))
John Smith
.rstrip()
# string.rstrip()
name = "Bill Ross          th"
print(name.rstrip(" " "th"))
Bill Ross
.strip()
# string.strip()
name = "   John Smith    "
print(name.strip())
John Smith
.title()
# string.title()
president = "barack obama"
print(president.title())
# or print(president.upper())  - upper case
# or print(president.lower())  - lower case
Barack Obama
String Exercise
Strip all white space and capitalize every name in the list given

names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration

# first I will create a new list to hold names after changes
# then I will loop through first list
# then I will strip white space in each name
# then I will capitalize each name
# then I will save the changed name in a variable
# then I will add changed names to new list
# then I will print the newlist with changes made

changed_names_list = []

for name in names:
    changed_name = name.strip().title()
    changed_names_list.append(changed_name)
print(changed_names_list)
['Connor', 'Max', 'Evan', 'Jordan']
Working With Lists
min()
# min(list)
numbers = [4, 5, 97, 54, 16]

print(min(numbers))
4
max()
# max(list)

print(max(numbers))
97
sum()
# sum(list)

print(sum(numbers))
176
sorted()
# sorted(list)
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
[4, 5, 97, 54, 16]
[4, 5, 16, 54, 97]
[4, 5, 97, 54, 16]
.sort()
Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list

# list.sort()
print(f'Before sort: {numbers}')
print(numbers.sort())
print(numbers)

# use sorted when you don't want to alter original list, use .sort() when you want to alter original list
Before sort: [4, 5, 97, 54, 16]
None
[4, 5, 16, 54, 97]
Copying a List
# [:] copies a list, doesn't alter original
list_1 = numbers [:]
print(list_1)
[4, 5, 16, 54, 97]
'in' keyword
l_teachers = ["Joel", "Derek", "Conner", "Brian", "Joe"]

# if 'Derek' in l_teachers:
#     print('Coding Temple Instructor')
# else: 
#     print('Not an instructor')

for name in l_teachers:
    if 'C' in name:
        print('Found')
    else:
        print ('Not Found')

# Can use index in for loop to check letter C in first position example on above: if 'C' in name[0]:
Not Found
Not Found
Found
Not Found
Not Found
'not in' keyword
if 'zack' not in l_teachers:
    print('Not a CT instructor')
Not a CT instructor
Checking an Empty List
# if l_1: or if l_1 = []
list_2 = []

if list_2 == []:
    print('Is Mayonaise an instrument')
Is Mayonaise an instrument
Removing Instances with a Loop
# while, remove
names = ['Conner', "Joel", 'Max', "Evan", "Evan", "Rob"]

while 'Evan' in names:
    names.remove('Evan')
print(names)

# for name in names: 
#     if name == 'Evan':
#         names.remove('Evan')
# print(names)

# For loops can miss duplicate items because they go one index at at time (add one)
# which can get messy with changing positions, 
# while loops start over each time from the beginning and are a better choice though they take longer.
['Conner', 'Joel', 'Max', 'Rob']
List Exercise
Remove all duplicates
Extra: Create a program that will remove any duplicates from a given list

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier
# Desires output: ['connor', 'bob', 'evan', 'max', 2, 3, 4, 'kevin']

# I need to create a blank list
# I need to go through the list - loop
# and determine if item is a duplicate -comparison
# and if duplicate remove items from the old list - .pop?
# and add to the new list - .append
# then print the list     - print statment

no_duplicates_list = []
for i in names:
    if i not in no_duplicates_list:
        no_duplicates_list.append(i)
print(no_duplicates_list)
['connor', 'bob', 'evan', 'max', 2, 3, 4, 'kevin']
List Comprehensions
Creating a quickly generated list to work with
*result* = [*transform* *iteration* *filter* ]

In a list comprehension we have a few pieces:
The first is the counter/ variable - IN this the variable is x
then we have a transform for the variable
The finale part of a list comp is called the condition
[transform, variable, condition]
     what do we do to something (transform / expression)
                where are we getting that something from (variable / value)
                           what has to be met for that to work (condition -if statements etc)
# number comprehension

# With a regular for loop

nums = []

for i in range(100):
    if i % 2 ==0:
        nums.append(i**2)
print(nums)


#[transform, variable, condition]

print('\n')
nums_comp = [i**2 for i in range(100) if i % 2 == 0]
print(nums_comp)

# not every single for loop that works with lists can be writtin into a comprehension
# https://improveandrepeat.com/2020/07/python-friday-30-list-comprehension/      
# -At website look at All together in one image section [(expression) for (value) in (collection) if (condition)]
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]


[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]
There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.

Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.

Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# square number comprehension

print([x**2 for x in range(10)])

print('\n')

squares_reg = []
for x in range(10):
    squares_reg.append(x**2)
print(squares_reg)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
string comprehension
#  string comprehension

names = ['Conner', 'Max', 'Evan', 'Rob']

first_char_comp = [name[0] for name in names]
print(first_char_comp)

first_char = []

for name in names:
    first_char.append(name[0])
print(first_char)
['C', 'M', 'E', 'R']
['C', 'M', 'E', 'R']
c_names = [first_name for first_name in names if first_name[0] == 'C']
print(c_names)

c_names_reg = []

for first_name in names:
    if first_name[0] =='C':
        c_names_reg.append(first_name)

        
print(c_names_reg)
['Conner']
['Conner']
Tuples
Defined as an immutable list


Seperated by commas using parenthesis
tup_1 = 1, 2, 3 # First way of creating a tuple
tup_2 = (1,2,3) # Other way of creatig a tuple

# print(type(tup_1))
# print(type(tup_2))

print(tup_1[0])

print(len(tup_1))

# Looping over tuples
for number in tup_1:
    print(number)

# Looping over a tuple with an index using range and len
for number in range(len(tup_1)):
    print(tup_1[number])
    
# Cannot use things like .pop() or .append() on a tuple because it is immutable.
1
3
1
2
3
1
2
3
sorted()
tup_3 = (20, 5, 1, 5, 3, 9, 45)

sorted_tup = sorted(tup_3)
print(sorted_tup)

random_list = [3, 4, 66, 77, 33]
combine_list = sorted(sorted_tup + random_list)

new_tup = tuple(combine_list)

print(new_tup)
print(type(sorted_tup))
print(tup_3)

# sorted will return a list which is mutable
[1, 3, 5, 9, 20, 45]
(1, 3, 3, 4, 5, 9, 20, 33, 45, 66, 77)
<class 'list'>
(20, 5, 1, 3, 9, 45)
Adding values to a Tuple
print(tup_1)

tup_1 = tup_1 + (5,)   #declaring a new variable, overwriting what is stored in the memory with a new same name variable
print(tup_1)
(1, 2, 3)
(1, 2, 3, 5)
Functions
User-Defined vs. Built-In Functions
# User defined    -Until you call the function, it's the idea of something, kind of like the blueprint of a house.
def sayHello():
    return 'Hello World'

sayHello()
# print(sayHello())
'Hello World'
Accepting Parameters
# ARGUMENTS OR PARAMETERS
# Order matters
# a variable can be of any type of object
def printFullName(first_name, last_name):
    return f'Hello, {first_name} {last_name}'

a_name = input('What is your first name?  ')

print(printFullName('Joel', 'Carter'))
print(printFullName(a_name, 'Apol'))
print(printFullName('a', 'Carter'))
print(printFullName('b', 'Carter'))
print(printFullName('c', 'Carter'))
print(printFullName('d'))    #error here due to missing second parameter
What is your first name?  Brandon
Hello, Joel Carter
Hello, Brandon Apol
Hello, a Carter
Hello, b Carter
Hello, c Carter
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [37], in <cell line: 14>()
     12 print(printFullName('b', 'Carter'))
     13 print(printFullName('c', 'Carter'))
---> 14 print(printFullName('d'))

TypeError: printFullName() missing 1 required positional argument: 'last_name'
Default Parameters
# Default paramters need to be declared AFTER non-default parameters each time

def printAgentName(first_name, last_name = 'Bond'):
    return f'The name is {last_name} ... {first_name} {last_name}!'

print(printAgentName('James'))

# DON'T DO THIS  - putting default parameters before non-defaul parameters.  Syntaxerror:
def printAgentAgain(last_name = 'ever', first_name):
    return f'Last_name {last_name}, first name {first_name}!'

print(printAgentAgain(first_name = 'Greatest'))
  Input In [36]
    def printAgentAgain(last_name = 'ever', first_name):
                                                      ^
SyntaxError: non-default argument follows default argument
Making an Argument Optional
def printHorseName (first, middle ='', last = 'Ed'):
    return f'Hello {first} {middle} {last}'

printHorseName("Mr")
'Hello Mr  Ed'
Keyword Arguments
def printSuperHero(name, power = 'flying'):
    return f"The hero's name is {name} and superpower is {power}"

printSuperHero(power = 'Spidey sense', name = 'Spider Man')
"The hero's name is Spider Man and superpower is Spidey sense"
Creating a start, stop, step function
def my_range(stop, start=0, step=1):
    for i in range(start,stop,step):
        print(i)

my_range(20, 5, 2)
5
7
9
11
13
15
17
19
Returning Values
def addNums (num1, num2):
    return num1 + num2

addNums(5,2)
7
*args
# args stands for arguments and takes ANY number of arguments as parameters
# Must be last if multiple parameters are present
def printArgs(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)
    
    for arg in args:
        print(arg)
    
    for kwarg in kwargs:
        print(kwarg)

printArgs(36, 'DragonZord', 'vanilla', 2, 3, testing = "joel")
36
('DragonZord', 'vanilla', 2, 3)
{'testing': 'joel'}
DragonZord
vanilla
2
3
testing
Docstring
def printNames(list_1):
    """
    Function requires a list to be passed as a parameter
    and will print the contents of the list. Expecting a list of
    names(strings) to be passed.
    """
    for name in list_1:
        print(name)

printNames(['George', 'Ramon', 'Peter'])
help(printNames)
George
Ramon
Peter
Help on function printNames in module __main__:

printNames(list_1)
    printNames(list_1)
    Function requires a list to be passed as a parameter
    and will print the contents of the list. Expecting a list of
    names(strings) to be passed.

Using a User Function in a Loop
def printInput(answer):
    print(answer)

response = input('Are you ready to quit??  ')
    
while True:
    ask = input('What do you want to do? ')
    printInput(ask)
    
    response = input('Ready Yet?  ')
    if response.lower() == 'quit':
        break
Are you ready to quit??  No
What do you want to do? I don't know
I don't know
Ready Yet?  quit
Function Exercise
Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']

# first I will define a function with two parameters first name list and last name list
# then I will create an empty full names list
# then I will select the first name in the first names list - loop
# then I will assign the item in first name to a variable
# then I will select the first name in the last names list - loop
# then I will assign the item in last name to a variable
# then I will create a variable to hold the combined name
# then I will combine them in a string and assign them to the combined name variable - concatenation
# then I will add the new string to the full names list - .append
# then I will return the list of full names - return full_names
# last I will make call statement


#                                   THIRD TRY     took pieces from last answer here, edited and merged with my code:
# https://stackoverflow.com/questions/39266197/suppose-i-have-two-lists-in-python-a-list-of-first-names-and-a-list-of-last-name


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

def combine_names(fname_list, lname_list):
    """
    Loops through a list of first_names and a list of last_names, 
    combines the two and return a list of full_names.
    """

    full_names = []

    for index in range(len(first_name)):

        first = first_name[index]
        last = last_name[index]
        full_name = first + ' ' + last
    
        full_names.append(full_name)
    
    return full_names
    
merged_names = combine_names(first_name, last_name)
print(merged_names)
['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
Scope
Scope refers to the ability to access variables, different types of scope include:
a) Global
b) Function (local)
c) Class (local)

number = 3 # Global variable; accessible ANYWHERE in my code now

def myFunc():
    number = 6 # Local function variable
    number += 4
    return number
    
print(number + 4)
print((myFunc()))
7
10
Exercises
Exercise 1
Given a list as a parameter,write a function that returns a list of numbers that are less than ten


For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def under_ten(list):
    solutions = [x for x in list if x < 10]
    return solutions

numbers_less_than_ten = under_ten(l_1)
print (numbers_less_than_ten)
[1, 5, 8, 9]
Exercise 2
Write a function that takes in two lists and returns the two lists merged together and sorted
Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merged_sorted(list1, list2):
    solutions_list = (list1 + list2)
    solutions_list.sort()
    return solutions_list
    
solution = merged_sorted(l_1, l_2)
print (solution)
[1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10]