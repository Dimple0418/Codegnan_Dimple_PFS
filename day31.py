# File handling
# --------------
'''
--> File handler is an object of file to maintain several functions of file such as creating,,reading,writing ,update and deleting file

How to open a file
------------------
1) Open()
----------

--> This open() function takes 2 parameters and in this we have to close the file by calling close() function after program

1.File name
2.Mode


2) With open()
----------------

Modes ("r","w","a","x","t")
------
'''

#1. "r" -- Read
'''
--------------
--> To read the file we use this mode and if the file dosent exit it will throw the error 

Eg.
---
any=open("dummy.txt","r")
print(any.read())
any.close()

'''

#2."w" -- Write
'''
--------------
--> To write the text into the file we will use this mode and it will create the file if it doesn't exist
--> It will over write new text with old text in the file.
Eg.
---
any=open("dummy.txt","w")
any.write(" To my mind the greatest reward ")
any.close()


any=open("other.txt","w")
any.write(" To my mind the greatest reward ")
any.close()


'''

#3."a" -- append
'''
-----------------
--> To add the text into the file this is used and it will create the file if it doesn't exist


Eg.
---

any=open("dummy.txt","a")
any.write("Granted a luxury")
any.close()

'''

#4."x" -- create
'''
------------------
--> This used to create the file , but if the file is there it will throw error

Eg.
----
any=open("BHANU.py","a")
any.write("Granted a luxury")
any.close()

'''

# To read a file
'''
----------------
1. Read()
--> This method can read the entire file chunk by chunk we can also specify the 

2. Readline()
--> This method can only read one line at a time

3. Readlines()
-->This method can read the entire file and return into list with each line is one index in the list

Eg.

any=open("dummy.txt","r")
print(any.read())
print(any.readline())
print(any.readlines())
any.close()





