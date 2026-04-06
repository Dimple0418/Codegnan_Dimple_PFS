#function --\
'''
It is a block of code which is reusable.
These are two types
   1. built-in or in-build
   2. user defined
========================================
1.Built -in or in- build
  --> They comes with program and those are already defined
      eg: print(),sum(),map()...
      
2.user define
  --> This is created by person who is developing or using for development
      syntax -- ( user define )--  iit's start wiht def keyword followed bye function_name and it has calling function...
      ()--  what are in paranthesis they called PARAMETERS
      function_name()--- in this we alled as ARGUMENTS

      
      def function_name():
          -------
          -------
          -------
          -------
      function_name()
'''

#by using def function
#even-odd numbers
'''
def flm(a):
    if a % 2 ==0:
        print("it is even number")
    else:
        print("it is odd number")
a=int(input())
flm(a)

a=7
def flm(a):
    if a % 2 ==0:
        print("it is even number")
    else:
        print("it is odd number")

flm(a=5)


a=int(input("ENTER A NUMBER: "))
count=0
def user(a):
    for j in range(1,a+1):
        if a % j ==0:
            count+=1
            
            print("it is prime number")
            
            count+=2
            
            print("it not a prime number")
user(a)

prime_num=int(input())
count=0
def prime_check(num,k):
    for j in range(1,num+1):
        if num % j == 0:
            k+=1
    if k==2:
        print("prime")
    else:
        print("not")

prime_check(prime_num,count)
    

a=int(input())
c=0
def lkm(a,c):
    for j in range(1,a+1):
        if a%j==0:
            c+=1
    if c==2:
        print("it is prime number")
    else:
        print("it is not prime number")
lkm(a,c)
'''

#differnce btw == and is

'''
a=[1,3]
b=[1,3]
print(id(a),id(b))
c=b
print(c is b)   #is --- used for location or object

a=[1,3]
b=[1,3]
print(id(a),id(b))
a=b
print(a is b)


a=[1,3]
b=[1,3]
c=b
print(c == b)

a=4
b=4
print(a == b)
'''





























