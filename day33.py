
#7.(?)
'''
----
-> This meta charcter will form a searching patterms as it will take any zero or one charcter for(?)
syntax --> re.findall(".?",variable_name)

import re
any=" This meta charcter "
an=re.findall("Th.?",any)
so=re.search("Th.?",any)
print(an)
print(so)

'''
#8.{}
'''
------
--> This meta charcter will form a searching patterns as we can mentioned the size in the {}

import re
any=" This meta charcter will form a searching patterns as it will take any zero or one charcter  "
an=re.findall(".{50}",any)
print(an)

'''

#9. (|)
'''
--------
--> This meta charcter will form a searching patterns as it consider right or left any string is present or not for (|)

import re
any=" This meta charcter will form "
an=re.findall("that|will",any)
print(an)

'''

#special sequence
'''
-----------------
A special sequence is a followed by one of the charcter are at the beginning of the string

1.\A
------
returns a match if the specified charcter are at the beginning of the string

EG: "\AThe"

import re
txt="The rain is spain"
#check if the string starts with "The":
x=re.findall("\AThe",txt)
print(x)

if x:
    print("yes, there is match!")
else:
    print("No match")

2.\b
------
return a match where the specified charcter are at the beginning or at the end of word

EG: r"\bain"


import re
txt = "The rain in spain"
#check if is present at the beginning of WORD:

x=re.findall(r"\bspain",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


3.\d
-----
--> returns a match if the string contains any digits (numbers from 0-9) 

EG: "\d"

import re
txt = "The rain in 56 spain"
#check if the string contains any digits (numbers from 0-9)

x=re.findall("\d",txt)
y=re.search("\d",txt)
print(x)
print(y)
if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


3.\D
-----
--> returns a match where the string DOES NOT contain digits

EG:"\D"

import re
txt = "The rain in 56 spain"
#Return a match at every no digit charcter:

x=re.findall("\D",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


4.\s
-----
--> returns a match where the string contains a white space character

EG: "\s"

import re
txt = "The rain in spain"
#Return a match at every white space character:

x=re.findall("\s",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


'''
# Time and DATE 
# ---------------------
'''

%d --> Day
%m --> Month
%Y --> Year
%H --> Hour
%M --> Min
%S --> Sec
%p --> AM/PM
%A --> Day name
%B --> Month name


import datetime
today = datetime.date.today()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))


'''






































