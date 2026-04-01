#even and odd

'''
n=[1,2,3,4,5,6,7,8,9]
for j in n:
    if j % 2==0:
        print(f"{j} is even number")
        even += j
    else:
        print(f"{j} i odd number")
        odd += j 
'''
#tables
'''
table_num=8
for j in range (1,11):
    print(table_num * j)



table_num=9
for j in range (1,13):
    print(f"{table_num}x{j}= {table_num * j}")


table_num=int(input())
for j in range (1,13):
    print(f"{table_num}x{j}= {table_num * j}")

sentence=input()
count_U =[]
count_L =[]
for j in sentence:
    if j.isupper():
        count_U.append(j)
    elif j.islower():
        count_L.append(j)
print(f"There are {count_U} capital letters")
print(f"There are {count_L} small letters")
    
    

sentence=input()
count_U =0
count_L =0
for j in sentence:
    if j.isupper():
        count_U +=1
    elif j.islower():
        count_L +=1
print(f"There are {count_U} capital letters")
print(f"There are {count_L} small letters")
'''

#ATM PIN
'''
SBI_SRINU_AC_DETAILS={"NAME":"CHITTIMUJU SRINUVASU RAO",
                      "ATM PIN":"1750"}
print("wellcome to SBI ATM")
print("please insert your card")
SBI_USER=input("ENTER YOUR PIN NUMBER : ")
if len(SBI_USER)==4:
    if SBI_USER in SBI_SRINU_AC_DETAILS['ATM PIN']:
        print("YOUR NUMBER IS CORRECT")
    else:
        print("PLEASE ENTER CORRECT NUMBER")
else:
    print("YOUR ENTERED NUMBER IS WRONG")'''


#PERFECT NUMBER 
'''
num=int(input())
num_all=0
for j in range(1,num):
    if num % j == 0:
        num_all +=j
if num_all == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")'''

































