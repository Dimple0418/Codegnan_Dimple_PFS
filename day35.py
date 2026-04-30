# Task
# ---

#1.
'''
import matplotlib.pyplot as pit
x=["TIGER","CHEETHA","POLAR BEAR"]
y=[100,150,240]

pit.bar(x,y,color="brown")
pit.title("Speed of animals")
pit.xlabel("ANIMALS")
pit.ylabel("SPEED")
pit.show()


'''
#2.

'''
import matplotlib.pyplot as pit
x=["NTV","NDTV","TV9","SUMAN TV"]
y=[200,150,240,120]

pit.scatter(x,y,color="PURPLE",s=200)
pit.title("REPORTS")
pit.xlabel("TV CHANNELS")
pit.ylabel("GROWTH")
pit.show()

'''

#3.
'''
import matplotlib.pyplot as pit
pit.pie([40,15,35,20],labels=["Backend(PYTHON)","Frontend(HTML,CSS)","Libraries(NUMPY,PANDAS)","Frameworks(FLASK)"])
pit.title("ATM APPLICATION (PROJECT)")
pit.legend(["RAGHU","TARUN","DIMPLE","AVANTHI"])
pit.show()

'''
#TASK - 2

#PROJECT 

'''
import matplotlib.pyplot as pit
books=["Mockingbird","Gatsby","Pridee","The Kite ","Atomic ","Ikigai","Alchemist","Sapiens","Patient","Depressed"]
prices=[300,200,1000,250,450,700,900,1200,2000,700]
pit.bar(books,prices)
pit.title("TOP BOOKS")
pit.xlabel("BOOKS NAMES")
pit.ylabel("PRICES")
pit.show()



 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

#step 1: WEB SCARPING
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding='utf-8'
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text,"html.parser")

books = soup.find_all("article",class_="product_pod")

names=[]
prices=[]

for book in books:
    name = book.h3.a["title"]

    #get raw price text
    price_text = book.find("p",class_="price_color").text

    #Extract numeric value using regex(fix for issue)
    price = float(re.findall(r'\d+\.\d+',price_text)[0])
    
    names.append(name)
    prices.append(price)

#step 2: store data in table

df = pd.DataFrame({
    "Book Name" : names,
    "price": prices
})

print("\n📊 Table Data:\n")
print(df.head())

#save to csv

df.to_csv("books_data.csv", index=False)
print("\n ✅ csv file 'books_data.csv'created succesfully!")

#step 3 : Data visulaization

plt.figure()
plt.bar(names[:10],prices[:10])
plt.xticks(rotation=90)
plt.xlabel("book names")
plt.ylabel("prices")
plt.title("book prices(top 10)")
plt.tight_layout()
plt.show()

'''

































