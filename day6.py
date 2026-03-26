
'''
print(9+8) 
print("python"+"language")---> concatenation '''

#concatenation ()
'''
-----------------
This is nothing but ,a (+) behaviour

case=1__>
integers  --- this will acts as addition for thw int

case=2___>

for other datatypes(we have to use same types) this (+) cts as a concatenation
we try to access two different data types
 
print("string"+[1,2])  TypeError: can only concatenate str (not "list") to str

print(1+[2,3]) TypeError: unsupported operand type(s) for +: 'int' and 'list'


'''

#tuple()

'''Tuple is a collection of different datatypes and this represented by 'paranthisis'() and then separated by (,) 'comas'

type_d=(1,"dimple",[2,3],(4,5))
print(type_d)

type_c=("hello",54,[4,8])
print(type_c)


thing=(12,89,"python",(23,"dimple",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing[3][2][1][9])

thing=(12,89,"python",(23,"dimple",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing[3][2][2])'''
#swap
'''
a=1
b=90
a,b=b,a
print(a,b)

a=int(input())
b=int(input())
a,b=b,a
print(a,b)


a=input()
b=input()
a,b=b,a
print(a,b)

'''

#leapyear code
'''
leap_year=int(input("Enter a year:"))
if (leap_year % 4==0 and leap_year % 100!= 0) or leap_year % 400 ==0 :
    print(f"yes,{leap_year}it is a leap year")
else:
    print(f"no,{leap_year}it is not a leap year")


leap_year=int(input("Enter a year:"))
if (leap_year % 4==0 and leap_year % 100!= 0) or leap_year % 400 ==0 :
    print("yes,it is a leap year")
else:
    print("no,it is not leap year")


'''























