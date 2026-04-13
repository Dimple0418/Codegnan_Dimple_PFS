# Generators
# ----------------
'''
# This is a special type of function that return an ITERATOR. Which one at a time
# Generator is a special type of function in Python that returns values one by one instead of returning everything at once.
# It uses the keyword yield instead of return.

'''

#1-code

'''
def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()
print(next(an))
print(next(an))
print(next(an))

'''
#2-code
'''
def square_gen(n):
    for i in range(n):
        yield i* i
for val in square_gen(5):
    print(val)

'''
# Difference btw YIELD & RETURN

#yield

'''
--> It will take a pause and again resume, this is not a nrml keyword can not be used in ethe nrml fuctions
-->This is used to produce a value and pause execution

Gives output -- multiple times
Stops function -- pauses and continues

'''

#Next()

'''
--> This is used to get next vlaue from a generator
--> When the value is finished , it will stop the iterator

'''

# Generator with Loop + next()
'''
def numbers():
    for i in range(1, 6):
        yield i

g = numbers()
print(next(g))
print(next(g))
print(next(g))
'''

#next() after values finished (StopIteration)

#--When generator values are finished, Python gives StopIteration error.

'''
def gen():
    yield "A"
    yield "B"

g = gen()

print(next(g))  
print(next(g))  

print(next(g)) 
'''












