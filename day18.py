
'''


 def list_1(arr,arr1,count):
     for i in arr:
         if i%2==0:
             arr1.append(i)
             count+=1
     if count==0:    
         print(f"Not a Single even number in list")
     else:
         print(f"{arr1} these are even numbers from the list")
 arr=eval(input())
 arr1=[]
 count=0
list_1(arr,arr1,count)                



def arm(input1,b,c,input2,a):
    input2=input1
    a=len(str(input1))
    while input1>0:
        b=input1%10
        c+=b**a
        input1=input1//10
    if input2==c:
        print(f"Yes, {input2} is a Armstrong Number")
    else:
        print(f"No,{input2} is not a Armstrong Number")
input1=int(input())
b=0
c=0
input2=0
a=0
arm(input1,b,c,input2,a)


'''

