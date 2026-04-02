#control statement --
#Break -- this is used to exit from the lopp , when we found the required value , it skip the if condition 
'''

for j in range (1,10):
    if j ==5:                 ----> if print is given after if condition that it will print only the value 5
         print(j)
         break

for j in range (1,10):
    print(j)                 --->if print is given before if condition that it will print only the all values in loop
    if j ==5: 
         break


list_1=[1,2,3,4,5]
for j in list_1:
    print(j)
    if j==4:
        break

list_1=list(map(int,input().split(" ")))
for j in list_1:
    print(j)
    if j==4:
        break
'''     

#Continue -- this is used to skip the particular loop
'''
for i in range(1,10):
    if i == 7:
        continue
    print(i)

list_1=[1,2,3,4,5,6,7,8,9]
for j in list_1:
    if j == 2:
        continue
    print(j)

'''

#pass --- this is called as space holders incase any statement like(if,elif,else,for..)this should be complete , if not we will get syntax or indentation error to avoid this we are using ' pass '

'''
for j in range (1,10):
    if j ==9:
        pass
'''
#else-- in for loops, if we use else , it will fall back to else block,when all loops are completed
'''
for n in range (1,10):
    print(n)
else:
    print("else block")

'''
#FIBONACCI SERIES ---- We used  end (syntax -- end="") method to separate the sequence or numbers and also we used swapping method here 
'''
user_in=int(input("ENTER THE LIMIT : "))
num1=0
num2=1
print(num1,num2,end=" ")
for an in range(user_in):
    num_3=num1+num2
    num1=num2
    num2=num_3
    print(num_3, end=" ")

user_in=int(input("ENTER THE LIMIT : "))
num1=0
num2=1
for an in range(user_in):
    print(num1,end=" ")
    num_3=num1+num2
    num1=num2
    num2=num_3

'''

#while loop -- This is a combination for and if statements , if we did not end the loop in properway it will run upto the memory space in the becomes empty  















