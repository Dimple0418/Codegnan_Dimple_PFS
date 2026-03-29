#basic questions solved
'''


Input Format:
Two integers, the first indicating the number of apples in the banana basket, the second indicating the number of bananas in the apple basket.

Output Format:
Two integers in a single line separated by a space: the corrected number of apples in the apple basket and bananas in the banana basket.

a=int(input())
b=int(input())
a,b=b,a
print(a,b)
-----------

Input Format:
Three strings (each on a new line):
Student ID (e.g., 23CS101)
Full name (e.g., "Aditi Sharma")
New branch name (e.g., "AI-DS")

Output Format:
Two lines:
Line 1: Print the student ID and full name (stored in valid variables).
Line 2: Print a message: Branch updated to: <new_branch> using valid variables only

student_id = input()
full_name = input()
new_branch = input()
print(student_id, full_name)
print("Branch updated to:", new_branch)
--------------------------------------------

Input Format:
Three strings on separate lines:
user ID
session token
login time (in any string format)

Output Format:
First line: All three variables printed space-separated.
Second line: Only the user_id variable is printed after deleting the others


a=input()
b=input()
c=input()
print(a,b,c,)
print(a)


------------------
Input Format:
Five strings, one per line, representing genome IDs (e.g., GENE123, ABC001, etc.)

Output Format:
Line 1: All five genome IDs printed in order, space-separated.
Line 2: All five variables printed again, with the first and last replaced by
"INVALID"

a=input()
b=input()
c=input()
d=input()
e=input()
print(a,b,c,d,e)
a="INVALID"
e="INVALID"
print(a,b,c,d,e)

---------------------
Input Format:
The first line contains the number of orange juice glasses sold.
The second line contains the number of apple juice glasses sold. The third line contains the number of carrot juice glasses sold.

Output Format:
First line: total number of juice glasses sold.
Second line: total money earned

a=int(input())
b=int(input())
c=int(input())
print((a+b+c))
d=a+b+c
print(d*18)

---------------------------

Input Format:
First line: distance (float or integer) run in the morning session
Second line: distance run in the afternoon session
Third line: distance run in the evening session.

Output Format:
First line: total distance covered
Second line: average distance per session

a=float(input())
b=float(input())
c=float(input())
print(a+b+c)
d=(a+b+c)/3
print(d)
--------------------------

 Input Format:
First line: number of notebooks purchased
Second line: number of pencils purchased
Third line: amount paid by the student

Output Format:
First line: total cost of the items

a=int(input())
b=int(input())
c=int(input())
d=(a*15)+(b*5)
e=c-d
print(d)
print(e)
-----------------------

Input Format:
First line: number of boxes.
Second line: number of caramel cubes per box
Third line: number of jelly beans per box

Output Format:
First line: total caramel cubes
Second line: total jelly beans
Third line: total number of sweets
Fourth line: total wrappers needed

a=int(input())
b=int(input())
c=int(input())
e=b*a
d=c*a
f=e+d
g=f
print(e)
print(d)
print(f)
print(g)
'''













