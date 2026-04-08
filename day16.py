#Recursion functions
'''
-------------------------------
Recursion is a programming technique where a function calls itself either directly or indirectly to solve a prblm by breaking it into smaller,simpler sub problems.
Recursion is especially useful for prblms that can be divided into identical smaller tasks , such as mathematical calculations, tree traversals or divide-and-conquer algorithms.

'''
'''

def validate_pin(self):
    while self.remaining_attempts>0:
        user_pin = input("ENTER 4 DIGIT PIN: ")
        if len(user_pin) ==4 and user_pin == self.user_info["ATM PIN"]:
            print(" welcome to the ATM")
            return true
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"invalid pin . attempts left: {self.remaining_attempts}")
            else:
                print("card blocked. please contact customer service")
                return false
'''



#vowels and consonants
'''
def func(so,vowels_list,conso_list):
    for i in so:
        if i in "aeiouAEIOU":
            vowels_list.append(i)
        elif i == " " or i in "0123456789":
            pass
        else:
            conso_list.append(i)
    print(f"{vowels_list}")
    print(f"{conso_list}")
    
so=input("enter a sentence: ")
vowels_list=[]
conso_list=[]
func(so,vowels_list,conso_list)
'''

#factorial number

'''
def func(a,temp):
    for i in range (1,a+1):
        temp=temp*i
    print(f"{temp}")
    
a=int(input())
temp=1
func(a,temp)

'''


#ATM PROJECT

'''
ICIC_Dimple_AC_details={"Name":"Dimple","ATM PIN": "2005","Balance":5000}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")

ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    
    if ICIC_user_pin in ICIC_Dimple_AC_details["ATM PIN"]:
        user_choice=int(input("Enter \n1.Withdraw:  \n2.Deposite: "))
        if user_choice==1:
            
            money_w=int(input("Enter money you want to withdraw"))
            if money_w<=ICIC_Dimple_AC_details["Balance"]:
                ICIC_Dimple_AC_details["Balance"] -= money_w
                print(ICIC_Dimple_AC_details["Balance"])
                
            else:
                print("insuff")
                
        elif user_choice==2:
            Deposite_m = int(input("plz enter the money you want to deposite: "))
            
            if Deposite_m % 100 == 0 and Deposite_m >=5000:
                ICIC_Dimple_AC_details["Balance"]+=Deposite_m
                
                print(f"you have depostied {Deposite_m} and the total ammount is {ICIC_Dimple_AC_details["Balance"]}")
            else:
                print(f"{Deposite_m} you have entered is change or less than given amount {5000}")
        else:
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")

'''































