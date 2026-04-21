#Inheritance
'''
3) multi-level -- inheritance happens in levels (A→B→C).
-------------
--> this occurs when a class inherits from a child class ,
--> creating a grandparent --> parent -> child in this structure

        A
        |
        B
        |
        C

#
class grandparent:
    def show_grandparent(self):
        print("I'm Grandparent")
        
class parent(grandparent):
    def show_parent(self):
        print("I'm parent")
        
class child(parent):
    def show_child(self):
        print("I'm child")

any=child()
any.show_grandparent()
any.show_parent()
any.show_child()

4) Hierachical -- One Parent → Many Children
--> In Hierarchical Inheritance, multiple child classes inherit from one parent class.

      Parent
     /     \
 Child1   Child2

# 
class Parent:
    def show(self):
        print("Parent class")

class child1(Parent):
    def msg1(self):
        print("Child1 class")

class child2(Parent):
    def msg2(self):
        print("Child2 class")

class child3(child1,child2):
    def msg3(self):
        print("i am the last child ")

    
obj1 = child3()
obj1.show()
obj1.msg1()
obj1.msg2()
obj1.msg3()


5)Hybrid inheritance

Hybrid Inheritance is a combination of two or more types of inheritance
(like multiple + multilevel).

Diagram:
        A
       / \
      B   C
       \ /
        D
        
'''
#

class Parent:
    def show(self):
        print("Parent class")

class child1(Parent):
    def msg1(self):
        print("Child1 class")

class child2(Parent):
    def msg2(self):
        print("Child2 class")

class child3(child1,child2,Parent):
    def msg3(self):
        print("i am the last child ")

    
obj1 = child3()
obj1.show()
obj1.msg1()
obj1.msg2()
obj1.msg3()




'''

class A:
    def msgA(self):
        print("Class A")

class B(A):
    def msgB(self):
        print("Class B")

class C(A):
    def msgC(self):
        print("Class C")

class D(B,C):
    def msgD(self):
        print("Class D")

obj = D()
obj.msgA()
obj.msgB()
obj.msgC()
obj.msgD()

'''
'''

| Type         | Meaning                          |
| ------------ | -------------------------------- |
| Single       | One parent → One child           |
| Multilevel   | Parent → Child → Grandchild      |
| Hierarchical | One parent → Many children       |
| Multiple     | Many parents → One child         |
| Hybrid       | Combination of inheritance types |

'''



























