#pattern program
'''
num=int(input("ENTER THE LIMIT: "))
for j in range(num):                    ---> postion
    for i in range(j):                  ---> to prints *
        print("*", end = "")
    print()

num=int(input("ENTER THE LIMIT: "))
for j in range(1,num+1):                   # ---> postion
    for i in range(1,j+1):                  #---> to prints *
        print(i, end = "")
    print()

num=int(input("ENTER THE LIMIT: "))
for j in range(1,num+1):
    for i in range(1,num+1):
        print("*",end=" ")
    print()


num=int(input("ENTER THE LIMIT: "))
for j in range(1,num+1):                   
    for i in range(1,num-j):                  
        print("*", end = " ")
    print()


num=int(input("ENTER THE LIMIT: "))
for j in range(num):                   
    for i in range(num-j):                  
        print("*", end = " ")
    print()


num=int(input("ENTER THE LIMIT: "))
for j in range(1,num+1):
    print(" "*(num-j),end=" ")
    for i in range(1,j+1):
        print("*",end = " ")
    print()

num=int(input("ENTER THE LIMIT: "))
for j in range(num):
    print(" "*(num-j-1),end= "")
    for i in range(j+1):
        print("*",end = " ")
    print()
'''


























