#even numbers

'''

a=eval(input())
b=[]
c=0
for i in a:
       if i %2==0:
              b.append(i)
              c+=1
if c==0:
       print(f"{a} there are no even number")
else:
       print(f"{a} this are even numbers ")
   
       
a=eval(input())
b=[]

for i in a:
       if i %2==0:
              b.append(i)
if len(b)>0:
       print(f"{b} thesse are even number")
else:
       print(f"{a} no are even numbers  in the list ")



a=eval(input())
b=[]
for i in a:
       if i %2==0:
              b.append(i)            
if len(b)==0:
       print(f"{a} there are no even number")
else:
       print(f"{b} this are even numbers ")
'''

#Armstrong number

'''
a=input()
b=len(a)
e=0
for i in a:
       c=int(i)
       e+=c**b
if e==int(a):
       print(f"{a} it is a armstrong number")
else:
       print(f"{a} it is not armstrong number")

'''












