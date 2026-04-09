#lambda function --- syntax -> lambda(keyword) arguments : expression 
#----------------------------------------------------
# lambda function is also called as anonymous function
# A lambda function can take n number of aerguments but have only one expression.

'''
type=lambda file : file+10
print(type(5))

tim=lambda file,do : file+do+10
print(type(6,5))

tle=lambda so,to : so-to-8
print(type(10,5))


type=lambda rag,dimp,taru :rag*dimp-taru
print(type(5,5,5))


pie=lambda wh,th,um : (wh-th)+um
print(type(40,30,20))


type=lambda wh,th,um : (wh-th)*um
print(type(30,10,5))


any=lambda wh,th,um : (wh-th)*um,um+wh
print(any(40,30,20))                        -- you cannot give more than one expression we get error -- 


so=lambda yo,la,sr,di: (yo/sr)/la*di
print(so(100,20,10,40))

file=lambda sum,omi:(sum*omi)
print(file())

'''

#list comprehensions --- syntax -> varaiable_name = [expression loop or condition]
#--------------------------
#This is offers the shortest syntax when you want to create a new list from the existing list


#old list to new list 
'''
old_list=[1,2,3,4,5]
new_list=[i for i in old_list]
print(new_list)
'''

#even numbers
'''
old_list=[1,2,3,4,5,6]
new_list=[i for i in old_list if i % 2==0]
print(new_list)

'''

#print length of list

'''

type_1=["dimple", "sai" , "raghu", "tarun"]
type_2=[k for k in type_1 ]
print(len(type_2))

'''















