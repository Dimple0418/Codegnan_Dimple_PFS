

def withdraw(bal):
    user=int(input("ENTER AMOUNT FOR WITHDRAW : "))
    bal-=user
    return bal

def deposit(bal):
    user_1=int(input("ENTER A AMOUNT: "))
    bal+=user_1
    return bal

def check(bal):
    print("YOUR BALANCE IS :",bal)

############################################################################
dic = {"ATM_PIN": 2005}
bal=10000

while True:
        Pin = int(input("ENTER A PIN: "))
        if Pin == dic["ATM_PIN"]:
                print("**************************")
                print("OPTIONS \n1. WITHDRAW \n2. DEPOSIT \n3. CHECK BALANCE \n4. PIN CHANGE")
                c=int(input("Enter a option: "))

                if c==1 :
                 bal=withdraw(bal) 

                elif c==2:
                    bal=deposit(bal)

                elif c==3:
                    check(bal)
                
                elif c==4:
                  d=int(input("ENTER YOUR OLD PIN: "))
                  if d==dic["ATM_PIN"]:
                    e=int(input("ENTER YOUR NEW PIN: "))
                    dic["ATM_PIN"]=e
                  else:
                      print("ENTER CORRECT PIN") 
                      break
                   

        else:
            print("WRONG PIN , PLEASE ENTER CORRECT PIN :")
            
