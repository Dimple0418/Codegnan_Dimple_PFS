#Datatypes

#string()
''' String ---> string is a collection of char,which represented by "" or ''  and we can access the using indexing  

any = 'i am learning python programming'
print (any [10])''' 'if we give more than one number or bunch of numbers at a time we get error print (any[3,4,5]) -- we get erros '

#slicing()
''' slicing -- syntax [0:0] if we want certain type of letters then we use slicing 

any = 'i am learning python programming'
print (any[5:20]) '''


#mutable and immutable
'''mutable and immutable --->
string imuutable & list mutable
any = 'java programming'
so = any.replace("java" ,"python")
print (any)
print (so)'''


'''my_name = 'ch Dimple'
print(f"my name is {my_name}[0:9]")

my_name = '  ch Dimple,i am currently pursuing btech final year.'
print(f"my name is {my_name[0:9]}")

my_name = 'ch Dimple,i am currently pursuing btech final year.'
print(f"my name is {my_name[-1:-3]}")

my_name = 'ch Dimple,i am currently pursuing btech final year.'  --> its is a step function slicing
print(f"my name is {my_name[-1:-6:-1]}")

my_name = 'ch Dimple,i am currently pursuing btech final year.'
print(f"my name is {my_name[::-1]}")'''

#len method

'''my_name = 'ch Dimple,i am currently pursuing btech final year.'
print(len(my_name))

list_num= 12345  --> not possible using string we get errors
print(len(list_num))

list_num= 12345
a= str(list_num) ---> here we used string function to convert int into string 
print(a) 

sum = "123"
print(sum)

some = "123rd"
num = str(some)
print (num)'''


#note:- we can convert a stirng into integer, if they contain only integer value'''

#methods of string
#-----------------

#split method
'''split()---> remove space, and this is in the list [] it will give the sperated thing in each index -- syntax :  variable_name.split() 


name_of= "python is a programming langugage "
print (name_of.split())

name_of= "python is a programming langugage "
print (name_of.split(" "))

name_of= "python is a programming langugage "
print (name_of.split("programming"))'''

#lower method --> 
''' lower()-->this is used to to convert all letters into lower case -- syntax:  variable_name.lower()

num_1="I Am VerY MuCh InteResTed In vLsi sTreaM"
print(num_1.lower())'''


#upper method --> 
''' upper ()-->this is used to to convert all letters into upper case -- syntax:  variable_name.upper()

num_1="I Am VerY MuCh InteResTed In vLsi sTreaM"
print(num_1.upper())


some = "I Am VerY MuCh InteResTed In vLsi sTreaM"
if "U" in some:
    print("yes,it is there")
else:
    print("no,it is not there")


some = "I Am VerY MuCh InteResTed In vLsi sTreaM"
if "e" in some:
    print("yes,it is there")
else:
    print("no,it is not there")'''

#join method
'''join() ---> this is used to join the string -- syntax: variable_name.join()

name = "Python is a programming language"
print(name.join("-"))'''

#replace method
'''replace() ---> this is used to replace the string -- syntax: variable_name.replace("old string","new string")

name = "Python is a programming language"
print(name.replace("programming","interpretur"))'''



'''name = "Python is a programming language"
if "is" in name:
    print("yes it is there")
else:
    print("no it is not there")

name = "Python is a programming language"
if "ython" in name:
    print("yes it is there")
else:
    print("no it is not there")'''




















