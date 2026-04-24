#Handling Errors
#-----------------

'''
1) Try Block
-------------
-->The try block will test a block of code for errors

Eg.
----
try:
    print(b)
    
########################################################

2) Except Block
------------------
--> Tis block will take care of any errors

Eg.
------ 
try:
    print(b)
except:
    print("This block can handle error")
    
#####################################################    

3) Else block
---------------
--> Else keyword to define a block of code to be excuted if no error were raised

Eg.
------
try:
    a=9
    b=10
    print(a+b)
except:
    print("ERROR IN CODE")
else:
    print("NO ERROR IN THE CODE")
   


4) Finally block
-----------------
-->This block will execute either try block have any error or no error

Eg.
-------
try:
    a=9
    b=10
    print(a+b)
except:
    print("ERROR IN CODE")
else:
    print("NO ERROR IN THE CODE")
finally:
    print("THE TRY ERROR BLOCK IS FINISHED")

try:
    a=9
    b=10
    print(a+b+c)
except:
    print("ERROR IN CODE")
else:
    print("NO ERROR IN THE CODE")
finally:
    print("THE TRY ERROR BLOCK IS FINISHED")

#1 --

try:
    num=int(input("Enter a number : "))
    num1=int(input("Enter a number : "))
    result=num/num1
    
except ValueError:
    print("plz enter a valid number")
except ZeroDivisionError:
    print("cannot divisible by zero")
else:
    print(f"result = {result}")
finally:
    print("program completed")



'''











































