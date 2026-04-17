#PRACTICE PROBLEMS
'''
#1.anagram

def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")

s1 = input().lower()
s2 = input().lower()

anagram(s1, s2)

#2.factorial

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

num = int(input("enter a num:"))
factorial(num)

#3.palindrome

def palindrome(s):
    if s == s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

s = input().lower()
palindrome(s)

#4.fibonaci series

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input())
fib(n)

#5.right angle triangle

def func(rows):

    for i in range(1,rows+1):
        for j in range(i):
            print("*" , end = " ")
        print()
rows=int(input())
func(rows)

#6.Diamond

def func(rows):

    for i in range (1,rows+1):
        for j in range(0,rows-i):
            print(" ",end="")
        for k in range(i):
            print("*",end=" ")
        print()
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(" ",end="")
        for k in range(rows- i):
            print("*", end=" ")
        print()
rows=int(input())
func(rows)

'''












