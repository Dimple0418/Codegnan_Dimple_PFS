#Encapsulation
#---------------
'''
---> The principle of binding data (attributes) and methods that operate on that data into a single unit, which is a class

Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to the data.

In simple words:
Data hiding + controlled access is called Encapsulation.

Why Encapsulation is used?

--Protects data from unauthorized access
--Improves security
Makes code reusable and maintainable
Controls how variables are modified

Access Specifiers in Python (Encapsulation)

Python has 3 types of access levels:
publice,protected,private


#1-code

class SBI_AC:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposite(self,amount):
        self.__balance+=amount
        
    def get_balance(self):
        return self.__balance

acc=SBI_AC(15000)
acc.deposite(7000)
print(acc.get_balance())
 '''   


#Inhertiance
#------------
'''
--> This allows a child class (subclass) to acquire the attributes and methods of a parent class (base class)  this is called INHERITANCE
-->It helps in code reuse and reduces duplication.

1) Single Inheritance: One parent → one child
2) Multiple Inheritance: Multiple parents → one child

#syntax --

class Parent:
    pass

class Child(Parent):
    pass

# Example of Inheritance

#2-code
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()      # Parent method
obj.display()   # Child method


1) Single inhertiance

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()

obj.show()
obj.display()

2) multiple inheritance

class Father:
    def skill_1(self):
        print("hardworking")

class Mother:
    def skill_2(self):
        print("cooking")

class child(Father,Mother):
    def skill_3(self):
        print("programming")

obj = child()
obj.skill_1()
obj.skill_2()
obj.skill_3()

'''
# super()
# ---------
'''
--> super() is used to call the parent (superclass) methods or constructor from the child (subclass).
      It helps in reusing parent class code without rewriting it.

Why we use super()?
 To call parent constructor inside child constructor
 To call parent method inside child method
 To avoid rewriting same code
 Useful in multiple inheritance also

super() is a built-in function used to access parent class methods and constructors inside a child class.

#using single inheritance

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        super().show()

obj = Child()
obj.display()

#using multiple inheritance


class Father:
    def skill(self):
        print("hardworking")

class Mother:
    def skill(self):
        print("cooking")

class child(Father,Mother):
    def skill_3(self):
        super().skill()
        print("DANCEER")

obj = child()
obj.skill_3()


'''
















































