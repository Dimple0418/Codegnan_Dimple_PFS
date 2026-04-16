# introduction to OOP'S
# =========================

'''
# OOPS'S
-------
--> Object oriented programming languages -- it is a style of programming where we model real-world things as objects that contain both data and function ()
--> It helps you write clean, reusable, and organized code

OOP is a programming style where we create real-world like models using:

# Class
------
--> class is a blue print or template
--> A class is a template that defines properties and functions.
--> syntax - class class_name:



# Object
----------
--> An object is an instance (real copy) of a class.
--> An object is a real instance created from a class. It is the actual thing exists in memory while the program run 
-->  

==> Example:
      Class → Blueprint (design)
      Object → Real thing created from class
      
      Class = Car (design)
      Object = BMW, Audi (real cars)


# Attributes
-------------
---> Attributes are the variables inside a class that store data about an object.
---> Example: name, age, branch, marks, etc.

#1
class Student:
    def play(self):
        print("Hello Student")

s1 = Student()   # object
s1.play()

#2b 
class Student:
    def __init__(self,user,pin):
        self.user=user
        self.pin=pin

s1 = Student("DIMPLE","0418")
print(s1.user) # object

#3

class car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car_1=car("porsche", "black")
car_2=car("tata","white")
print(car_1.brand)
print(car_1.color)


#4
class car:
    wheels=4
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=20
    def drive(self,miles):
        self.mileage += miles
        return f"Drove {miles} miles.total: {self.mileage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"

car_1=car("ford","mustang","2008")
car_2=car("toyota","camry","2023")

print(car_1.info())
print(car_2.info())
print(car_2.drive(10))


'''











