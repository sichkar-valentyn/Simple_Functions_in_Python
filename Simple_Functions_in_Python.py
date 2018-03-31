# File: Simple_Functions_in_Python.py
# Description: Simple examples on how to create and use functions in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Simple examples on how to create and use functions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Simple_Functions_in_Python (date of access: XX.XX.XXXX)


# Creating functions in Python
def min2(a, b):  # Defining function with two parameters
    if a <= b:
        return a
    else:
        return b
    

print(min2(2, 3)) 
print(min2(min2(5, 6), 4))  # It is possible to use function inside function


# Another example
def f(n):
    return n * 10 + 5
print(f(f(f(10))))  # Calculating result from function itself 3 times


# We define with mark '*' and the number of parameters can be any and it is stored in the list a[]
def min2(*a):
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m


print(min2(2, 3, 5, 6, 7, -1))


# Example how to define parameter by default using '=' and value
def my_range(start, stop, step = 1):
    r = []
    if step > 0:
        x = start
        while x < stop:
            r += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            r += [x]
            x += step
    return r


print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))


# We can also use the names of parameters and write them when calling the function in different order
print(my_range(stop = 20, start = 1))


# Local variables inside function can't change the values with the same name outside the function
def local_variables():
    a = 100

# In this case variable 'a' will not be changed by function
a = 0
local_variables()
print(a)

# The same if we pass 'a' from the outside of the function as parameter of function
def local_variables_1(a):
    a = 100
    
b = 0
local_variables_1(b)
print(b)

# If we want to use functions and their local variables to change global variables
def append_to_list(list1):
    list1.append(0)  # This will change the list
    list1 = [100]  # this will not change the list from outside because it references to different memory

a = [1, 2]
append_to_list(a)
print(a)
    

# Global variables we can use everywhere inside program even inside functions
def print_value():
    print(a)  # Variable is not defined inside function as local, so it is global
a = 5
print_value()


# Implementing the task
# Function processes list by deleting odd vlues and integer divivsion for even numbers
def modify_list(list1):
    for i in range(len(list1) - 1, -1, -1):  # Going through the list from end to the beginning
        if list1[i] % 2 == 0:
            list1[i] = list1[i] // 2
        else:
            del list1[i]  # Because we change the size of the list and if we go from the beginning it will be error 

lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)
