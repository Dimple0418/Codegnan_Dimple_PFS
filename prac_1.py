'''def add(d,r):
    return d+r

def sub(d,r):
    return d-r

def mul(d,r):
    return d*r

'''

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
    return " "
    
'''
def add(num,count):
    for i in range (1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} it is prime number")
    else:
        print(f"{num} it not a prime number")
num=int(input("ENTER A VALUE : "))
count=0  
add(num,count)'''
