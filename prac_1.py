def add(d,r):
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

#14-4-26
'''
#1
n=int(input())
for i in range(1,11):
    k=n*i
    if k%3==0:
        print(k)
'''

    
'''
#2
n=0
while n<11:
    print(n)
'''

'''
#3

n=int(input())
k=0
while k<5:
    k+=1
    print(n*k)
'''



#4





'''
def pyramid(rows):
    for i in range(1,rows+1):
        for j in range(rows+1-i):
            print(" ",end="")
            
        for k in range(i):
            print("*",end=" ")
        print()
    
rows=int(input())
pyramid(rows)





def pyramid(num):
    for i in range(1,num+1):
        for j in range(i):
            print("*",end="")
            
        print()
    
num=int(input())
pyramid(num)


def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")

s1 = input().lower()
s2 = input().lower()

anagram(s1, s2)





def withdraw(bal):
    user=int(input("ENTER AMOUNT FOR WITHDRAW : "))
    bal-=user
    print(bal)

def deposit(bal):
    user_1=int(input("ENTER A AMOUNT: "))
    bal+=user_1
    print(bal)

def check(bal):
    print("YOUR BALANCE IS :",bal)

############################################################################
dic = {"ATM_PIN": 2005}
bal=10000

Pin = int(input("ENTER A PIN: "))

if Pin == dic["ATM_PIN"]:
    print("OPTIONS \n1. WITHDRAW \n2. DEPOSIT \n3. CHECK BALANCE")
    c=int(input("Enter a option: "))
##############################################################################
    if c==1 :
       withdraw(bal) 

    elif c==2:
        deposit(bal)

    elif c==3:
        check(bal)


else:
    print("WRONG PIN , PLEASE ENTER CORRECT PIN :")

'''
'''
st=["de","dep","fgh"]
qu=["de","imm","fgh"]
c=0
for i in range(len(qu)):
    for j in range(len(st)):
        if qu[i]== st[j] :
            c+=1
print(c)

st = ["de", "dep", "fgh"]
qu = ["de", "imm", "fgh"]

for i in range(len(qu)):
    c = 0
    for j in range(len(st)):
        if qu[i] == st[j]:
            c += 1
    print(c)

def arrayManipulation(n, queries):
    arr = [0] * (n + 2)   # extra space for b+1 safety

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max_val = 0
    current = 0

    for i in range(1, n + 1):
        current += arr[i]
        if current > max_val:
            max_val = current

    return max_val

n, m = map(int, input().split())

arr = [0] * (n + 2)

# Taking queries input and updating difference array
for _ in range(m):
    a, b, k = map(int, input().split())
    arr[a] = arr[a] + k
    
    if (b + 1) <= n:
        arr[b + 1] = arr[b + 1] - k

# Prefix sum to find maximum
max_val = 0
current = 0

for i in range(1, n + 1):
    current = current + arr[i]
    
    if current > max_val:
        max_val = current

print(max_val)


'''

'''

class student:
    name=input()
    id=int(input())

    def show(self):
        print("NAME :",self.name)
        print("ID:",self.id)


obj=student()
obj.show()

class father:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def show(self):
        print("name:", self.name)
        print("roll no :",self.roll_no)


obj=father(name=input(),
roll_no=int(input()))
obj.show()







class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name, "Roll No:", self.roll_no, "Marks:", self.marks)


# # User Input
# name = input("Enter Student Name: ")
# roll_no = int(input("Enter Roll Number: "))
# marks = int(input("Enter Marks: "))

# Object Creation
s1 = Student(name = input(),roll_no = int(input()),marks = int(input()))

# Display Output
s1.display_details()



#square root
n=int(input())
k=0
for i in range (1,n+1):
    if i*i == n:
        k=i
if k*k==n:
    print(f"{k} it is square root of {n}")    
else:
    print("it is not perfect square root number ")

#missing number
n=[1,2,4,5]
m=len(n)+1
some = (m*(m+1))//2 
c=0
for i in n:
    c+=i
print(some-c)

#arrays equal or not
a=[1,2,3,4]
b=[1,2,3]
c=0
if len(a) == len(b):

    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    if c!= len(a):
        print("no")
    else:
        print("yes")
else:
    print("not matched")

    
a=[1,1,1,1,1,1]
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


def get(a,b):
    c=(a**b)%10
    # d=str(c)
    # e=d[-1]
    print(c)
a=int(input())
b=int(input())
get(a,b)

'''
        
