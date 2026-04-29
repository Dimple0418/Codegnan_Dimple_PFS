# --> TASK 

'''
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern,name)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern,email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern,phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern,password)

def main():
    name=input("Enter Name: ")
    email=input("Enter Email: ")
    phone=input("Enter Phone Number: ")
    password=input("Enter Password: ")

    if not validate_name(name):
        print("Invalid Name")
    elif not validate_email(email):
        print("Invalid Email")
    elif not validate_phone(phone):
        print("Invalid Phone Number")
    elif not validate_password(password):
        print("Invalid Password")
    else:
        print("All inputs are valid ! form submitted successfull ")
        
if __name__=="__main__":
    main()

 # --  DATA ANALYSIS  -- 

 why is this needed?
-> This is critical becoz it converts raw data into actionable insights,enabling information to decision - making easy and improve
operational efficeiency ...
-> Data analysis is the process of collecting, cleaning, organizing, and interpreting data to extract meaningful insights.

 1.Decision making
 2.Improved opeartional efficiency
 3.Customer understanding
 4.Market insight
 5.Risk management
 6.Data - Driven stratigies 

'''
#LINE PLOT
'''
 # 1.Eg..

import matplotlib.pyplot as pit
x=[1,2,3,4,5]
y=[10,20,15,25,7]

pit.plot(x,y)
pit.show()

  # 2. Eg..

import matplotlib.pyplot as pit
x=[100,20,30,40,50]
y=[1,2,3,4,5]

pit.plot(y,x)
pit.show()

'''
#BAR GRAPH
'''
   # 3. Eg..
   
import matplotlib.pyplot as pit
pit.bar(["TV9","NDTV","SUMANTV"],[10,5,25])
pit.show()

   # 4. Eg..

import matplotlib.pyplot as pit
x=["TIGER","CHEETHA","POLAR BEAR"]
y=[100,150,240]

pit.bar(x,y)
pit.show()

'''
#PIE CHART
'''
   # 5. Eg..
   
import matplotlib.pyplot as pit
pit.pie([35,15,25,25],labels = ["Avanthi","Sai","Dimple","Yochitha"])
pit.show()

   # 6. Eg..

import matplotlib.pyplot as pit
aim=[35,15,25,25]
app= ["Avanthi","Sai","Dimple","Yochitha"]
pit.pie(aim,labels=app)
pit.show()

'''
#HISTOGRAM

'''
    # 7. Eg..
import matplotlib.pyplot as pit
pit.hist([23,14,78,12])
pit.show()

     #8. Eg..

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90, 95]

plt.hist(marks, bins=6, edgecolor="black")
plt.title("Histogram of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()


'''

#NUMPY -- NumPy = Fast calculations + Powerful arrays in Python

'''
NumPy means Numerical Python. 

It is a Python library used for working with numbers, arrays, and mathematical operations very efficiently.

 Why NumPy is used?

NumPy helps in:

Creating arrays (faster than Python lists)
Performing mathematical calculations
Doing matrix operations
Handling large datasets
Supporting data analysis & machine learning


  #1.Eg..

import numpy as np
arr=np.array([1,2,3])
print(arr+1)

  #2.Eg..
  
import numpy as np
arr=np.array([1,2,3])
print(arr-1)

   #3.Eg..
   
import numpy as np
mat = np.array([[1, 2, 3],[4, 5, 6]])
print(mat)

    #4.Eg..
    
import numpy as np
a = np.zeros(5)
b = np.ones(5)
print(a)
print(b)

     #5.Eg..
     
import numpy as np
a = np.zeros(5)
b = np.ones(5)
print(a)
print(b)
print(c)

     #6.Eg..
     
import numpy as np
twos = np.ones(5) * 2
threes = np.ones(5) * 3
print(twos)
print(threes)

    #7.Eg..
    
import numpy as np
arr = np.arange(1, 11)
print(arr)

    #8.Eg..
    
import numpy as np
arr = np.arange(1, 13)
new_arr = arr.reshape(4, 3)
print(new_arr)

'''


#PANDAS
'''
------
-->Pandas is used for handling structured data in table format


pip install pandas

   #1.Eg..
   
import pandas as pd
data={"Name":["Raghu","Dimple"],"Marks": [35,89]}
any=pd.DataFrame(data)
print(any)






































































