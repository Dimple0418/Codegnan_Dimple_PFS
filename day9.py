

'''a="Python is a programming language"
vowel_count=0
space_count=0
consonant_count=0
for i in a:
    if i in "AEIOUaeiou":
        vowel_count+=1
  
    elif i in " ":
        space_count+=1

    else:
        consonant_count+=1
print(vowel_count)
print(space_count)
print(consonant_count)    '''



'''

a="Python is a programming language"
vowel_count=0
space_count=0
consonant_count=0
for i in a:
    if i in "AEIOUaeiou":
        vowel_count+=1
  
    elif i in " ":
        space_count+=1
print(vowel_count)
print(space_count)
print(len(a)-(vowel_count+space_count))'''    

#for loops
'''
#for i in range: In for  loop i is an initial variable that can acess in output directly never get an error in output
a=int(input())
print(a)
for i in range(1,11):
    print(i)

range()---> this is used to generate number
syntax---->range(start,end,step)
'''

'''
#step---> It skip the number according to position 
for i in range(1,21,2):
    print(i)'''

'''
#Type Conversion
#for coverting string to integer string should be contain only numbers
any2="abc"
any1="123"
print(list(any2))
print(tuple(any2))
print(int(any1))
'''

'''
so=123
print(str(so))
print(float(so))
'''

'''
an=[1,2,3]
print(str(an))
print(type(str(an)))
print(tuple(an))'''

'''

an=[(1,2),(3,4)]
print(dict(an))
'''
#palindrome
'''
a=input()
rev=""
for i in a:
    rev=i+rev
if rev==a:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
#even and odd numbers
'''
a=int(input())
for i in range(1,a+1):
    if i%2==0:
        print("Even:",i)
    else:
        print("Odd:",i)
'''










'''

prime_num=int(input("ENTER A NUMBER : "))
count=0
for i in range (1,prime_num+1):
    print(i)
    if prime_num % i == 0:
        count +=1
    print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")

for an in range(2,100):
    count=0
    for j in range(1,an+1):
        if an % j == 0:
            count+=1
    if count == 2:
        print(f"{an} is a prime")
    else :
        print(f"{an} is not a prime")


list_num=[1052,197,97,45,3,39,57,87,23]
for an in list_num : 
    count=0
    for j in range(1,an+1):
        if an % j ==0:
            count+=1
    if count==2:
        print(f"{an} is prime")
    else:
        print(f"{an} is not prime")

num=int(input())
for an in range(1,num+1):
    if an % 2==0:
        print(f"{an} it is a even number")
    else:
        print(f"{an} it is not a even number")


any=[2,356,8,6,3,2,8]
empty =[]
for an in any:
    if an not in empty:
        empty.append(an)
        print(empty)
'''

so=int(input())
length=len(str(so))
amstr=0
for j in str(so):
    amstr +=int(j) ** length
    print(amstr)
if amstr == so:
    print(f"{so} is amstrong num")
else:
    print(f"{so} is not amstrong num")
        
    














