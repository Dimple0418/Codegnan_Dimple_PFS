# modules
# -----------
# ---> A module in a python is simply file that contain python code (functions, varaibles,classes )
# ---> To use modules,we have to use keyword called import before the module
# ---------------------------
# Types of modules -- 1) Built-in or Inbuilt  2)User define modules

'''
Modules in Python

A module in Python is a file that contains Python code like:

functions
variables
classes
reusable logic

📌 A module is simply a .py file.
Example: math.py, mymodule.py
'''

# TYPES OF MODULES

# 1- User define module -- { Created by user }
#--------------------
# This is developed by the user or programmer inside a file of python code and used by called import with file_name..
# Syntax
'''
--> import(keyword) file_name
    file_name .functionality
'''
# -- examples

'''

import prac_1
print(prac_1.add(10,5))
print(prac_1.sub(6,3))
print(prac_1.mul(2,5))

import prac_1
print(prac_1.func(5))

'''


# 2- Built-in or InBuilt -- { Already available in Python }
#----------------------
# Already these are comes with installation and they are ready to use in the program
# This is developed by developers

'''
1)math
2)random
3)os
4)sys
5)datetime
'''
# -- examples
'''
import math
print(math.sqrt(100))


import math
num = 25
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))

'''

# GUESSING NUMBER

'''

import random
attempts=3
k=random.randint(1, 100)
print(k)
while attempts>0:
    n=int(input("Enter a number : "))
    if  k== n :
        print("True")
    else:
        print("Flase")
    attempts-=1

'''
    












