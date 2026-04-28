#Regular Expression (Reg Ex)
#---------------------------
'''

--> This regular expression or RegEx is a sequence of charcters that forms a searching pattern
--> To use this we have to import re, which will unlock the

Functions
----------
1.Findall
--> By using this function it will find all the sequence of characters in the string
syntax -> re.findall("metachar",variable_name)

Eg.

import re
any = "python is a language"
so= re.findall("a",any)
print(so)


2.Search
--> By using this function , it will only find the first sequence in the string
syntax -> re.search("metachar",variable_name)

Eg.

import re
any = "python is a language"
so= re.search("a",any)
print(so)


# Metacharacters
-------------
--> Metacharcters are used to form searching pattern 

1.[] --> in this metacharcters we can search for [a-z],[A-Z],[0-9]
-----
Eg.

import re
any = "a lot was left unsaid"
so= re.findall("[a-z]",any)
the=re.search("a",any)
print(so)
print(the)

import re
any = "a lot was left unsaid"
so= re.findall("[aes]",any)
print(so)

import re
any = "a 0lot was 4 left 1unsaid 8"
so= re.findall("[0-9]",any)
print
(so)

import re
any = "a 0lot was 4 left 1unsaid 8"
so= re.findall("[0-9a-z]",any)
print(so)


2.dot(.)
--------

Eg.
---
import re
we="hello"
the=re.findall("h...o",we)
some=re.search("h...o",we)
print(the)
print(some)

3. cap(^) -> This is used to find the string is starting with the sequence or  
--------- 
syntax -> re.findall("metachar",variable_name)

Eg.
----
import re
many="dream inspire focus motivate improve creative positive"
so=re.findall("^dream",many)
then=re.search("^dream",many)
print(many)
print(then)

4. dollar($) ->  This is used to find the string is ending with the sequence
-------------
syntax -> re.findall("metachar",variable_name)

Eg.
---

import re
out="This is used to find the string is ending with the sequence   "
one=re.findall("sequence   $",out)
two=re.search("This$",out)
print(one)
print(two)


5. (*) --> This meta character will form a searching pattern as it will take any zero or more charcter for (*)
--------

Eg.
----

import re
dimple="  This is used to find the string is ending with the sequence "
gk=re.findall("T.*s",dimple)
mk=re.search("T.*",dimple)
print(gk)
print(mk)


6.(+) --> This meta character will form a searching pattern as it will take any one or more charcter for (+)
------
'''

import re
dimple="  This is used to find the string is ending with the sequence "
gk=re.findall("en.+g",dimple)
mk=re.search("t.+",dimple)

print(gk)

print(mk)
















