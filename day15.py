#way to pass aruguments in calling function
#--------------
#---> required arguments --- the parameters and aruguments should be equal or it should match the same number variables in calling with def 

'''

num_1=9
num_2=1
def func(num_1,num_2):
    print(num_1 + num_2)
func(num_1,num_2)

'''

#---> default arguments ------ it will take default values from the arguments

'''

my_name="DIMPLE"
def name(my_name):
    print(my_name)
name("SRINUVASU RAO")
name("LAKSHMI")

'''

#prime number using function

'''

def add(num,count):
    for i in range (1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} it is prime number")
    else:
        print(f"{num} it not a prime number")
num=int(input("ENTER A VALUE : "))
count=0  
add(num,count)
'''



#keyword arrguments

'''
def fie(any_1,any_2,any_3):
    print(f"any_3={any_3}, any_2={any_2}, any_1={any_1}")
fie(any_3=2 ,any_1=9, any_2=0)

'''
'''
def add(num,count):
    for i in range (1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} it is prime number")
    else:
        print(f"{num} it not a prime number")
  
add(num=47,count=0)
add(num=9,count=0)
add(num=3,count=0)
add(num=51,count=0)
'''

#variable length argument --- adding a star (*) before the parameters name in function, receive a tuple of arguments and access items with indexes

'''

def name(*candidate_):
    print(candidate_[3])
name("Dimple","Raghu","Yochitha","nivas")

'''

#prac ques
#even or odd number


'''
def numb(n):
    if n % 2==0:
        print("even number")
    else:
        print("odd number")
        
numb(n=int(input("enter a value: ")))   
'''

#tables
'''
def type(num):
    for i in range (1,10+1):
        print(f"{num} x {i} = {num*i}")
num=int(input("ENTER A VALUE : "))
type(num)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''



#types of errors

# 1.syntax error --> if a function or any method is not ended properly using colon or parenthisis we get error  and also the statement should end uop with colon

    '''eg. for j in range():     #{error -- missing colon}
                print (j)'''
    
# 2.indentation error --> Indentend value is expected after a for statement there should be tab space 

     ''' eg. for j in range ():       #{error -- identation }
                 print (j)'''
# 3.attribute error --> use only methods for applicable datatypes, dont use for other

    ''' eg. a=[4,5,6]
            a.replace(9)         #{string method is replace it used for list }
            print(a) '''
# 4.type error --> the given values are differnt data types

    ''' eg. print(9+"dimple")     #{type error because 9 is int dimple is string} '''



    







