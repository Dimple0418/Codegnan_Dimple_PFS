'''
#Identifying vowels and Consonants
n=input("Enter a letter:")
if n in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")
'''

'''
#Time Format Converter 24hours to 12 hours time

time=input("Enter 24 hours time:")
parts=time.split(":")
hours=int(parts[0])
mins=int(parts[1])
if hours>=13 and mins<60:
    print(time,"Convert into",hours-12,":",mins,"Pm") #print(f"{time} Convert into {hours-12}:{mins}pm"
else:
    print("You have entered nrml or min are in correct")
'''



'''
#List--> What is a List in Python?

A List is a collection (group) of items stored in a single variable.

👉 Definition:
A list is a mutable, ordered collection of elements in Python.

🔹 Key Features of List
Ordered
Items have a fixed position (index starts from 0)
Mutable (Changeable)
You can modify, add, or remove elements
Allows Duplicates
Same values can appear multiple times
Heterogeneous
Can store different data types (int, string, float, etc.)

Eg--> [1,"Name",[1,2,"Teja"]]
'''

'''
List_1=[1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(List_1[4][2][0][3])
print(List_1[4][2][1][2])

Methods od list
---------------
append() ---> this method is used to add new item into list it will only go for the last index of the list
syntax---> Variable_name.append(item)

extend() ---> this method is used to add items into list in the last index , where each item or substring is each index in the list
syntax---> variable_name.extend(item)

remove()---> this method will delete the item or value directly from the list
syntax---> Variable_name.remove(item)

pop()--->this value delete the item based on index value
syntax--->Variable_name.pop(index value)



mutable--> I can directly modify on that particular variable
immutable---> I can not modify directly on the variable
'''

'''
#Example of Append
list=[1,2,3,4,5]
print(list)
list.append(23)
print(list)
list.append([21,22])
print(list)
list.append("Dimple")
print(list)

'''

'''
#Example of Extend
list=[1,2,3,4]
list.extend([23,4,5])
print(list)
list.extend("Dimple")
print(list)
list.append("Dimple")
print(list)
'''

'''
list_=[2,3,4]
list1=list_.extend("Dimple")
print(list1)
'''

'''
#example of remove
list_=[23,56,89,"Python"]
list_.remove(23)
print(list_)'''


list_=[23,34,56]
list_.pop(1)
print(list_)









