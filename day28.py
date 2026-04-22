# Polymorphism

'''
--> Polymorphism means “many forms”.
--> In Object-Oriented Programming, polymorphism allows the same function/method name to behave differently depending on the object or data type.
--> Simply: One name, different behavior.

This allows a object of different classes to be treated as instance of the same base class , with methods behaving differently based on the actual object type

eg.
-----
print(len("python"))
print(len([1,2,3]))

'''

# Method Overloading

'''
Method Overloading means:
➡ Same method name but different parameters (number/type of arguments).

eg..
#1
class calcualation:
    def add(self,a,b=0,c=0):
        return a+b+c

call=calcualation()
print(call.add(10))
print(call.add(10,5,5))
print(call.add(20,7,3))

#2
class calcualation:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
        
call=calcualation()
print(call.add(10,5))
print(call.sub(15,5))
print(call.mul(10,5))
    
'''

# Method Overriding

'''
Method Overriding means:
➡ A child class provides a new implementation of a method already defined in the parent class.

#3
class animal:
    def speak(self):
        return "sound"
class dog:
    def speak(self):
        return "bark"


obj=dog()
print(obj.speak())


#4
class Parent:
    def scoldings(self):
        return "Don't be lazy"

class Child(Parent):
    def scoldings(self):   # overriding
        return "Okay mom, I will work hard"

obj = Child()
print(obj.scoldings())

###########################################################


| Feature        | Overloading  | Overriding           |
| -------------- | ------------ | -------------------- |
| Happens in     | Same class   | Parent & Child class |
| Method name    | Same         | Same                 |
| Parameters     | Different    | Same                 |
| Python support | Not directly | Fully supported      |

'''


#operator overloading
'''
Operator Overloading means:
➡ Giving extra meaning to an operator (+ , - , * , / , > , <) for user-defined classes by implementing special methods.
Python allows this using magic methods / dunder methods like:
 __add__()     for +
 __sub__()     for -
 __mul__()     for *
 __truediv__() for /

#5
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return someone(self.a + other.a , self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"

dim = someone(2,3)
rag = someone(5,9)
print(dim + rag)

#6
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __sub__(self,other):
        return someone(self.a - other.a , self.b - other.b)

    def __str__(self):
        return f"({self.a}, {self.b})"
    
dim = someone(2,3)
rag = someone(5,9)
print(dim - rag)

#7
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(80)
s2 = Student(70)

print("Total Marks:", s1 + s2)

'''
#Data Abstraction 
'''
Data Abstraction means hiding internal implementation details and showing only the important features to the user.

--> What to do is shown, how it is done is hidden.

{ Real-Life Example

📌 When you drive a bike/car:

You know accelerator, brake, steering
But you don’t know the internal engine working

That is abstraction. }

🔹 Encapsulation = Data hiding (protect data)
🔹 Abstraction = Implementation hiding (hide working)

#8
from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius **2
    
circle = circle(5)
print(circle.area())

'''












