#constructor --- (__init__)
#------------------------------
# --> A constructor is a special method used to intialize object data

'''

A constructor is a special method that is automatically called when an object is created.
It is mainly used to initialize variables (attributes).

🔹 In Python, constructor name is: __init__()

#1

class student:
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
    def display(self):
        print(self.name,self.Id)
stu_1=student("Dimple",418)
stu_1.display()
'''


# Access specifiers
# ------------------------
'''
Access Specifiers in Python (Access Modifiers)
Access specifiers decide who can access variables/methods inside a class.

Python has 3 types:

1) Public -- Can be accessed anywhere -- No underscore used -- [syntax => name]

class Demo:
    def __init__(self):
        self.name = "Public"

obj = Demo()
print(obj.name)


2) Protected -- Can be accessed inside the class and its child class -- Use single underscore _ -- [syntax => _name]

class Demo:
    def __init__(self):
        self._age = 20

obj = Demo()
print(obj._age)

Note: Protected is not fully restricted, but it's a convention.


3) private -- Can be accessed only inside the same class -- Use double underscore __ -- [syntax => __name]

class Demo:
    def __init__(self):
        self.__salary = 50000

obj = Demo()
print(obj._Demo__salary)   # print(obj.__salary)  ❌ Error


#2
  
class some:
    def __init__(self):
        self.public="public"
        self.protected="protected"
        self.private="private"
any= some()
print(any.public)
print(any._protected)
print(any.__private)

'''

# Self
# ------------------
'''
-->self represents the current object (instance) of the class.
--> It is used to access instance variables and instance methods.

Why do we use self?

To differentiate between:

local variables
object variables (attributes)

#3

class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable

    def display(self):
        print(self.name, self.age)

s1 = Student("Dimple", 20)
s1.display()
'''





















